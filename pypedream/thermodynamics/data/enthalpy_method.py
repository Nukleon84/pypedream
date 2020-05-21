from ..factories.variable_factory import VariableFactory
from ..data.substance import Substance
from ...unitsofmeasure.unitset import PhysicalDimension
from ..data.enums import ReferencePhase, ExcessEnthalpyMethod
class PureEnthalpy(object):

    def __init__(self, factory:VariableFactory, substance:Substance):
        self.substance=substance
        self.Tref= factory.createVariable('T','ref','Reference temperature for enthalpy calculation', PhysicalDimension.Temperature)
        self.Href= factory.createVariable('H','ref','Reference enthalpy for enthalpy calculation', PhysicalDimension.SpecificMolarEnthalpy)
        self.Tpc= factory.createVariable('T','pc','Temperature of phase change for enthalpy calculation', PhysicalDimension.Temperature)
        self.freePhaseChange=True
        self.referenceState=ReferencePhase.Vapor
        return

class EnthalpyMethod(object):

    def __init__(self):
        self.name="ENTH01"
        self.pureFunctions=[]
        self.excess= ExcessEnthalpyMethod.Ideal