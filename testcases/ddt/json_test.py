import pytest
import json

def get_adta():
    with open('test.json') as f:
        lst = []
        data = json.load(f)
        lst.extend(data['keys'])
        return lst

@pytest.mark.parametrize('name', get_adta())
def test01(name):
    print(name)

if __name__ == '__main__':
    #print(get_adta())
    pytest.main(['-sv', 'json_test.py'])