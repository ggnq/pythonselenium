#run_method.py# -*- coding: utf-8 -*-
#封装get和post基类
import requests


class RunMethod:

    def post_main(self, url, data, header):
        res = None
        if header != None:
            res = requests.post(url=url, data=data, header=None)
        else:
            res = requests.post(url=url, data=data)
        return res

    def get_main(self, url, data=None, header=None):
        res = None
        if header != None:
            res = requests.get(url=url, data=None, header=header)
        else:
            res = requests.get(url=url, data=data)
        return res

    def run_main(self, method, url, data=None, header=None):
        res = None
        if method == 'post':
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)
        return res