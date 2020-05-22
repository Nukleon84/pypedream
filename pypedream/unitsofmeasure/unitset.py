from enum import Enum,auto
from . SI import SI
from . METRIC import METRIC

class PhysicalDimension(Enum):
    Temperature = auto()
    TemperatureDifference = auto()
    Pressure = auto()
    MolarFlow = auto()
    MassFlow = auto()
    VolumeFlow=auto()
    MolarDensity=auto()
    MassDensity=auto()
    HeatFlow=auto()
    Energy=auto()
    Power=auto()
    Work=auto()
    Currency=auto()
    Length=auto()
    Area=auto()
    Volume=auto()
    Time=auto()
    Mass=auto()
    Mole=auto()
    Enthalpy=auto()
    HeatCapacity=auto()
    MolarVolume=auto()
    Dimensionless=auto()
    SpecificMolarEnthalpy=auto()
    SpecificMassEnthalpy=auto()
    HeatTransferCoefficient=auto()
    SurfaceTension=auto()
    HeatConductivity=auto()
    DiffusionCoefficient=auto()
    MolarFraction=auto()
    MassFraction=auto()
    SpecificArea=auto()
    MassTransferCoefficient=auto()
    DynamicViscosity=auto()
    Velocity=auto()
    MolarWeight=auto()

class UnitSet(object):
    def __init__(self, name, description):
        self.name=name
        self.description=description
        self.mapping={}
    def __getitem__(self, key):
        return self.mapping[key]        
    def __setitem__(self, key,value):
        self.mapping[key] =value

class UnitSetSI(UnitSet):
    def __init__(self):
        super(UnitSetSI,self).__init__("SI", "Unit set according to the SI")       
        self.mapping[PhysicalDimension.Dimensionless]=SI.none
        self.mapping[PhysicalDimension.Temperature]=SI.K
        self.mapping[PhysicalDimension.Pressure]=SI.Pa

        self.mapping[PhysicalDimension.Mass]=SI.kg
        self.mapping[PhysicalDimension.Mole]=SI.mol

        self.mapping[PhysicalDimension.Length]=SI.m
        self.mapping[PhysicalDimension.Area]=SI.sqm
        self.mapping[PhysicalDimension.Volume]=SI.cum

        self.mapping[PhysicalDimension.MassFlow]=SI.kg/SI.s
        self.mapping[PhysicalDimension.MolarFlow]=SI.mol/SI.s
        self.mapping[PhysicalDimension.HeatFlow]=SI.J/SI.s
        self.mapping[PhysicalDimension.Enthalpy]=SI.J/SI.s
        self.mapping[PhysicalDimension.VolumeFlow]=SI.cum/SI.s

        self.mapping[PhysicalDimension.MolarWeight]=SI.kg/SI.mol

        self.mapping[PhysicalDimension.MolarVolume]=SI.cum/SI.mol
        self.mapping[PhysicalDimension.MassDensity]=SI.kg/SI.cum
        self.mapping[PhysicalDimension.MolarDensity]=SI.mol/SI.cum

        self.mapping[PhysicalDimension.SpecificMolarEnthalpy]=SI.J/SI.mol
        self.mapping[PhysicalDimension.SpecificMassEnthalpy]=SI.J/SI.kg
        self.mapping[PhysicalDimension.HeatCapacity]=SI.J/SI.mol/SI.K

        self.mapping[PhysicalDimension.HeatTransferCoefficient]=SI.W / SI.sqm / SI.K
        self.mapping[PhysicalDimension.MassTransferCoefficient]= SI.m / SI.s

        self.mapping[PhysicalDimension.MolarFraction]= SI.mol / SI.mol
        self.mapping[PhysicalDimension.MassFraction]= SI.kg / SI.kg
        self.mapping[PhysicalDimension.SpecificArea]= SI.sqm / SI.cum

        self.mapping[PhysicalDimension.DynamicViscosity]= SI.Pa / SI.s
        self.mapping[PhysicalDimension.Velocity]= SI.m / SI.s

class UnitSetDefault(UnitSet):
    def __init__(self):
        super(UnitSetDefault,self).__init__("Default", "Default unit set according to the common European engineering practice")
        self.mapping[PhysicalDimension.Dimensionless]=SI.none
        self.mapping[PhysicalDimension.Temperature]=METRIC.C
        self.mapping[PhysicalDimension.Pressure]=METRIC.mbar

        self.mapping[PhysicalDimension.Mass]=SI.kg
        self.mapping[PhysicalDimension.Mole]=SI.mol

        self.mapping[PhysicalDimension.Length]=SI.m
        self.mapping[PhysicalDimension.Area]=SI.sqm
        self.mapping[PhysicalDimension.Volume]=SI.cum

        self.mapping[PhysicalDimension.MassFlow]=SI.kg/SI.h
        self.mapping[PhysicalDimension.MolarFlow]=SI.kmol/SI.h
        self.mapping[PhysicalDimension.HeatFlow]=SI.kW
        self.mapping[PhysicalDimension.Enthalpy]=SI.kW
        self.mapping[PhysicalDimension.VolumeFlow]=SI.cum/SI.h

        self.mapping[PhysicalDimension.MolarWeight]=SI.kg/SI.kmol

        self.mapping[PhysicalDimension.MolarVolume]=SI.cum/SI.kmol
        self.mapping[PhysicalDimension.MassDensity]=SI.kg/SI.cum
        self.mapping[PhysicalDimension.MolarDensity]=SI.kmol/SI.cum

        self.mapping[PhysicalDimension.SpecificMolarEnthalpy]=SI.kJ/SI.kmol
        self.mapping[PhysicalDimension.SpecificMassEnthalpy]=SI.kJ/SI.kg
        self.mapping[PhysicalDimension.HeatCapacity]=SI.kJ/SI.kmol/SI.K

        self.mapping[PhysicalDimension.HeatTransferCoefficient]=SI.W / SI.sqm / SI.K
        self.mapping[PhysicalDimension.MassTransferCoefficient]= SI.m / SI.s

        self.mapping[PhysicalDimension.MolarFraction]= SI.mol / SI.mol
        self.mapping[PhysicalDimension.MassFraction]= SI.kg / SI.kg
        self.mapping[PhysicalDimension.SpecificArea]= SI.sqm / SI.cum

        self.mapping[PhysicalDimension.DynamicViscosity]= SI.Pa / SI.s
        self.mapping[PhysicalDimension.Velocity]= SI.m / SI.s







