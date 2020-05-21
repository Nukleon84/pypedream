from ..data.enums import FunctionTypes, Properties
from ..data.pureComponentFunction import PureComponentFunction
from ...expressions import Variable
from ...expressions import Par, Sin, Cos, Tan, Ln, Exp, Sqrt, Sinh ,Cosh, Coth, Tanh
import math

class PureComponentFunctionFactory(object):
    
    def __createPolynomial(self, func:PureComponentFunction,T:Variable,TC:Variable,PC:Variable):
        c=self.__ensure(func.coefficients,1)
        expr=c[0]
        for i in range(1, len(c)):
            if(abs(c[i])>0):
                expr =expr+ c[i] * T ** i
        return expr
    
    def __createPolynomialIntegrated(self, func:PureComponentFunction,T:Variable,TC:Variable,PC:Variable):
        c=self.__ensure(func.coefficients,1)
        expr=c[0]*T
        for i in range(1, len(c)):
            if(abs(c[i])>0):
                expr =expr+ 1/(i+1)*c[i] * T ** (i+1)
        return expr        
     
    def __createAntoine(self, func:PureComponentFunction,T:Variable,TC:Variable,PC:Variable):
        c=self.__ensure(func.coefficients,3)
        return Exp(c[0]- c[1]/Par(T + c[2]))

    def __createExtendedAntoine(self, func:PureComponentFunction,T:Variable,TC:Variable,PC:Variable):
        c=self.__ensure(func.coefficients,7)
        return Exp(c[0] + c[1]/Par(T + c[2]) + c[3]*T + c[4]*Ln(T) +c[5]*T**c[6] )

    def __createWagner(self, func:PureComponentFunction,T:Variable,TC:Variable,PC:Variable):
        c=self.__ensure(func.coefficients,7)
        TR= T/TC
        tau=Par(1-TR)
        return Exp(Ln(PC) + 1/TR *Par(c[2]*tau + c[3]*tau**1.5 + c[4]*tau**3 + c[5]*tau**6) )

    def __createDIPPR106(self, func:PureComponentFunction,T:Variable,TC:Variable,PC:Variable):
        c=self.__ensure(func.coefficients,6)
        TR=T/c[0]
        h= Par(c[2] +c[3]*TR + c[4]*TR**2 + c[5]*TR**3)
        return c[1] * Par(1-TR)**h
    
    def __createAlyLee(self, func:PureComponentFunction,T:Variable,TC:Variable,PC:Variable):
        c=self.__ensure(func.coefficients,5)       
        return c[0] + c[1] * Par(c[2]/T/Sinh(c[2]/T))**2 + c[3]*Par(c[4]*T / Cosh(c[4]/T))**2
    
    def __createDIPPR117(self, func:PureComponentFunction,T:Variable,TC:Variable,PC:Variable):
        c=self.__ensure(func.coefficients,5)       
        return c[0]*T + c[1]*c[2] * Coth(c[2]/T) - c[3]*c[4]*Tanh(c[4]/T)

    def __createRacket(self, func:PureComponentFunction,T:Variable,TC:Variable,PC:Variable):
        c=self.__ensure(func.coefficients,4)       
        TR=T/c[2]
        return c[0] / Par( c[1]**Par(1+Par(1-TR)**c[3]) )

    def __createWatson(self, func:PureComponentFunction,T:Variable,TC:Variable,PC:Variable):
        c=self.__ensure(func.coefficients,4)       
        return c[0] * Par(c[2]-T)**c[1]+c[3]
    
    def __createDIPPR102(self, func:PureComponentFunction,T:Variable,TC:Variable,PC:Variable):
        c=self.__ensure(func.coefficients,4)       
        return c[0] * T**c[1]/Par(1+c[2]/T +c[3]/T)

    def __createKirchhoff(self, func:PureComponentFunction,T:Variable,TC:Variable,PC:Variable):
        c=self.__ensure(func.coefficients,2)       
        return Exp(c[0] - c[1]/T +c[2]*Ln(T) )

    def __createExtendedKirchhoff(self, func:PureComponentFunction,T:Variable,TC:Variable,PC:Variable):
        c=self.__ensure(func.coefficients,5)       
        return Exp(c[0] + c[1]/T +c[2]*Ln(T) +c[3]*T**c[4])

    def __createSutherland(self, func:PureComponentFunction,T:Variable,TC:Variable,PC:Variable):
        c=self.__ensure(func.coefficients,2)       
        return c[0]*Sqrt(T)/(1 + c[1]/T)
  
    def __createChemSep16(self, func:PureComponentFunction,T:Variable,TC:Variable,PC:Variable):
        c=self.__ensure(func.coefficients,5)       
        return c[0] + Exp(c[1]/T) + c[2] + c[3]*T + c[4]*T**2
    
    def __createChemSep101(self, func:PureComponentFunction,T:Variable,TC:Variable,PC:Variable):
        c=self.__ensure(func.coefficients,5)       
        return Exp(c[0] + c[1]/T +c[2]*Ln(T) +c[3]*T**2)
     
    def __createChemSep102(self, func:PureComponentFunction,T:Variable,TC:Variable,PC:Variable):
        c=self.__ensure(func.coefficients,5)       
        return c[0]*T**c[1]/Par(1 +c[2]/T +c[3]/T**2)

    def __createChemSep106(self, func:PureComponentFunction,T:Variable,TC:Variable,PC:Variable):
        c=self.__ensure(func.coefficients,6)       
        TR=T/TC
        h= c[1] +c[2]*TR+ c[3] *TR**2+c[4]*TR**3
        return c[0]*Par(1-TR)**h


    def __ensure(self, coeffs, minCoeff):
        c=coeffs        
        if(len(c)<minCoeff):
            for _ in range(minCoeff-len(c)):
                c.append(0)
        return c

    def __init__(self):
        self.factoryMap={}
        self.factoryMap[FunctionTypes.Antoine]= self.__createAntoine
        self.factoryMap[FunctionTypes.ExtendedAntoine]= self.__createExtendedAntoine
        self.factoryMap[FunctionTypes.Polynomial]= self.__createPolynomial
        self.factoryMap[FunctionTypes.Chemsep101]= self.__createChemSep101
        self.factoryMap[FunctionTypes.Chemsep102]= self.__createChemSep102
        self.factoryMap[FunctionTypes.Chemsep106]= self.__createChemSep106
        self.factoryMap[FunctionTypes.Chemsep16]= self.__createChemSep16
        self.factoryMap[FunctionTypes.Kirchhoff]= self.__createKirchhoff
        self.factoryMap[FunctionTypes.ExtendedKirchhoff]= self.__createExtendedKirchhoff        
        self.factoryMap[FunctionTypes.Wagner]= self.__createWagner
        self.factoryMap[FunctionTypes.Watson]= self.__createWatson
        self.factoryMap[FunctionTypes.AlyLee]= self.__createAlyLee
        self.factoryMap[FunctionTypes.Sutherland]= self.__createSutherland
        self.factoryMap[FunctionTypes.Rackett]= self.__createRacket
        self.factoryMap[FunctionTypes.Dippr102]= self.__createDIPPR102
        self.factoryMap[FunctionTypes.Dippr106]= self.__createDIPPR106
        self.factoryMap[FunctionTypes.Dippr117]= self.__createDIPPR117
   
    def createFunction(self, func:PureComponentFunction,T:Variable,TC:Variable=None,PC:Variable=None):
        return self.factoryMap[func.functionType](func, T, TC, PC)
