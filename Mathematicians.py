from SimpleParser import SimpleParser
from bs4 import BeautifulSoup
from utils import *

class Mathematicians ():
    def __init__(self):
        self.__url = 'http://www.fabpedigree.com/james/mathmen.htm'

    def list_names(self, top = 100) -> list:
        '''
        Return a mathematician names list from http://www.fabpedigree.com/james/mathmen.htm 
        '''
        result = None
        try:
            parser = SimpleParser()
            response = parser.request(self.__url)

            if response is not None:
                html = BeautifulSoup(response, 'html.parser')
                names = set()
                for li in html.select('li'):
                    for name in li.text.split('\n'):
                        if (len(name) > 0 and len(names) < top):
                            names.add(name.strip())
                result = list(names)
        except Exception as error:
            log_error('Error: {}'.format(error))
        finally:
            return result