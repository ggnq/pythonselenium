

import requests
import json


class RunMain:
    #当前类的第一个参数是self
    def send_get(self, url):
        res = requests.get(url=url).json()
        r = json.dumps(res, indent=2, sort_keys=True)
        return r

    def send_post(self, url, data):
        res = requests.post(url=url, data=data).json()
        r = json.dumps(res, indent=2, sort_keys=True)
        return r

    def run_main(self, url, method, data=None):  #把daa数据默认为空，因为get不用传数据，空参数要放在有值参数后面
        res = None
        if method == 'GET':
           res = self.send_get(url)
        else:
           res = self.send_post(url, data)
        return res


if __name__ == '__main__':
  #这种写法就是每次都要先实例化，然后再去调用run_main
    run = RunMain()
    url = 'http://127.0.0.1:8000/login/?username=dajiu&password=123'
    data = {
    'username':'dajiu',
    'password':'123456'
    }
    print(run.run_main(url, 'POST', data))


class RunMain2:
    # 构造函数
    def __init__(self, url, method, data=None):
        self.res = self.run_main(url, method, data)
        # 当前类的第一个参数是self

    def send_get(self, url):
        res = requests.get(url=url).json()
        r = json.dumps(res, indent=2, sort_keys=True)
        return r

    def send_post(self, url, data):
        res = requests.post(url=url, data=data).json()
        r = json.dumps(res, indent=2, sort_keys=True)
        return r

    def run_main(self, url, method, data=None):  # 把daa数据默认为空，因为get不用传数据，空参数要放在有值参数后面
        res = None
        if method == 'GET':
            res = self.send_get(url)
        else:
            res = self.send_post(url, data)
        return res


if __name__ == "__main__":
    url = 'http://127.0.0.1:8000/login/'
    data = {
        'username': 'sun',
        'password': '123',
    }
    run = RunMain2(url, 'POST', data)  # 实例化的同时执行构造函数
    print(run.res)


class RunMain3:
    #当前类的第一个参数是self
    def send_get(self, url):
        res = requests.get(url=url)
        return res.text

    def send_post(self, url, data):
        res = requests.post(url=url, data=data)
        return res

    def run_main(self, url, method, data=None):  #把data数据默认为空，因为get不用传数据，空参数要放在有值参数后面
        res = None
        if method == 'GET':
            res = self.send_get(url)
        else:
            res = self.send_post(url, data)
        return res.text


if __name__ == '__main__':
  #这种写法就是每次都要先实例化，然后再去调用run_main
    run = RunMain3()
    url = ''
    data = {

    }
    print(run.run_main(url, 'POST', data))