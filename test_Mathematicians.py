from Mathematicians import Mathematicians


def test_get_names():
    mathematicians = Mathematicians()
    names = mathematicians.get_names()
    assert names is not None