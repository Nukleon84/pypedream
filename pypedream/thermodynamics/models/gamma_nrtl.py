from ...expressions import Expression, SymSum,Ln,Exp,Par, Literal,Alias
from ...thermodynamics import PhaseState
from ...thermodynamics.data.binary_parameters import BinaryParameterSet, BinaryParameterSetType
class GammaNRTL(Expression):
    def __init__(self, system , T , x, c):
        super(GammaNRTL,self).__init__()
        self.arguments=[]        
        self.arguments.append(T)
        self.arguments.extend(x)
        
        i= system.components.index(c)
        A= system.binaryParameters[BinaryParameterSetType.NRTL].matrices["A"]
        B= system.binaryParameters[BinaryParameterSetType.NRTL].matrices["B"]
        C= system.binaryParameters[BinaryParameterSetType.NRTL].matrices["C"]
        D= system.binaryParameters[BinaryParameterSetType.NRTL].matrices["D"]
        E= system.binaryParameters[BinaryParameterSetType.NRTL].matrices["E"]
        F= system.binaryParameters[BinaryParameterSetType.NRTL].matrices["F"]
        
        NC= system.getNumberOfComponents()
        tau = [[0 for x in range(NC)] for y in range(NC)] 
        G = [[0 for x in range(NC)] for y in range(NC)] 

        for ii in range(NC):
            for j in range(NC):
                tau[ii][j] = Literal(A[ii,j])
                if(B[ii,j]!= 0.0):
                    tau[ii][j] += Literal(B[ii,j])/T
                if(E[ii,j]!= 0.0):
                    tau[ii][j] += Literal(E[ii,j])*Ln(T)
                if(F[ii,j]!= 0.0):
                    tau[ii][j] += Literal(F[ii,j])*T
                tau[ii][j]=Par(tau[ii][j])

                sij= Literal(C[ii,j])
                if(D[ii,j]!= 0.0):
                    sij+=Literal(D[ii,j])*(T-273.15)
                
                sij=Par(sij)

                if(C[ii,j]== 0.0 and C[ii,j]== 0.0 ):
                     G[ii][j]=Literal(1.0)
                else:
                    G[ii][j]= Exp(-sij*tau[ii][j])                

        S1=0.0
        S2 = [0 for x in range(NC)]
        S3=0.0
        for j in range(NC):
            if(A[j,i] ==0.0 and B[j,i]==0.0):
                continue
            if(C[j,i] ==0.0 and D[j,i]==0.0):
                continue
            if(not(x[j].isFixed==True and x[j].value==0.0)):
                S1+= x[j]*tau[j][i]*G[j][i]
        
        for ii in range(NC):
            S2[ii]=Literal(0.0)
            for k in range(NC):
                if(not(x[k].isFixed==True and x[k].value==0.0)):
                    S2[ii]+= x[k]*G[k][ii]
    
        for j in range(NC):
            S5=Literal(0.0)
            for m in range(NC):
                if(A[m,j] ==0.0 and B[m,j]==0.0):
                    continue
                if(not(x[m].isFixed==True and x[m].value==0.0)):
                    S5+=x[m] *tau[m][j] * G[m][j]
            
            if(x[j].isFixed==True and x[j].value==0.0):
                S3+=0                           
            else:
                S3+=x[j] * G[i][j] / Par(S2[j]) * Par( tau[i][j] - S5 / Par(S2[j]) )

        
        self.gamma=Exp(S1 / S2[i] + S3)
        self.children.append(self.gamma)
        return


    def fullEvaluate(self)->float:
        return self.gamma.eval()


    def diff(self, variable)->float:
        if(variable in self.arguments):            
            return self.gamma.diff(variable)
        else:
            return 0


    def print(self):
        return f"γ[NRTL](T,x)"
    def __str__(self):
        return self.print()
    def __repr__(self):        
        return self.print()         