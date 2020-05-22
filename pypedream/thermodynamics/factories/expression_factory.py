from ...unitsofmeasure.unitset import UnitSetSI,UnitSetDefault
from ...unitsofmeasure.unitset import PhysicalDimension
from ...expressions import Variable
from .. import PhysicalConstants, Properties, PureComponentFunction

class ExpressionFactory(object):

    def __init__(self,system):
        self.system= system
    
    def EquilibriumCoefficient(self,c, T,P,x,y):
        Keq= self.VaporPressure(c,T)/P
        return Keq

    def VaporPressure(self, comp, T):        
        fdesc=comp.functions[Properties.VaporPressure]        
        f = self.system.correlationFactory.createFunction(fdesc,T)
        return f

