from HtmlParser import HtmlParser

def test_make_valid_request():
    url = 'https://realpython.com/python-web-scraping-practical-introduction/'
    parser = HtmlParser()
    parsing_result = parser.request(url) 
    assert parsing_result is not None

def test_make_invalid_request():
    url = 'https://XYZrealpython.com/python-web-scraping-practical-introduction/'
    parser = HtmlParser()
    parsing_result = parser.request(url) 
    assert parsing_result is None