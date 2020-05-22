from . basic import Expression
import math

class SymSum(Expression):
    
    def __init__(self, arguments):
       super(SymSum,self).__init__()
       for a in arguments:
           self.children.append(a)

    def fullEvaluate(self):
        return sum(c.eval() for c in self.children)

    def diff(self, variable):
        return sum(c.diff(variable) for c in self.children) 
    
    def print(self):
        argList=", ".join( c.print() for c in self.children)
        return f"∑({argList})"

    def __str__(self):
        return self.print()
    def __repr__(self):        
        return self.print()   

class Alias(Expression):
    
    def __init__(self, name,argument):
        super(Alias,self).__init__()
        self.name=name
        self.argument=argument       
        self.children.append(argument)

    def fullEvaluate(self):
        return self.argument.eval()

    def diff(self, variable):
        return self.argument.diff(variable)  
    
    def print(self):        
        return f"{self.name}"

    def __str__(self):
        return self.print()
    def __repr__(self):        
        return self.print()                


