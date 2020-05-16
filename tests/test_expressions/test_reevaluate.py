from pypedream  import  Variable, Addition, Subtraction, Multiplication, Division
import pytest

def test_reevaluate():
    x= Variable('x',2)
    y= Variable('y',3)
    expr = x+y
    assert pytest.approx(expr.eval()) == 5
    assert expr.print() == "x + y"
    y.value=40
    
    expr.reset()
    assert pytest.approx(expr.eval()) == 42
    assert expr.print() == "x + y"