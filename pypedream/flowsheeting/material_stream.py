
from .base_element import BaseElement
from ..thermodynamics import ThermodynamicSystem, PhaseState
from ..unitsofmeasure import PhysicalDimension
from ..numerics import AlgebraicSystem, ScalarMethods
from ..expressions import Par, SymSum, Alias

class MaterialStream(BaseElement):
    def __init__(self, name,system:ThermodynamicSystem):
        super(MaterialStream, self).__init__(name,system)

        self.state= PhaseState.LiquidVapor
        self.addVar(system.variableFactory.createVariable("T","","Stream Temperature",PhysicalDimension.Temperature))
        self.addVar(system.variableFactory.createVariable("P","","Stream Pressure",PhysicalDimension.Pressure))
        self.addVar(system.variableFactory.createVariable("F","","Stream Molar Flow",PhysicalDimension.MolarFlow))
        self.addVar(system.variableFactory.createVariable("L","","Liquid Molar Flow",PhysicalDimension.MolarFlow))
        self.addVar(system.variableFactory.createVariable("V","","Vapor Molar Flow",PhysicalDimension.MolarFlow))
        #self.addVar(system.variableFactory.createVariable("H","","Stream Enthalpy",PhysicalDimension.SpecificMolarEnthalpy))
        self.addVar(system.variableFactory.createVariable("VF","","Stream Molar Vapor Fraction",PhysicalDimension.MolarFraction))

        self.T=  self.getVar("T")
        self.P=  self.getVar("P")
        self.F=  self.getVar("F")
        self.V=  self.getVar("V")
        self.L=  self.getVar("L")
        self.VF=  self.getVar("VF")
        self.x=[]
        self.y=[]
        self.z=[]
        self.K=[]
        for c in system.components:
            zi=system.variableFactory.createVariable("z",c.id,"Mixed Molar composition",PhysicalDimension.MolarFraction)                        
            xi=system.variableFactory.createVariable("x",c.id,"Liquid Molar composition",PhysicalDimension.MolarFraction)
            yi=system.variableFactory.createVariable("y",c.id,"Vapor Molar composition",PhysicalDimension.MolarFraction)
            
            self.addVar(zi)
            self.addVar(xi)            
            self.addVar(yi)

            self.x.append(xi)
            self.y.append(yi)
            self.z.append(zi)
            Ki=Alias(f"K[{c.id}]",self.system.expressionFactory.EquilibriumCoefficient(c,self.T,self.P,self.x,self.y))
            self.K.append(Ki)
        return
    
    def ftpz(self, f,t,p, z):    
        self.VF.unfix()    
        self.F.fixValue(f)
        self.T.fixValue(t)
        self.P.fixValue(p)
        
        for c in self.system.components:
             self.getVar(f"z[{c.id}]").fixValue(0)

        for pair in z:
            self.getVar(f"z[{pair[0]}]").fixValue(pair[1])

        self.init()
        return self
    
    def fvpz(self, f,v,p, z):        
        self.T.unfix()
        self.F.fixValue(f)
        self.VF.fixValue(v)
        self.P.fixValue(p)
        
        for c in self.system.components:
             self.getVar(f"z[{c.id}]").fixValue(0)

        for pair in z:
            self.getVar(f"z[{pair[0]}]").fixValue(pair[1])

        self.init()
        return self        

    def fpx(self, f,p, x):     
        self.T.unfix()   
        self.F.fixValue(f)
        self.VF.fixValue(0.0)
        self.P.fixValue(p)
        
        for c in self.system.components:
             self.getVar(f"z[{c.id}]").fixValue(0)

        for pair in x:
            self.getVar(f"z[{pair[0]}]").fixValue(pair[1])

        self.init()
        return self  

    def fpy(self, f,p, y):   
        self.T.unfix()     
        self.F.fixValue(f)
        self.VF.fixValue(1.0)
        self.P.fixValue(p)
        
        for c in self.system.components:
             self.getVar(f"z[{c.id}]").fixValue(0)

        for pair in y:
            self.getVar(f"z[{pair[0]}]").fixValue(pair[1])

        self.init()
        return self          
    
    def init(self):
        if(self.T.isFixed and self.P.isFixed):
            self.flashP(self.VF)
        if(self.VF.isFixed and self.P.isFixed):
            self.flashP(self.T)
        return


    def __generateRachfordRice(self):
        rachfordRice=None
        for i,c in enumerate(self.system.components):            
            if(rachfordRice==None):
                rachfordRice = self.z[i]*Par(1-self.K[i])/Par(1+ self.VF *Par(self.K[i]-1))
            else:
                rachfordRice += self.z[i]*Par(1-self.K[i])/Par(1+ self.VF *Par(self.K[i]-1))
        return rachfordRice

    
    def flashP(self,solveFor):
        rachfordRice=self.__generateRachfordRice()

        if(solveFor==self.VF):
            #Solve for unknown vapor fraction
            rachfordRice.reset()
            self.VF.value=0
            rrAt0= rachfordRice.eval()
            
            rachfordRice.reset()
            self.VF.value=1
            rrAt1= rachfordRice.eval()

            if(rrAt0>0 and rrAt1>0):
                self.state=PhaseState.Liquid
                self.VF.value=0
            if(rrAt0>0 and rrAt1==0):
                self.state=PhaseState.BubblePoint
                self.VF.value=0    
            if(rrAt0<0 and rrAt1>0):
                self.state=PhaseState.LiquidVapor
                self.VF.value=0.5
            if(rrAt0==0 and rrAt1<0):
                self.state=PhaseState.DewPoint
                self.VF.value=1  
            if(rrAt0<0 and rrAt1<0):
                self.state=PhaseState.Vapor
                self.VF.value=1                                                      

        if(self.state== PhaseState.LiquidVapor or self.state==PhaseState.BubblePoint or self.state==PhaseState.DewPoint):
            ScalarMethods.solveNewtonRaphson(rachfordRice, solveFor)

        self.V.value= self.VF.value*self.F.value
        self.L.value= self.F.value-self.V.value
        
        for i,c in enumerate(self.system.components):            
            self.x[i].value= self.z[i].value/(1 + self.VF.value*(self.K[i].value-1))
            self.y[i].value= self.x[i].value*self.K[i].value  
        return

    def instantiate(self, instance:AlgebraicSystem):
        super(MaterialStream, self).instantiate(instance)
        
        F=self.F
        V=self.V
        L=self.L
        T=self.T
        P=self.P
        VF=self.VF
        x=self.x
        y=self.y

        instance.eq( VF*F - V , "Vapor Fraction"  )
        instance.eq( F - L- V , "Total mole balance"  )
        instance.eq( SymSum(y)-SymSum(x) , "Mole Fraction Closure (two-phase)"  )
       
        for i,c in enumerate(self.system.components): 
            instance.eq( self.y[i] - self.K[i]*self.x[i] , "Equilibrium"  )
            instance.eq( self.z[i]   - VF*self.y[i]- Par(1-VF)*self.x[i] , "Component Balance"  )
                            
        return