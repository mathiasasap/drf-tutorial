import requests

ENDPOINT = "http://127.0.0.1:8000/api/status"


def do(method='get', data={}):
    r = requests.request(method, ENDPOINT, data=data)
    print(r.text)
    return r

do()
