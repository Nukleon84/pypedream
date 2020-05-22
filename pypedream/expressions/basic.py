import math
from typing import List
from ..unitsofmeasure import Unit,SI, PhysicalDimension

class Expression(object):
    
    def __init__(self):
        self.value= float
        self.value = 0
        self.children= List[Expression]
        self.children=[]
        self.needsEval=True

    def eval(self) -> float:
        if(self.needsEval):            
            self.value=self.fullEvaluate()
            self.needsEval=False
        return self.value

    def fullEvaluate(self)->float:
        raise NotImplementedError

    def diff(self, variable)->float:
        return 0

    def reset(self):
        self.needsEval=True
        for c in self.children:
            c.reset()
            
    def print(self):
         raise NotImplementedError

    def __add__(self, other): 
        if(isinstance(other, int) or isinstance(other, float)):
            other=Literal(other)
        return Addition(self, other)  
    def __sub__(self, other):
        if(isinstance(other, int) or isinstance(other, float)):
            other=Literal(other) 
        return Subtraction(self, other)     
    def __mul__(self, other): 
        if(isinstance(other, int) or isinstance(other, float)):
            other=Literal(other)
        return Multiplication(self, other)         
    def __truediv__(self, other):
        if(isinstance(other, int) or isinstance(other, float)):
            other=Literal(other) 
        return Division(self, other) 
    def __pow__(self, other):
        if(isinstance(other, int) or isinstance(other, float)):
            other=Literal(other) 
        return Power(self, other) 

    def __rmul__(self,other):
        if(isinstance(other, int) or isinstance(other, float)):
            other=Literal(other)
        return Multiplication(other, self)      

    def __radd__(self,other):
        if(isinstance(other, int) or isinstance(other, float)):
            other=Literal(other)
        return Addition(other, self)  
 
    def __rsub__(self,other):
        if(isinstance(other, int) or isinstance(other, float)):
            other=Literal(other) 
        return Subtraction(other, self)      

    def __rtruediv__(self,other):
        if(isinstance(other, int) or isinstance(other, float)):
            other=Literal(other) 
        return Division(other, self)                 

    def __rpow__(self, other):
        if(isinstance(other, int) or isinstance(other, float)):
            other=Literal(other) 
        return Power(other, self) 
    
    def __neg__(self):
        return Negate(self)

    def __str__(self):
        return self.print()
    def __repr__(self):        
        return self.print()

class Literal(Expression):
    def __init__(self, value):
        self.value = value
        self.children=[]
    def print(self):
        return str(self.value)
    def reset(self):
        return

    def eval(self)->float:        
        return self.value

    def fullEvaluate(self)->float:
        return self.value

    def __str__(self):
        return self.print()
    def __repr__(self):        
        return self.print()


class UnaryExpression(Expression):
    
    def __init__(self, symbol, argument):
        super(UnaryExpression,self).__init__()
        self.children.append(argument)        
        self.argument=argument        
        self.symbol=symbol
    def print(self):
        return f"{self.symbol}({self.argument.print()})"
    def __str__(self):
        return self.print()
    def __repr__(self):        
        return self.print()        

class BinaryExpression(Expression):
    
    def __init__(self, symbol, left,right):
        super(BinaryExpression,self).__init__()
        if(isinstance(left, int) or isinstance(left, float)):
            left=Literal(left) 
        if(isinstance(right, int) or isinstance(right, float)):
            left=Literal(right) 
    
        self.children.append(left)
        self.children.append(right)
        self.left=left
        self.right=right
        self.symbol=symbol
    def print(self):
        return f"{self.left.print()} {self.symbol} {self.right.print()}"
    def __str__(self):
        return self.print()
    def __repr__(self):        
        return self.print()        

class BinaryFunction(BinaryExpression):
    
    def __init__(self, symbol, left,right):
        super(BinaryFunction,self).__init__(symbol, left, right)        
    def print(self):
        return f"{self.symbol}({self.left.print()}, {self.right.print()})"
    def __str__(self):
        return self.print()
    def __repr__(self):        
        return self.print()


