import requests
import json


class initiate_calls(object):
    """
    - Class to intiate the calls
    - Will define the initate request method used by all the searches.
    - Will also define the individual search methods
    """

    def init_request(self, url, payload):
        self.url = url
        self.payload = payload
        result = None
        try:
            r = requests.get(self.url, params=self.payload, timeout=15)
            if r.status_code == 200:
                result = json.loads(r.text)
            return result, r.status_code, r.elapsed.total_seconds()
        except:
            # return a generic error, status = 500, from IANA HTTP status code
            return None, 500, -1
