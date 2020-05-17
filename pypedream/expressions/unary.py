from . basic import UnaryExpression
import math

class Exp(UnaryExpression):
    
    def __init__(self, argument):
       super(Exp,self).__init__('exp',argument)

    def fullEvaluate(self):
        return math.exp(self.argument.eval())

    def diff(self, variable):
        return self.argument.diff(variable)*self.eval() 

class Ln(UnaryExpression):
    
    def __init__(self, argument):
       super(Ln,self).__init__('ln',argument)

    def fullEvaluate(self):
        return math.log(self.argument.eval())

    def diff(self, variable):
        return 1/self.argument.eval()*self.argument.diff(variable)



class Sqrt(UnaryExpression):
    
    def __init__(self, argument):
       super(Sqrt,self).__init__('sqrt',argument)

    def fullEvaluate(self):
        return math.sqrt(self.argument.eval())

    def diff(self, variable):
        return 1.0/(2.0*self.argument.eval())*self.argument.diff(variable)        

class Par(UnaryExpression):
    
    def __init__(self, argument):
       super(Par,self).__init__('',argument)

    def fullEvaluate(self):
        return self.argument.eval()

    def diff(self, variable):
        return self.argument.diff(variable)       

    