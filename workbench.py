from pypedream import  AlgebraicSystem, Equation, Variable,  Addition, Subtraction, Multiplication, Division, Unit, SI, METRIC,PhysicalDimension, UnitSet, UnitSetDefault, UnitSetSI
from pypedream import ScalarMethods as scalar
from pypedream import NewtonSolver
from pypedream import Sin, Cos, Exp
from pypedream.thermodynamics import PureComponentFunctionFactory, Substance
import pypedream.thermodynamics as thermo
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


#plt.plot(t, t*t*t-5*t+3, 'r') # plotting t, a separately 
#plt.plot(t, 0*t, 'b') # plotting t, b separately 
#plt.plot(x2, 0, 'kx') # plotting t, b separately 
#plt.plot(x1, 0, 'ko') # plotting t, b separately 

#plt.show()

x1= Variable('x1',1)
x2= Variable('x2',1)
x3= Variable('x3',1)

sys=AlgebraicSystem("test")

sys.equations.append(Equation(3*x1 - sym.Cos(x2*x3)- 3.0/2.0, "EQ1" ))
sys.equations.append(Equation(4*x1**2 - 625*x2**2 + 2*x2-1, "EQ2" ))
sys.equations.append(Equation(sym.Exp(-x1*x2) + 20*x3 + (10 * math.pi - 3.0)/3.0 , "EQ3"))

sys.variables.extend([x1,x2,x3])

x1values=[]
x2values=[]
x3values=[]


def callback(iter, norm, error):
    x1values.append(x1.value)
    x2values.append(x2.value)
    x3values.append(x3.value)
    

solver= NewtonSolver(50,1e-6,1.0,callback)
solver.solve(sys)
for v in sys.variables:
    print(v.value)
#Assert.AreEqual(0.833196581863439, x1.Val(), 1e-6);
#Assert.AreEqual(0.0549436583091183, x2.Val(), 1e-6);
#Assert.AreEqual(-0.521361434378159, x3.Val(), 1e-6);

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(xs=x1values, ys=x2values, zs=x3values)
ax.scatter3D(x1values, x2values, x3values)
#plt.show()

T= Variable("T", 273.15, SI.K)
print(T.quantity())
T.displayUnit=METRIC.C
print(T.quantity())

water= Substance("Water", "H2O", 18.01)

water.addFunction(thermo.Properties.LiquidHeatCapacity, thermo.FunctionTypes.Polynomial, 150,550, [4.18, 1e-3, 2.124], SI.K, SI.J/SI.mol/SI.K)
factory=thermo.PureComponentFunctionFactory()

fdesc=water.functions[thermo.Properties.LiquidHeatCapacity]

f1=factory.createFunction(fdesc,T)
print(f1)