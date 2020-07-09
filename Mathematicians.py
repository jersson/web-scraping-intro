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
                names = list()
                for li in html.select('li'):
                    html_list_names = li.text.split('\n')
                    if len(html_list_names) == 6:
                        for name in html_list_names:
                            if (len(name) > 0 and len(names) < top):
                                names.append(name.strip())
                result =  names
        except Exception as error:
            log_error('Error: {}'.format(error))
        finally:
            return result