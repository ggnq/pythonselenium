# -*- coding: utf-8 -*-


from mock import mock

#重构mock  封装


def mock_test(mock_method, request_data, url, method, respone_data): #参数就是mock要模拟的方法，请求数据，url，方法，返回数据

    mock_method = mock.Mock(return_value=respone_data)    #模拟的是一个方法，把返回数据作为mock数据

    res = mock_method(url, method, request_data)        #方法的参数，执行res

    print(res)

    return res