from . basic import Expression,Variable


class Equation(object):
    def __init__(self, rhs, name=""):
        self.name=name
        self.rhs=rhs
        self.variables=[]
        self.exploreVariables(rhs)
        return
    
    def exploreVariables(self, expr):
        if(isinstance(expr,Variable)):
            if expr not in self.variables:
                self.variables.append(expr)
        else:
            for child in expr.children:
                self.exploreVariables(child)
        return
   
    def residual(self):        
        return self.rhs.eval()
    
    def reset(self):
        return self.rhs.reset()