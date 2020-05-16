from . unit import Unit
from . SI import SI

class METRIC(object):
    C=Unit.derive("°C","Celsius", SI.K, 1, 273.15)                
    bar=Unit.derive("bar","Bar (absolute)", SI.Pa, 1e5,0)                
    mbar=Unit.derive("mbar","MilliBar (absolute)", SI.Pa, 1e2,0)                

    ton=Unit.derive("ton","ton (metric)", SI.kg, 1e3,0)                

    weightPercent= Unit.derive("w-%","Weight Percent", SI.kg/SI.kg, 1e-2,0)
    molPercent= Unit.derive("mol-%","Mol Percent", SI.mol/SI.mol, 1e-2,0)
  