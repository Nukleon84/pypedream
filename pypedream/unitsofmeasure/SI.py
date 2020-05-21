from . unit import Unit

class SI(object):
    none= Unit("","Dimensionless", [0,0,0,0,0,0,0,0])
    m=Unit("m","Meter", [1,0,0,0,0,0,0,0])        
    kg=Unit("kg","Kilogram", [0,1,0,0,0,0,0,0])                
    s= Unit("s","Second", [0,0,1,0,0,0,0,0])                
    K=Unit("K","Kelvin", [0,0,0,0,1,0,0,0])                
    mol= Unit("mol","mol", [0,0,0,0,0,1,0,0])                
    kmol= Unit.derive("kmol","KiloMol",mol,1e3,0)                 

    N= Unit.derive("N","Newton", kg*m/(s**2))                
    J= Unit.derive("J","Joule",N*m)                

    Pa= Unit.derive("Pa","Pascal",N/m**2) 
    kPa= Unit.derive("kPa","KiloPascal",Pa,1e3,0)                 

    W= Unit.derive("W","Watt",J/s)                

    min= Unit.derive("min","Minute",s,60,0)                
    h= Unit.derive("h","hour",s,3600,0)                

    sqm= Unit.derive("sqm","square-meter",m**2)        
    cum= Unit.derive("cum","cubic-meter",m**3)        

    kJ= Unit.derive("kJ","KiloJoule",J,1e3,0)  
    kW= Unit.derive("kW","KiloWatt",W,1e3,0)  
    MW= Unit.derive("MJ","MegaJoule",W,1e6,0)  



