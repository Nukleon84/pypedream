from pypedream  import  Variable, Addition, Subtraction, Multiplication, Division,Par

import pytest

def test_addmultiply():
    x= Variable('x',2)
    y= Variable('y',3)
    z= Variable('z',4)
    expr = x+y*z
    assert pytest.approx(expr.eval()) == 14
    assert expr.print() == "x + y * z"


def test_multiply_subtract():
    x= Variable('x',2)
    y= Variable('y',7)
    z= Variable('z',4)
    expr = x*Par(y-z)
    assert pytest.approx(expr.eval()) == 6
    assert expr.print() == "x * (y - z)"

