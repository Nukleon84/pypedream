from ..factories.pureComponentFunctionFactory import PureComponentFunctionFactory
from .equilibrium_method import EquilibriumMethod
from .enthalpy_method import EnthalpyMethod, PureEnthalpy
from .enums import ActivityMethod, FugacityMethod, EquilibriumApproach, EquationOfState, AllowedPhases, ReferencePhase, PhysicalConstants
from .substance import Substance
from ..factories.variable_factory import VariableFactory
class ThermodynamicSystem(object):
    
    def __init__(self,name, baseMethod="IDEAL"):
        self.name=name
        self.baseMethod=baseMethod
        self.components=[]
        self.correlationFactory= PureComponentFunctionFactory()
        self.variableFactory=VariableFactory()
        self.equilibrium= EquilibriumMethod()
        self.modifyDefaults()
        self.enthalpyMethod= EnthalpyMethod()
        return
    
    def modifyDefaults(self):
        if(self.baseMethod=="NRTL"):
            self.equilibrium.activityMethod= ActivityMethod.NRTL
        if(self.baseMethod=="Wilson"):
            self.equilibrium.activityMethod= ActivityMethod.Wilson
        return

    def addComponent(self, substance:Substance):
        self.components.append(substance)
        enth= PureEnthalpy(self.variableFactory, substance)
        enth.Tref.value=298.15
        self.enthalpyMethod.pureFunctions.append(enth)
        return self
    
    def __str__(self):
        lines=[]
        lines.append(f'System: {self.name}')
        lines.append('')
        lines.append('Equilibrium')
        lines.append('')
        lines.append(f'Phases   : {self.equilibrium.allowedPhases}')
        lines.append(f'VLEQ     : {self.equilibrium.equilibriumApproach}')        
        lines.append(f'Gamma    : {self.equilibrium.activityMethod}')
        lines.append(f'Phi      : {self.equilibrium.fugacityMethod}')
        lines.append(f'Henry    : {self.equilibrium.allowHenry}')
        lines.append(f'Poynting : {self.equilibrium.poyntingCorrection}')
        lines.append('')
        lines.append('')
        lines.append('Units of measure')
        lines.append('')
        lines.append('{0}{1}{2}{3}'.format('Dimension'.ljust(25),'Internal'.ljust(15),'Input'.ljust(15),'Output'.ljust(15)  ))
        for unit in self.variableFactory.internalSet.mapping.keys():
             lines.append('{0}{1}{2}{3}'.format(unit.name.ljust(25),self.variableFactory.internalSet[unit].symbol.ljust(15),self.variableFactory.inputSet[unit].symbol.ljust(15),self.variableFactory.outputSet[unit].symbol.ljust(15)  ) )

        lines.append('')
        lines.append('')
        lines.append('Components')
        lines.append('')            
        #   _logger.Log(String.Format("{0,-25} {1,-15} {2,-15} {3,-15} {4,-15} {5,-15} {6,-15}", "Name", "ID", "CAS-No", "Inert", "MOLW", "TC", "PC")); 
        lines.append('{0}{1}{2}{3}{4}{5}{6}'.format('Name'.ljust(25),'ID'.ljust(15),'Cas-No'.ljust(15),'Inert'.ljust(15),'MOLW'.ljust(15),'TC'.ljust(15),'PC'.ljust(15)  ))
        for comp in self.components:
            lines.append('{0}{1}{2}{3}{4}{5}{6}'.format(
                comp.name.ljust(25),
                comp.id.ljust(15),
                comp.casno.ljust(15),
                str(comp.isInert).ljust(15),
                str(comp.constants[PhysicalConstants.MolarWeight].value).ljust(15),
                str(comp.constants[PhysicalConstants.CriticalTemperature].value).ljust(15),
                str(comp.constants[PhysicalConstants.CriticalPressure].value).ljust(15)  ))
        lines.append('')
        lines.append('')
        lines.append('Enthalpy Calculation')
        lines.append('')       
        #_logger.Log(String.Format("{0,-15} {1,-10} {2,-12} {3,-8} {4,-8} {5,-5}", "Comp", "Phase", "Href", "Tref", "TPc", "Fixed Phase Change"));
        lines.append('{0}{1}{2}{3}{4}{5}{6}'.format('Name'.ljust(25),'ID'.ljust(15),'Phase'.ljust(15),'Href'.ljust(15),'Tref'.ljust(15),'TPc'.ljust(15),'PC@TSYS'.ljust(15)))
        for enth in self.enthalpyMethod.pureFunctions:
            lines.append('{0}{1}{2}{3}{4}{5}{6}'.format(
                enth.substance.name.ljust(25),
                enth.substance.id.ljust(15),
                enth.referenceState.name.ljust(15),
                str(enth.Href.value).ljust(15),
                str(enth.Tref.value).ljust(15),
                str(enth.Tpc.value).ljust(15),
                str(enth.freePhaseChange).ljust(15)))
        lines.append('')
        lines.append('')
        lines.append('Pure Component Property Correlations')
        lines.append('')                 
        #_logger.Log(String.Format("{0,-15} {1,-25} {2,-15} {3,-8} {4,-8} {5,-5} {6,-25}", "Comp", "Property", "Form", "Min T", "Max T", "Coeff", "Equation"));
        lines.append('{0}{1}{2}{3}{4}{5}{6}{7}{8}'.format('Name'.ljust(25),'ID'.ljust(15),'Property'.ljust(25),'Form'.ljust(15),'Tmin'.ljust(15),'Tmax'.ljust(15),'T Unit'.ljust(15),'Num Coeff'.ljust(15),'Unit'.ljust(15)))
        for c in self.components:
           for f in c.functions.values():
               lines.append('{0}{1}{2}{3}{4}{5}{6}{7}{8}'.format(
                    c.name.ljust(25),
                    c.id.ljust(15),
                    f.property.name.ljust(25),
                    f.functionType.name.ljust(15),
                    str(f.tmin).ljust(15),
                    str(f.tmax).ljust(15),
                    f.xUnit.symbol.ljust(15),
                    str(len(f.coefficients)).ljust(15),
                    f.yUnit.symbol.ljust(15)))

       


        return '\n'.join(lines)