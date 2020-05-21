from . enums import *

class EquilibriumMethod(object):
    def __init__(self):
        self.equilibriumApproach= EquilibriumApproach.GammaPhi
        self.activityMethod= ActivityMethod.Ideal
        self.equationOfState=EquationOfState.Ideal
        self.fugacityMethod= FugacityMethod.Ideal
        self.allowedPhases= AllowedPhases.VLE
        self.allowHenry=False
        self.poyntingCorrection=False
        