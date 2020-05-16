
from pypedream  import  Variable, Addition, Subtraction, Multiplication, Division

import pytest

def test_add():
    x= Variable('x',2)
    y= Variable('y',3)
    expr = x+y
    assert pytest.approx(expr.eval()) == 5
    assert expr.print() == "x + y"
    assert pytest.approx(expr.diff(x)) == 1
    assert pytest.approx(expr.diff(y)) == 1

def test_subtract():
    x= Variable('x',2)
    y= Variable('y',3)
    expr = x-y
    assert pytest.approx(expr.eval()) == -1
    assert expr.print() == "x - y" 
    assert pytest.approx(expr.diff(x)) == 1
    assert pytest.approx(expr.diff(y)) == -1   

def test_multiply():
    x= Variable('x',2)
    y= Variable('y',3)
    expr = x*y
    assert pytest.approx(expr.eval()) == 6
    assert expr.print() == "x * y"    
    assert pytest.approx(expr.diff(x)) == 3
    assert pytest.approx(expr.diff(y)) == 2

def test_divide():
    x= Variable('x',1.0)
    y= Variable('y',2.0)
    expr = x/y
    assert pytest.approx(expr.eval()) == 1.0/2.0
    assert expr.print() == "x / y"
    assert pytest.approx(expr.diff(x)) == 0.5
    assert pytest.approx(expr.diff(y)) == -0.25   