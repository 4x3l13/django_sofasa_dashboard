import json
import requests

def get_data_api(url):
    r = requests.get(url)
    data = r.json()
    dump = json.dumps(data)
    dict = json.loads(dump)
    return dict

def get_data_api_json(url):
    r = requests.get(url)
    data = r.json()
    dump = json.dumps(data)
    dict = json.loads(dump)
    return dict,dump

def post_data_api(url,dict):
    r = requests.post(url,json=dict)
    
def delete_data_api(url):
    r = requests.delete(url)

def put_data_api(url,dict):
    r = requests.put(url,dict)