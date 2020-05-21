from . enums import EquationOfState, EquilibriumApproach, ActivityMethod, EquationOfState, FugacityMethod, AllowedPhases

class EquilibriumMethod(object):
    def __init__(self):
        self.equilibriumApproach= EquilibriumApproach.GammaPhi
        self.activityMethod= ActivityMethod.Ideal
        self.equationOfState=EquationOfState.Ideal
        self.fugacityMethod= FugacityMethod.Ideal
        self.allowedPhases= AllowedPhases.VLE
        self.allowHenry=False
        self.poyntingCorrection=False
        