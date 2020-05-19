from .enums import FunctionTypes, Properties
from ...unitsofmeasure import Unit

class PureComponentFunction(object):

    def __init__(self,property:Properties, functionType:FunctionTypes, tmin:float, tmax:float, coefficients, xUnit:Unit, yUnit:Unit, referenceX=0):
        self.functionType=functionType
        self.property=property
        self.tmin=tmin
        self.tmax=tmax
        self.coefficients=coefficients
        self.xUnit=xUnit
        self.yUnit=yUnit
        self.referenceX=referenceX