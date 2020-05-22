from . algebraic_system import AlgebraicSystem
import numpy as np
from scipy.sparse.linalg import spsolve as sparseLinearSolve, lgmres
from scipy.sparse import dok_matrix
from numpy.linalg import norm
from .fill_jacobian import fillJacobian


class NewtonSolver(object):
    
    def __init__(self, maxIter=20, tolerance=1e-6, factor=1.0, _callback=None):
        self.maximumIterations=maxIter
        self.tolerance=tolerance
        self.iterCallback= _callback
        self.factor=factor
        return

    def log(self, msg):
        print(msg)
        return
 
    def solve(self, system: AlgebraicSystem):

        if(system.numberOfEquations() != system.numberOfVariables()):
            self.log(f"Number of Equations: {system.numberOfEquations()} Number of Variables: {system.numberOfVariables()}")
            raise RuntimeError("Can only solve square systems")

        system.createIndex()
        system.createSparsityPattern()
        delta = np.zeros(system.numberOfVariables())
        b = np.zeros(system.numberOfEquations())
        n =1e12
        e= 1e12
        if(self.iterCallback):
            self.iterCallback(-1,n,e )

        labels=["Iter","Norm","Residual","Flags","Comment"]
        comment=''
        print(f"{labels[0]:<4} {'': <10s} {labels[1]:<12} {'': <10s} {labels[2]:<12} {'': <10s} {labels[3]:<6} {'': <10s} {labels[4]:<12}")
        for i in range(self.maximumIterations):
            A,b= fillJacobian(system,b)
            delta= sparseLinearSolve(A,-b)
            comment=''
            n=norm(delta)
            e=np.amax(b)
            flags=["-","-","-","-"]
            
            if(np.isnan(n)):                
                delta,_= lgmres(A,-b)                
                flags[0]='I'
                comment='Singular Matrix. Trying lgmres'
                n=norm(delta)

            for index,variable in enumerate(system.variables):
                variable.addDelta(self.factor*delta[index])
            
            self.log(f"{i:4} {'': <10s} {('{0:2E}'.format(n)):>12} {'': <10s} {('{0:2E}'.format(e)):>12} {'': <10s} {''.join(flags):<6} {'': <10s} {comment}")    

            if(self.iterCallback):
                self.iterCallback(i,n,e )

            if(norm(delta)<self.tolerance):
                if(e<self.tolerance):
                    self.log("Solve succeeded.")
                else:
                    self.log("Norm is less than tolerance but residuals are not converged.")
                return True            

        self.log("Maximum number of iterations exceeded!")
        return False
