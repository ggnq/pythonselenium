#run_method.py# -*- coding: utf-8 -*-
#封装get和post基类
import requests


class RunMethod:

    def post_main(self, url, data, headers):
        res = None
        if header != None:
            res = requests.post(url=url, data=data, headers=None)
        else:
            res = requests.post(url=url, data=data)
        return res

    def get_main(self, url, data=None, headers=None):
        res = None
        if header != None:
            res = requests.get(url=url, data=None, headers=headers)
        else:
            res = requests.get(url=url, data=data)
        return res

    def run_main(self, method, url, data=None, headers=None):
        res = None
        if method == 'post':
            res = self.post_main(url, data, headers)
        else:
            res = self.get_main(url, data, headers)
        return res