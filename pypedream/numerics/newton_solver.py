from . algebraic_system import AlgebraicSystem
import numpy as np
from scipy.sparse.linalg import spsolve as sparseLinearSolve
from scipy.sparse import dok_matrix
from numpy.linalg import norm
class NewtonSolver(object):
    
    def __init__(self, maxIter=20, tolerance=1e-6, factor=1.0, _callback=None):
        self.maximumIterations=maxIter
        self.tolerance=tolerance
        self.iterCallback= _callback
        self.factor=factor
        return

    def fillJacobian(self, system,b):
        for eq in system.equations:
            eq.reset()

        A = dok_matrix((system.numberOfEquations(),system.numberOfVariables()), dtype=float)
        for incidence in system.sparsityPattern:
            i=incidence["EquationIndex"]
            j=incidence["VariableIndex"]
            b[i]=system.equations[i].residual()
            der= system.equations[i].rhs.diff(system.variables[j])
            A[i,j]=der
        return (A.tocsc(),b)

    def solve(self, system: AlgebraicSystem):

        if(system.numberOfEquations() != system.numberOfVariables()):
            raise RuntimeError("Can only solve square systems")

        system.createIndex()
        system.createSparsityPattern()
        delta = np.zeros(system.numberOfVariables())
        b = np.zeros(system.numberOfEquations())
        n =1e12
        e= 1e12
        if(self.iterCallback):
            self.iterCallback(-1,n,e )

        for i in range(self.maximumIterations):
            A,b= self.fillJacobian(system,b)
            delta= sparseLinearSolve(A,-b)

            for index,variable in enumerate(system.variables):
                variable.value+= self.factor*delta[index]

            n=norm(delta)
            e=np.amax(b)
            print(f"Iter: {i} Norm: {n} Err:{e}")
            if(self.iterCallback):
                self.iterCallback(i,n,e )

            if(norm(delta)<self.tolerance):
                print("Solve succeeded.")
                return True
            

        print("Maximum number of iterations exceeded!")
        return False
