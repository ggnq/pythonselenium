#operationjson.py# -*- coding: utf-8 -*-

import json


class operation_json:

    def __init__(self):
        self.data = self.read_data()

    # 读取json文件
    def read_data(self):
        with open('case.json') as fp:  # 自动会关闭文件，不用再close.()
            data = json.load(fp)  # 加载文件
        return data

    def get_data(self, requestdata=None):
        if requestdata == None:
            return ''
        return self.data[requestdata]

    # # 写入json
    # def write_data(self, data=None):
    #     with open("G:/uni_test/data/请求数据.json", 'w') as fp:
    #         fp.write(json.dumps(data))


if __name__ == '__main__':
    operas = operation_json()
    # print(operas.read_data())
    print(operas.get_data('login'))
