from . basic import Expression
class Variable(Expression):   
    name="undefined"
    
    def __init__(self, name, value):
        self.name=name
        self.value=value

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