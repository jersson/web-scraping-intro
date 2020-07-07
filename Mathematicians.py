from SimpleParser import SimpleParser
from bs4 import BeautifulSoup

class Mathematicians ():
    def __init__(self):
        self.__url = 'http://www.fabpedigree.com/james/mathmen.htm'

    def get_names(self):
        parser = SimpleParser()
        response = parser.get(self.__url)

        if response is not None:
            html = BeautifulSoup(response, 'html.parser')
            names = set()
            for li in html.select('li'):
                for name in li.text.split('\n'):
                    if len(name) > 0:
                        names.add(name.strip())
            return list(names)