from . basic import UnaryExpression
import math

class Sin(UnaryExpression):
    
    def __init__(self, argument):
       super(Sin,self).__init__('sin',argument)

    def fullEvaluate(self)->float:
        return math.sin(self.argument.eval())

    def diff(self, variable)->float:
        return self.argument.diff(variable)*math.cos(self.argument.eval()) 

class Cos(UnaryExpression):
    
    def __init__(self, argument):
       super(Cos,self).__init__('cos',argument)

    def fullEvaluate(self)->float:
        return math.cos(self.argument.eval())

    def diff(self, variable)->float:
        return -(self.argument.diff(variable)*math.sin(self.argument.eval()))     

class Sinh(UnaryExpression):
    
    def __init__(self, argument):
       super(Sinh,self).__init__('sinh',argument)

    def fullEvaluate(self)->float:
        return math.sinh(self.argument.eval())

    def diff(self, variable)->float:
        return self.argument.diff(variable)*math.cosh(self.argument.eval()) 

class Cosh(UnaryExpression):
    
    def __init__(self, argument):
       super(Cosh,self).__init__('cosh',argument)

    def fullEvaluate(self)->float:
        return math.cosh(self.argument.eval())

    def diff(self, variable)->float:
        return -(self.argument.diff(variable)*math.sinh(self.argument.eval()))         

class Tan(UnaryExpression):
    
    def __init__(self, argument):
       super(Tan,self).__init__('tan',argument)

    def fullEvaluate(self)->float:
        return math.tan(self.argument.eval())

    def diff(self, variable)->float:
        return self.argument.diff(variable)*math.tan(self.argument.eval())          


def calculateCoth(x:float)->float:
    return (math.exp(x) + math.exp(-x)) / (math.exp(x) - math.exp(-x))

def calculateCosech(x:float)->float:
    return 2 / (math.exp(x) - math.exp(-x))

def calculateSech(x:float)->float:
    return 2 / (math.exp(x) + math.exp(-x))

class Coth(UnaryExpression):
        
    def __init__(self, argument):
       super(Coth,self).__init__('coth',argument)

    def fullEvaluate(self)->float:
        return calculateCoth(self.argument.eval())

    def diff(self, variable)->float:
        return -((calculateCosech(self.argument.eval()))**2 * self.argument.diff(variable))        

class Tanh(UnaryExpression):
        
    def __init__(self, argument):
       super(Tanh,self).__init__('tanh',argument)

    def fullEvaluate(self)->float:
        return math.tanh(self.argument.eval())

    def diff(self, variable)->float:
        return (calculateSech(self.argument.eval()))**2 * self.argument.diff(variable)        




