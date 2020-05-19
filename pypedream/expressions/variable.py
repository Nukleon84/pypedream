from . basic import Expression
from ..unitsofmeasure import Unit,SI


class Variable(Expression):       
    
    def __init__(self, name, value, unit=SI.none):
        super(Variable,self).__init__()
        self.name=name
        self.value=value
        self.internalUnit=unit
        self.displayUnit=unit
        self.isConstant=False
        

    def __str__(self):
        return self.print()

    def displayValue(self):
        return Unit.convert(self.internalUnit, self.displayUnit, self.value)

    def setValue(self,value):
        self.value= Unit.convert(self.displayUnit, self.internalUnit, value)

    def quantity(self):
        return (self.displayValue(), self.displayUnit)

    def eval(self):      
        return self.value

    def fullEvaluate(self):
        return self.value

    def diff(self, variable):
        return 1.0 if variable==self else 0.0

    def reset(self):
        return
        
    def print(self):
        return f"{self.name}"  

