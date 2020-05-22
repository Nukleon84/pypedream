
from .base_element import BaseElement
from ..thermodynamics.data.thermodynamic_system import ThermodynamicSystem
from ..unitsofmeasure import PhysicalDimension
from ..numerics import AlgebraicSystem
from ..expressions import Par, SymSum

class MaterialStream(BaseElement):
    def __init__(self, name,system:ThermodynamicSystem):
        super(MaterialStream, self).__init__(name,system)

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
            #self.addVar(system.variableFactory.createVariable("K",c.id,"Equilibrium coefficient",PhysicalDimension.Dimensionless))
        return
    
    def ftpz(self, f,t,p, z):        
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
        self.F.fixValue(f)
        self.VF.fixValue(v)
        self.P.fixValue(p)
        
        for c in self.system.components:
             self.getVar(f"z[{c.id}]").fixValue(0)

        for pair in z:
            self.getVar(f"z[{pair[0]}]").fixValue(pair[1])

        self.init()
        return self        
    
    def init(self):
        self.L.value= (0.5*self.F.value)
        self.V.value= (0.5*self.F.value)
        
        if(not self.V.isFixed):
            self.VF.value=0.5
        
        for c in self.system.components:
            self.getVar(f"x[{c.id}]").setValue(self.getVar(f"z[{c.id}]").value*0.9)
            self.getVar(f"y[{c.id}]").setValue(self.getVar(f"z[{c.id}]").value*1.1)           

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
       
        for c in self.system.components:            
            xi=self.getVar(f"x[{c.id}]")
            yi=self.getVar(f"y[{c.id}]")
            zi=self.getVar(f"z[{c.id}]")     

            Ki=self.system.expressionFactory.EquilibriumCoefficient(c,T,P,x,y)
            instance.eq( yi-Ki*xi , "Equilibrium"  )
            instance.eq( zi - VF*yi- Par(1-VF)*xi , "Component Balance"  )

        instance.eq( SymSum(y)-SymSum(x) , "Mole Fraction Closure (two-phase)"  )                    
        return