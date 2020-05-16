from pypedream import  Variable, Addition, Subtraction, Multiplication, Division, Unit, SI, METRIC,PhysicalDimension, UnitSet, UnitSetDefault, UnitSetSI
from pypedream import ScalarMethods as scalar
import pytest

import matplotlib.pyplot as plt
import numpy as np

def printUnit(uom):
    print(f"Name {uom.name} Symbol: {uom.symbol} Dims: {uom.printDimensions()} Units: {uom.printBaseUnits()} Factor: {uom.factor} Offset: {uom.offset}")
    return

print(SI.K)
print(SI.mol)

print(f"{SI.N} Dims: {SI.N.printDimensions()} Units: {SI.N.printBaseUnits()}")

print(Unit.convert(SI.K, METRIC.C, 298.15))

units= UnitSetDefault()

printUnit(units[PhysicalDimension.Temperature])
printUnit(units[PhysicalDimension.Pressure])

x= Variable('x',1)
f=  x*x*x - 5*x +3 
scalar.solveNewtonRaphson(f,x)

x.value=1
scalar.solveBisection(f,x,0,1)

t = np.arange(0., 2., 0.1)


plt.plot(t, t*t*t-5*t+3, 'r') # plotting t, a separately 
plt.plot(t, 0*t, 'b') # plotting t, b separately 
plt.plot(x.value, 0, 'kx') # plotting t, b separately 

plt.show()