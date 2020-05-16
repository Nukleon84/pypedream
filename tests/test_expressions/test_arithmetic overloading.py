
from pypedream import  Variable, Addition, Subtraction, Multiplication, Division
import pytest

def test_add():
    x= Variable('x',2)
    y= Variable('y',3)
    expr = x+y
    assert pytest.approx(expr.eval()) == 5
    assert expr.print() == "x + y"

def test_subtract():
    x= Variable('x',2)
    y= Variable('y',3)
    expr = x-y
    assert pytest.approx(expr.eval()) == -1
    assert expr.print() == "x - y"    

def test_multiply():
    x= Variable('x',2)
    y= Variable('y',3)
    expr = x*y
    assert pytest.approx(expr.eval()) == 6
    assert expr.print() == "x * y"    

def test_divide():
    x= Variable('x',2.0)
    y= Variable('y',3.0)
    expr = x/y
    assert pytest.approx(expr.eval()) == 2.0/3.0
    assert expr.print() == "x / y"  


def test_add_literal_right():
    x= Variable('x',2)    
    expr = x+3.0
    assert pytest.approx(expr.eval()) == 5
    assert expr.print() == "x + 3.0"

def test_subtract_literal_right():
    x= Variable('x',2)    
    expr = x-3.0
    assert pytest.approx(expr.eval()) == -1
    assert expr.print() == "x - 3.0"    

def test_multiply_literal_right():
    x= Variable('x',2)    
    expr = x*3.0
    assert pytest.approx(expr.eval()) == 6
    assert expr.print() == "x * 3.0"    

def test_divide_literal_right():
    x= Variable('x',2.0)    
    expr = x/3.0
    assert pytest.approx(expr.eval()) == 2.0/3.0
    assert expr.print() == "x / 3.0"      


def test_add_literal_left():
    
    y= Variable('y',3)
    expr = 2.0+y
    assert pytest.approx(expr.eval()) == 5
    assert expr.print() == "2.0 + y"

def test_subtract_literal_left():    
    y= Variable('y',3)
    expr = 2.0-y
    assert pytest.approx(expr.eval()) == -1
    assert expr.print() == "2.0 - y"    

def test_multiply_literal_left():    
    y= Variable('y',3)
    expr = 2.0*y
    assert pytest.approx(expr.eval()) == 6
    assert expr.print() == "2.0 * y"    

def test_divide_literal_left():
    
    y= Variable('y',3.0)
    expr = 2.0/y
    assert pytest.approx(expr.eval()) == 2.0/3.0
    assert expr.print() == "2.0 / y"  
