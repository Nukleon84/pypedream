from ..expressions import Equation,Variable

class AlgebraicSystem(object):

    def __init__(self, name=""):
        self.name=name
        self.variables=[]
        self.equations=[]
        self.sparsityPattern=[]
        self.variableIndex={}
    
    def addvar(self, var):
        self.variables.append(var)
        return var
    
    def makevar(self, name, value):
        var= Variable(name,value)
        self.variables.append(var)
        return var
    

    def eq(self, rhs, name=""):
        if(name==""):
            name=f"EQ{len(self.equations)}"
        equation=Equation(rhs,name)
        self.equations.append(equation)
        return equation

    def numberOfVariables(self):
        return len(self.variables)

    def numberOfEquations(self):
        return len(self.equations)

    def numberOfNonZeros(self):
        return len(self.sparsityPattern)
    
    def createIndex(self):
        self.variableIndex={}
        for i, v in enumerate(self.variables, start=0):
            self.variableIndex[v]=i
    
    def createSparsityPattern(self):
        self.sparsityPattern=[]
        for i, eq in enumerate(self.equations, start=0):
            for var in eq.variables:
                if(var in self.variableIndex.keys()):
                    j= self.variableIndex[var]
                    self.sparsityPattern.append({'EquationIndex':i,'VariableIndex':j,'Value':1.0})

