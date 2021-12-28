#get_data.py# -*- coding: utf-8 -*-
#封装获取变量数据

import sys
sys.path.append("G:/uni_test")
from testcase.case_excel import OperationExcel
from data_config import global_var
from operationjson import operation_json


class GetData:
    """docstring for GetData"""
    def __init__(self):
        self.opera_excel = OperationExcel()
        #之前遇到直接调用data.config.get_url()报错说data.config未定义，就实例化一下global_var类
        self.dataconfig = global_var()
        self.opera_json = operation_json()

    #去获取excel行数，就是我们的case个数
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    #获取是否执行
    #list indices must be integers,not str 遇到这个错误，在数据之前加上int
    def get_is_run(self, row):
        flag = None
        col = int(self.dataconfig.get_run())
        run_model = self.opera_excel.get_cell_value(row, col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    #获取是否需要header
    def is_header(self, row):
        col = int(self.dataconfig.get_header())
        header = self.opera_excel.get_cell_value(row, col)
        if header == 'yes':
            return self.dataconfig.get_header_value()
        else:
            return None

    #获取请求方式
    def get_request_method(self, row):
        col = int(self.dataconfig.get_request_way())
        request_method = self.opera_excel.get_cell_value(row, col)
        return request_method

    #获取url
    def get_request_url(self, row):
        col = int(self.dataconfig.get_url())
        url = self.opera_excel.get_cell_value(row, col)
        return url

    #获取请求数据
    def get_request_data(self, row):
        col = int(self.dataconfig.get_data())#第9列
        data = self.opera_excel.get_cell_value(row, col)#传入行数，取值
        if data:
            return data
        else:
            return None



    #通过获取关键字拿到data数据
    def get_data_for_json(self, row):
        data = self.get_request_data(row)  #取到的值
        request_data = self.opera_json.get_data(data)#取到的值传入get_data中，然后通过get_read读取到值
        return request_data    #返回请求数据

    #获取预期结果
    def get_expect_data(self, row):
        col = int(self.dataconfig.get_expect())
        get_expect = self.opera_excel.get_cell_value(row, col)
        return get_expect

    # 把返回结果写入excel
    def write_result(self, row, value):
        col = int(self.dataconfig.get_result())
        result = self.opera_excel.write_value(row, col, value)
        return result




    def get_depend_key(self, row):
        col = int(self.dataconfig.get_data_depend())
        depend_key = self.opera_excel.get_cell_value(row, col)
        if depend_key == '':
            return None
        else:
            return depend_key

    def get_depend_key(self, row):
        col = int(self.dataconfig.get_data_depend())
        depend_key = self.opera_excel.get_cell_value(row, col)
        if depend_key == "":
            return None
        else:
            return depend_key
        # 判断case是否有依赖

    def is_depend(self, row):
        col = int(self.dataconfig.get_field_depend())
        depend_case_id = self.opera_excel.get_cell_value(row, col)
        if depend_case_id == "":
            return None
        else:
            return depend_case_id
        # 获取数据依赖字段

    def get_depend_filed(self, row):
        col = int(self.dataconfig.get_field_depend())
        data = self.opera_excel.get_cell_value(row, col)
        if data == "":
            return None
        else:
            return data