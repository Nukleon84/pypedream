from pypedream import  AlgebraicSystem, Equation, Variable,  Addition, Subtraction, Multiplication, Division, Unit, SI, METRIC,PhysicalDimension, UnitSet, UnitSetDefault, UnitSetSI
from pypedream import ScalarMethods as scalar
from pypedream import NewtonSolver
from pypedream import Sin, Cos, Exp
from pypedream.thermodynamics import PureComponentFunctionFactory, Substance,ThermodynamicSystem, PhysicalConstants, Properties
import pypedream.thermodynamics as thermo
import pypedream as sym
import pytest
import math
import matplotlib.pyplot as plt
import numpy as np
import pypedream.database.purecomponents as pcdb
from timeit import default_timer as timer
import random
import cProfile
import pstats
from pstats import SortKey

print("")
print ("Start timing")

sys= ThermodynamicSystem("Test")
sys.addComponent(pcdb.Water())
sys.addComponent(pcdb.Isopropanol())
sys.addComponent(pcdb.Methanol())

def test():
    for c in sys.components:
        for p in [e for e in Properties]:
            fdesc=c.functions[p]
            T= Variable("T", 273.15, SI.K)
            T.displayUnit=METRIC.C
            TC= c.constants[PhysicalConstants.CriticalTemperature]
            PC= c.constants[PhysicalConstants.CriticalPressure]
            f=sys.correlationFactory.createFunction(fdesc,T, TC, PC)
            for i in range(2000):
                T.value= random.uniform(100.0,550.0)
                f.reset()
                y= f.eval()

def test2():
    sys=AlgebraicSystem("test")
    x1= sys.makevar('x1',1)
    x2= sys.makevar('x2',1)
    x3= sys.makevar('x3',1)
    sys.eq(3*x1 - sym.Cos(x2*x3)- 3.0/2.0, "EQ1" )
    sys.eq(4*x1**2 - 625*x2**2 + 2*x2-1, "EQ2" )
    sys.eq(sym.Exp(-x1*x2) + 20*x3 + (10 * math.pi - 3.0)/3.0 , "EQ3")
    
    for i in range(1000):
        x1.value=random.uniform(0,3)
        x2.value=random.uniform(0,3)
        x2.value=random.uniform(0,3)
        solver= NewtonSolver(50,1e-6,1.0)
        solver.solve(sys)                

cProfile.run("test2()","mystats")

p = pstats.Stats('mystats')
p.sort_stats(SortKey.CUMULATIVE).print_stats(50)