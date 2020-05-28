from ...unitsofmeasure.unitset import UnitSetSI,UnitSetDefault
from ...unitsofmeasure.unitset import PhysicalDimension
from ...expressions import Variable
from .. import PhysicalConstants, Properties, PureComponentFunction
from ..data.enums import ActivityMethod
from ..models import GammaNRTL

class ExpressionFactory(object):

    def __init__(self,system):
        self.system= system
    
    def EquilibriumCoefficient(self,c, T,P,x,y):
        if(self.system.equilibrium.activityMethod== ActivityMethod.NRTL):
            return GammaNRTL(self.system, T,x,c)*self.VaporPressure(c,T)/P

        #Default= Ideal        
        return self.VaporPressure(c,T)/P

    def VaporPressure(self, comp, T):        
        fdesc=comp.functions[Properties.VaporPressure]        
        f = self.system.correlationFactory.createFunction(fdesc,T)
        return f

