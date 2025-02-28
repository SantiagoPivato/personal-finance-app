import requests
from  urllib.parse import urlencode

class Api:
    url: str = None
    key: str = None
    last_status_code: int = None

    def call(self, endpoint: str, method: str, data: dict = {}): 
        #"requests" module function tu be used, e.g. requests.get(), requests.post()S, ...
        call_fn = getattr(requests, method.lower())
        
        #Creating url
        call_url = self.url + endpoint
        if method.lower() == "get" and data != {}:
            call_url += "?" + urlencode(data)

        
        #Api call
        call_response = call_fn(url=call_url, data=data, verify=False)

        #Saving status code
        self.last_status_code = call_response.status_code
        return call_response
    

class ApiREST(Api):
    def call(self, endpoint: str, method: str, data: dict = {}): 
        raw_response = super().call(endpoint, method, data)
        if(self.last_status_code == 200):
            return raw_response.json()
        else:
            return raw_response


class ApiEstadisticasCambiariasBCRA(ApiREST):
    def __init__(self):
        self.url = "https://api.bcra.gob.ar/estadisticas/v3.0/"
        self.key = False
        super().__init__()

    
