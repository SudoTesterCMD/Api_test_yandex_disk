import requests


class API_disk(object):


    def __init__(self, number_iter = None):
        self.number_iter = number_iter


    def get(self, url =  None, headers = None):
        return requests.get(f"{url}", headers = headers)

    def get_query_text(self, url = None, headers = None):
        return self.get(url, headers).text
    
    def get_query_content(self, url = None, headers = None):
        return self.get(url, headers).content

    def get_query_json(self, url = None, headers = None):
        return self.get(url, headers).json()