class Addition(BinaryExpression):
    
    def __init__(self, left,right):
       super(Addition,self).__init__('+',left,right)

    def fullEvaluate(self)->float:
        return self.left.eval()+self.right.eval()

    def diff(self, variable)->float:
        return self.left.diff(variable)+self.right.diff(variable)
    def __str__(self):
        return self.print()
    def __repr__(self):        
        return self.print()        

class Subtraction(BinaryExpression):

    def __init__(self, left,right):
       super(Subtraction,self).__init__('-',left,right)

    def fullEvaluate(self)->float:
        return (self.left.eval())- (self.right.eval())   
    
    def diff(self, variable)->float:
        return (self.left.diff(variable))-(self.right.diff(variable))    
    def __str__(self):
        return self.print()
    def __repr__(self):        
        return self.print()

class Multiplication(BinaryExpression):

    def __init__(self, left,right):
       super(Multiplication,self).__init__('×',left,right)

    def fullEvaluate(self)->float:
        return self.left.eval()*self.right.eval()   
    
    def diff(self, variable)->float:
        return self.left.diff(variable)*self.right.eval()+self.left.eval()*self.right.diff(variable)
    def __str__(self):
        return self.print()
    def __repr__(self):        
        return self.print()        

class Division(BinaryExpression):

    def __init__(self, left,right):
       super(Division,self).__init__('/',left,right)

    def fullEvaluate(self)->float:
        return self.left.eval()/self.right.eval()     
    
    def diff(self, variable)->float:
        return (self.left.diff(variable)*self.right.eval()-self.left.eval()*self.right.diff(variable))/ (self.right.eval()**2)
    def __str__(self):
        return self.print()
    def __repr__(self):        
        return self.print()        

      
class Power(BinaryExpression):

    def __init__(self, left,right):
       super(Power,self).__init__('^',left,right)

    def fullEvaluate(self)->float:        
        return self.left.eval()**self.right.eval()  
    
    def diff(self, variable)->float:
        return (self.right.eval()*(self.left.eval()**(self.right.eval()-1))*self.left.diff(variable)
            +(self.left.eval()**self.right.eval())*math.log(self.right.eval())*self.right.diff(variable))
    def __str__(self):
        return self.print()
    def __repr__(self):        
        return self.print()            

class Negate(UnaryExpression):
    
    def __init__(self, argument):
       super(Negate,self).__init__('-',argument)

    def fullEvaluate(self)->float:
        return -self.argument.eval()

    def diff(self, variable)->float:
        return -(self.argument.diff(variable)) 
    def __str__(self):
        return self.print()
    def __repr__(self):        
        return self.print()        




class Variable(Expression):       
    
    def __init__(self, name, value, unit=SI.none):
        super(Variable,self).__init__()
        self.name=name
        self.value=value
        self.internalUnit=unit
        self.displayUnit=unit
        self.isConstant=False
        self.dimension=None
        self.subscript=""
        self.lowerBound=-1e20
        self.upperBound=1e20
        self.isFixed=False
        return
        

    def __str__(self):
        return self.print()

    def fullName(self):
        if(self.subscript != ""):
            return f"{self.name}[{self.subscript}]" 
        else:
            return self.name

    def displayValue(self):
        return Unit.convert(self.internalUnit, self.displayUnit, self.value)

    def setValue(self,value, unit=None):
        if(unit==None):
            unit=self.displayUnit
        self.value= Unit.convert(unit, self.internalUnit, value)
        return

    def fixValue(self,value, unit=None):
        if(unit==None):
            unit=self.displayUnit
        self.value= Unit.convert(unit, self.internalUnit, value)
        self.isFixed=True
        return
    
    def unfix(self):
        self.isFixed=False
        return

    def quantity(self):
        return (self.displayValue(), self.displayUnit)

    def eval(self)->float:      
        return self.value

    def fullEvaluate(self)->float:
        return self.value

    def diff(self, variable)->float:
        return 1.0 if variable==self else 0.0

    def addDelta(self, delta):
        if(self.dimension== PhysicalDimension.Temperature):
            delta=max(-35, min(35, delta))

        self.value+= delta
        self.value=max(self.lowerBound, min(self.upperBound, self.value))
        return
        
    def reset(self):
        return
        
    def print(self):
        return self.fullName()  
