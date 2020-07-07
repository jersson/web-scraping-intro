from SimpleParser import SimpleParser

def test_make_valid_request():
    url = 'https://realpython.com/python-web-scraping-practical-introduction/'
    parser = SimpleParser()
    parsing_result = parser.get(url) 
    assert parsing_result is not None

def test_make_invalid_request():
    url = 'https://XYZrealpython.com/python-web-scraping-practical-introduction/'
    parser = SimpleParser()
    parsing_result = parser.get(url) 
    assert parsing_result is None