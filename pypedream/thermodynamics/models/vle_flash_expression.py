from ...expressions import Expression, SymSum
from ...thermodynamics import PhaseState
class VLEFlashExpression(Expression):

    def __init__(self, stream):
        super(VLEFlashExpression,self).__init__()
        self.checkFrequency=3
        self.iterationsUntilNextCheck=0
        self.stream=stream
        self.LV= SymSum(stream.x)-SymSum(stream.y)
        self.L= SymSum(stream.x)-1
        self.V= SymSum(stream.y)-1
        self.children.extend([self.LV, self.V, self.L])
        return
    
    def fullEvaluate(self):
        
        self.iterationsUntilNextCheck-=1

        if(self.iterationsUntilNextCheck<=0):
            self.stream.updatePhaseState()
            self.iterationsUntilNextCheck= self.checkFrequency

        if(self.stream.state==PhaseState.LiquidVapor
            or self.stream.state==PhaseState.BubblePoint
            or self.stream.state==PhaseState.DewPoint ):
            return self.LV.eval()
        if(self.stream.state==PhaseState.Liquid):
            return self.L.eval()            
        if(self.stream.state==PhaseState.Vapor):
            return self.V.eval()       
        

    def diff(self, variable):
        if(self.stream.state==PhaseState.LiquidVapor
            or self.stream.state==PhaseState.BubblePoint
            or self.stream.state==PhaseState.DewPoint ):
            return self.LV.diff(variable)
        if(self.stream.state==PhaseState.Liquid):
            return self.L.diff(variable)           
        if(self.stream.state==PhaseState.Vapor):
            return self.V.diff(variable)  