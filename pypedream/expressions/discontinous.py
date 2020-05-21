from . basic import BinaryFunction

class Min(BinaryFunction):

    def __init__(self, left,right):
       super(Min,self).__init__('min',left,right)

    def fullEvaluate(self)->float:
        return min(self.left.eval(),self.right.eval())
    
    def diff(self, variable)->float:
        return self.left.diff(variable)+self.right.diff(variable)

class Max(BinaryFunction):

    def __init__(self, left,right):
       super(Max,self).__init__('max',left,right)

    def fullEvaluate(self)->float:
        return max(self.left.eval(),self.right.eval())
    
    def diff(self, variable)->float:
        return self.left.diff(variable)+self.right.diff(variable)

