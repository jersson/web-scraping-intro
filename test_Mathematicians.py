from Mathematicians import Mathematicians


def test_get_names():
    mathematicians = Mathematicians()
    names = mathematicians.list_names()
    assert names is not None