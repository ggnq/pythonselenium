#data_config.py#-*- coding: utf-8 -*-
#根据每个字段的行数给模板定义一个固定变量
#TypeError: test() takes 0 positional arguments but 1 was given 遇到这个报错信息，把函数默认加上self参数


class global_var:
    Id = '0'
    request_name = '1'
    url = '2'
    run = '3'
    request_way = '4'
    header = '5'
    case_depend = '6'
    data_depend = '7'
    filid_depend = '8'
    data = '9'
    expect = '10'
    result = '11'

    def get_id(self):
        return global_var.Id

    def get_url(self):
        return global_var.url

    def get_run(self):
        return global_var.run



    def get_request_way(self):
        return global_var.request_way

    def get_header(self):
        return global_var.header

    def get_case_depend(self):
        return global_var.case_depend

    def get_data_depend(self):
        return global_var.data_depend

    def get_filid_depend(self):
        return global_var.filid_depend

    def get_data(self):
        return global_var.data

    def get_expect(self):
        return global_var.expect

    def get_result(self):
        return global_var.result

    def get_header_value(self):
        header = {
            'header':'1234',
            'cookie':'dajiujiu'
        }