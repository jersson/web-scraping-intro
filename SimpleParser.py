from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from utils import *

class SimpleParser():
    def __is_valid_web_response(self, res):
        '''
        Returns True if the response seems to be HTML, False otherwise.
        '''
        content_type = res.headers['Content-Type'].lower()

        return (res.status_code == 200
                and content_type is not None
                and content_type.find('html') > -1)

    def get(self, url):
        '''
        Attempts to get the content at `url` by making an HTTP GET request.
        If the content-type of response is some kind of HTML/XML, return the
        text content, otherwise return None.
        '''
        try:
            result = None
            with closing(get(url, stream=True)) as response:
                if self.__is_valid_web_response(response):
                    result = response.content

        except RequestException as error:
            log_error('Error making web requests to {}: {}'.format(url, error))
        finally:
            return result