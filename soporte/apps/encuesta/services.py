import json
import requests

def get_data_api(url):
    r = requests.get(url)
    data = r.json()
    dump = json.dumps(data)
    dict = json.loads(dump)
    return dict