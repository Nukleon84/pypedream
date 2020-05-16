from pypedream  import  Variable, Sin, Cos,Tan, Sinh, Cosh, Tanh
import pytest
import math

def test_sin():
    x= Variable('x',math.pi/2.0)    
    expr = Sin(x)
    assert pytest.approx(expr.eval()) == math.sin(math.pi/2.0)
    assert expr.print() == "sin(x)"

def test_cos():
    x= Variable('x',math.pi/2.0)    
    expr = Cos(x)
    assert pytest.approx(expr.eval()) == math.cos(math.pi/2.0)
    assert expr.print() == "cos(x)"    

def test_tan():
    x= Variable('x',math.pi/2.0)    
    expr = Tan(x)
    assert pytest.approx(expr.eval()) == math.tan(math.pi/2.0)
    assert expr.print() == "tan(x)"  

def test_sinh():
    x= Variable('x',math.pi/2.0)    
    expr = Sinh(x)
    assert pytest.approx(expr.eval()) == math.sinh(math.pi/2.0)
    assert expr.print() == "sinh(x)"

def test_cosh():
    x= Variable('x',math.pi/2.0)    
    expr = Cosh(x)
    assert pytest.approx(expr.eval()) == math.cosh(math.pi/2.0)
    assert expr.print() == "cosh(x)"    

def test_tanh():
    x= Variable('x',math.pi/2.0)    
    expr = Tanh(x)
    assert pytest.approx(expr.eval()) == math.tanh(math.pi/2.0)
    assert expr.print() == "tanh(x)"  

