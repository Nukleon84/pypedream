from scipy.sparse import dok_matrix
from .algebraic_system import AlgebraicSystem
import numpy as np
from numpy import ndarray

def fillJacobian(system:AlgebraicSystem,b:ndarray):
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