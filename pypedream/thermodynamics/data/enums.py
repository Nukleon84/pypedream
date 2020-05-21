from enum import Enum,auto

class FunctionTypes(Enum):        
        Antoine= auto()
        ExtendedAntoine= auto()
        AlyLee= auto()
        Polynomial= auto()
        Dippr106 = auto()
        Rackett= auto()
        Wagner= auto()
        Watson= auto()
        Dippr117= auto()
        PolynomialIntegrated= auto()
        Dippr102= auto()
        Kirchhoff= auto()
        ExtendedKirchhoff= auto()
        Sutherland= auto()
        Chemsep16= auto()
        Chemsep16Integrated= auto()
        Chemsep101= auto()
        Chemsep102= auto()
        Chemsep106= auto()

class Properties(Enum): 
        VaporPressure= auto()
        IdealGasHeatCapacity= auto()
        LiquidHeatCapacity= auto()
        HeatOfVaporization= auto()
        LiquidDensity= auto()
        SurfaceTension= auto()
        LiquidHeatConductivity= auto()
        VaporHeatConductivity= auto()
        LiquidViscosity= auto()
        VaporViscosity = auto()       

class PhysicalConstants(Enum): 
        MolarWeight= auto() 
        CriticalPressure= auto() 
        CriticalTemperature= auto() 
        CriticalVolume= auto() 
        CriticalDensity= auto() 
        AcentricFactor= auto() 
        UniquacQ= auto() 
        UniquacQP= auto() 
        UniquacR= auto() 
        HeatOfFormation= auto() 
        RKSA= auto() 
        RKSB= auto()         

class EquationOfState(Enum):    
        Ideal= auto() 
        RedlichKwong= auto() 
        SoaveRedlichKwong= auto() 
        PengRobinson= auto() 
    

class EquilibriumApproach(Enum):    
        GammaPhi= auto() 
        PhiPhi= auto() 
    

class FugacityMethod(Enum):    
        Ideal= auto() 
        RedlichKwong= auto() 
        SoaveRedlichKwong= auto() 
        PengRobinson= auto() 
    

class ActivityMethod(Enum):    
        Ideal= auto() 
        Wilson= auto() 
        NRTL= auto() 
        UNIQUAC= auto() 
        MODUNIQUAC= auto() 
        UNIFAC= auto() 
   
class ExcessEnthalpyMethod(Enum):    
        Ideal= auto() 
        NRTL= auto() 
        UNIQUAC= auto() 
        MODUNIFAC= auto() 
    

class AllowedPhases(Enum):    
        V= auto() 
        L= auto() 
        VLE= auto() 
        LLE= auto() 
        VLLE= auto() 
        SLE= auto() 
        SLLE= auto()     

class ReferencePhase(Enum):    
        Liquid= auto()         
        Vapor= auto() 
 

class PhaseState(Enum):    
        Liquid= auto() 
        BubblePoint= auto() 
        LiquidVapor= auto() 
        DewPoint= auto() 
        Vapor= auto() 

propertyToName={
     Properties.HeatOfVaporization:"HVAP",
     Properties.IdealGasHeatCapacity:"CPID",
     Properties.LiquidDensity:"DENL",
     Properties.LiquidHeatCapacity:"CL",
     Properties.LiquidHeatConductivity:"KLIQ",
     Properties.SurfaceTension:"ST",
     Properties.VaporHeatConductivity:"KVAP",
     Properties.VaporViscosity:"VISV",
     Properties.LiquidViscosity:"VISL",
     Properties.VaporPressure:"VP"
}       
constantToName={
        PhysicalConstants.CriticalPressure:"PC",
        PhysicalConstants.CriticalTemperature:"TC",
        PhysicalConstants.MolarWeight:"MW",
        PhysicalConstants.AcentricFactor:"ACF",
}
nameToProperty={
     "HVAP":Properties.HeatOfVaporization,
     "CPID":Properties.IdealGasHeatCapacity,
     "DENL":Properties.LiquidDensity,
     "CL":Properties.LiquidHeatCapacity,
     "KLIQ":Properties.LiquidHeatConductivity,
     "ST":Properties.SurfaceTension,
     "KVAP":Properties.VaporHeatConductivity,
     "VISV":Properties.VaporViscosity,
     "VISL":Properties.LiquidViscosity,
     "VP":Properties.VaporPressure}   