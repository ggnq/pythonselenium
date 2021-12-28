import json

import pytest
import requests
from load_data import yaml_load

token = None

@pytest.mark.parametrize('', yaml_load.load('./user.yaml'))
def test_01(data):
    url =
    res = requests.post(url=url, json=data['user'])
    print(res.text)
    result = json.load(res.text)
    try:
        global token
        token = result['token']
    except:
        pass

    assert data['msg'] == result['msg']

def test_02():
    print(token)
