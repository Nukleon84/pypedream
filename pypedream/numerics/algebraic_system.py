class AlgebraicSystem(object):

    def __init__(self, name=""):
        self.name=name
        self.variables=[]
        self.equations=[]
        self.sparsityPattern=[]
        self.variableIndex={}
    
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

