from ..data.enums import FunctionTypes, Properties
from ..data.pureComponentFunction import PureComponentFunction
from ...expressions import Variable
from ...expressions import Par, Sin, Cos, Tan, Ln, Exp, Sqrt
import math
class PureComponentFunctionFactory(object):
    
    def __createPolynomial(self, func:PureComponentFunction,T:Variable,TC:Variable,PC:Variable):
        
        expr=func.coefficients[0]
        for i in range(1, len(func.coefficients)):
            if(abs(func.coefficients[i])>0):
                expr =expr+ func.coefficients[i] * T ** i
        return expr
     
    def __createAntoine(self, func:PureComponentFunction,T:Variable,TC:Variable,PC:Variable):
        c=func.coefficients
        return c[0]- c[1]/Par(T + c[2])

    
    def __init__(self):
        self.factoryMap={}
        self.factoryMap[FunctionTypes.Antoine]= self.__createAntoine
        self.factoryMap[FunctionTypes.Polynomial]= self.__createPolynomial

   
    def createFunction(self, func:PureComponentFunction,T:Variable,TC:Variable=None,PC:Variable=None):
        return self.factoryMap[func.functionType](func, T, TC, PC)
