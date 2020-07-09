from .context import src
from src.Mathematicians import Mathematicians

def test_get_names():
    mathematicians = Mathematicians()
    names = mathematicians.list_names(100)
    assert names is not None

def test_get_names_with_default_parameter_value():
    mathematicians = Mathematicians()
    names = mathematicians.list_names()
    assert len(names) == 100

def test_get_10_names():
    mathematicians = Mathematicians()
    names = mathematicians.list_names(10)
    assert len(names) == 10
