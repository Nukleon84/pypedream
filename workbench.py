from pypedream import  AlgebraicSystem, Equation, Variable, Constant, Addition, Subtraction, Multiplication, Division, Unit, SI, METRIC,PhysicalDimension, UnitSet, UnitSetDefault, UnitSetSI
from pypedream import ScalarMethods as scalar
from pypedream import Sin, Cos, Exp
import pypedream as sym
import pytest
import math
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
x1=x.value

x.value=1
scalar.solveBisection(f,x,1,2)
x2=x.value
t = np.arange(0., 2., 0.001)


plt.plot(t, t*t*t-5*t+3, 'r') # plotting t, a separately 
plt.plot(t, 0*t, 'b') # plotting t, b separately 
plt.plot(x2, 0, 'kx') # plotting t, b separately 
plt.plot(x1, 0, 'ko') # plotting t, b separately 

#plt.show()

x1= Variable('x1',1)
x2= Variable('x2',1)
x3= Variable('x3',1)

sys=AlgebraicSystem("test")
sys.equations.append(Equation(3*x1 - sym.Cos(x2*x3)- 3.0/2.0 ))
sys.equations.append(Equation(4*x1**2 - 625*x2**2 + 2*x2-1 ))
sys.equations.append(Equation(sym.Exp(-x1*x2) + 20*x3 + (10 * math.pi - 3.0)/3.0 ))

sys.variables.append(x1)
sys.variables.append(x2)
sys.variables.append(x3)

sys.createIndex()
sys.createSparsityPattern()

for sp in sys.sparsityPattern:
    print(sp)