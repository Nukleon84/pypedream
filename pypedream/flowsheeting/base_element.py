from ..expressions import Variable
from ..numerics import AlgebraicSystem

class BaseElement(object):

    def __init__(self, name, system):
        self.name=name
        self.system=system
        self.variables={}
        self.parameters={}
        return

    def addVar(self, vari:Variable):
        self.variables[vari.fullName()]=vari
        return
    
    def getVar(self, fullName)->Variable:
        if(fullName in self.variables):
            return self.variables[fullName]
        else:
            raise RuntimeError(f"Element {self.name} does not contain a variable called {fullName}")

    def init(self):
        raise NotImplementedError()

    def instantiate(self, instance:AlgebraicSystem):
        for v in self.variables.values():
            if(not v.isFixed):
                instance.addvar(v)
        return
