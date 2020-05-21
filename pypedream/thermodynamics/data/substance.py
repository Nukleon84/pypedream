from ...expressions.variable import Variable
from ...unitsofmeasure import Unit, SI, METRIC
from .enums import FunctionTypes, PhysicalConstants, Properties
from .pureComponentFunction import PureComponentFunction


class Substance(object):

    def __init__(self, name, id, molarWeight):
        self.name=name
        self.id=id
        self.casno='123-45-6'
        self.structure=''
        self.isInert=False
        self.isSolid=False
        self.molarWeight= Variable(PhysicalConstants.MolarWeight.name, molarWeight, SI.kg/SI.kmol)
        self.molarWeight.isConstant=True
        self.constants={}
        self.functions={}
        self.constants[PhysicalConstants.MolarWeight]=self.molarWeight
        return    

    def renameId(self,newID):
        self.id=newID
        return self

    def addFunction(self, prop:Properties, functionType:FunctionTypes, tmin:float, tmax:float, coefficients,  xUnit:Unit, yUnit:Unit, referenceX=0):
        self.functions[prop]=PureComponentFunction(prop, functionType, tmin, tmax, coefficients, xUnit, yUnit, referenceX)
        return self
    
    def addConstant(self, const:PhysicalConstants, value, unit=SI.none):
        variable= Variable(const.name, value, unit)
        variable.isConstant=True
        self.constants[const]=variable
        return self 