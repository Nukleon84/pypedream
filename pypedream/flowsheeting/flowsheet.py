from .base_element import BaseElement
from ..thermodynamics.data.thermodynamic_system import ThermodynamicSystem
from ..unitsofmeasure import PhysicalDimension
from .material_stream import MaterialStream

from ..numerics import AlgebraicSystem, NewtonSolver

class Flowsheet(BaseElement):
    
    def __init__(self, name, system:ThermodynamicSystem):
        super(Flowsheet, self).__init__(name,system)
        self.materialStreams={}
        self.units={}
        self.specifications={}
        return
    
    def mstr(self, name, system=None):
        if(name not in self.materialStreams):
            if(system==None):
                system=self.system
            mstr= MaterialStream(name, system)
            self.materialStreams[name]=mstr           
            
        return self.materialStreams[name]

    def instantiate(self, instance:AlgebraicSystem):
        super(Flowsheet, self).instantiate(instance)
        
        for s in self.materialStreams.values():
            s.instantiate(instance)
        
        for u in self.units.values():
            u.instantiate(instance)

        for u in self.specifications.values():
            instance.equations.append(u)


        return
    
    def solve(self):
        instance= AlgebraicSystem(self.name)
        self.instantiate(instance)
        solver= NewtonSolver()
        status=solver.solve(instance)
        return status

        


