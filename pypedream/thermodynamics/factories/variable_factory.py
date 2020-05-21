from ...unitsofmeasure.unitset import UnitSetSI,UnitSetDefault
from ...unitsofmeasure.unitset import PhysicalDimension
from ...expressions import Variable
class VariableFactory(object):
    def __init__(self):
        self.internalSet= UnitSetSI()
        self.inputSet=UnitSetDefault()
        self.outputSet=UnitSetDefault()
        self.tmin=1
        self.tmax=1000
        self.pmin=100
        self.pmax=1e9
        return

    def setTemperatureLimits(self, tmin:float,tmax:float):
        self.tmin=tmin
        self.tmax=tmax
        return
    def setPressureLimits(self, pmin:float,pmax:float):
        self.pmin=pmin
        self.pmax=pmax
        return

    def createVariable(self, name, subscript,description, dimension:PhysicalDimension ):
        vari = Variable(name,0,self.internalSet[dimension])
        vari.displayUnit=self.outputSet[dimension]
        vari.dimension=dimension        
        vari.subscript=subscript

        if(dimension== PhysicalDimension.Temperature):
            vari.value=273.15
            vari.lowerBound= self.tmin
            vari.upperBound=self.tmax
        
        if(dimension== PhysicalDimension.Pressure):
            vari.value=1e5
            vari.lowerBound= self.pmin
            vari.upperBound=self.pmax
        
        if( dimension==PhysicalDimension.MassDensity or
            dimension==PhysicalDimension.MolarDensity or
            dimension==PhysicalDimension.MassFlow or
            dimension==PhysicalDimension.MolarFlow or
            dimension==PhysicalDimension.VolumeFlow or
            dimension==PhysicalDimension.MolarVolume 
            ):
            vari.lowerBound=0

        if(dimension== PhysicalDimension.MolarFraction or dimension== PhysicalDimension.MassFraction):            
            vari.lowerBound= 0
            vari.upperBound=1
                 
            

        return vari

