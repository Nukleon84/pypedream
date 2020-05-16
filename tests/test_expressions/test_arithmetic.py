from pypedream  import  Variable, Addition, Subtraction, Multiplication, Division
import pytest

def test_add():
    x= Variable('x',2)
    y= Variable('y',3)
    expr = Addition(x,y)
    assert pytest.approx(expr.eval()) == 5
    assert expr.print() == "x + y"

def test_subtract():
    x= Variable('x',2)
    y= Variable('y',3)
    expr = Subtraction(x,y)
    assert pytest.approx(expr.eval()) == -1
    assert expr.print() == "x - y"    

def test_multiply():
    x= Variable('x',2)
    y= Variable('y',3)
    expr = Multiplication(x,y)
    assert pytest.approx(expr.eval()) == 6
    assert expr.print() == "x * y"    

def test_divide():
    x= Variable('x',2.0)
    y= Variable('y',3.0)
    expr = Division(x,y)
    assert pytest.approx(expr.eval()) == 2.0/3.0
    assert expr.print() == "x / y"    