from scipy.sparse import dok_matrix
from .algebraic_system import AlgebraicSystem
import numpy as np
from numpy import ndarray

def fillJacobian(system:AlgebraicSystem,b:ndarray):
    for i, eq in enumerate(system.equations):
        eq.reset()
        b[i]=eq.residual()

    A = dok_matrix((system.numberOfEquations(),system.numberOfVariables()), dtype=float)
    for incidence in system.sparsityPattern:
        i=incidence["EquationIndex"]
        j=incidence["VariableIndex"]   
        eq=  system.equations[i].rhs   
        var=system.variables[j]
        der= eq.diff(var)
        A[i,j]=der
    return (A.tocsc(),b)