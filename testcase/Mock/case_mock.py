# -*- coding: utf-8 -*-
import unittest
import json
from api import RunMain2   #导入方法
from mock import mock
from mock_demp import mock_test  #导入mock_test
import HTMLTestRunner


class TestMethod(unittest.TestCase):
    def setUp(self):
      self.run = RunMain2()   #每次都实例化

    def test_01(self):
      url = 'http://10.1.30.118:3200/provider/user/user/login?loginName=15519560010&loginModel=0&password=12345678&loginType=01'
      data = {
    'loginName':'15519560010',
    'loginModel':'01',
    'password':'12345678',
    'loginModel':'0',
    'timeStamp':'1582616038764'
    }
      #mock_data = mock.Mock(return_value=data)
      #self.run.run_main = mock_data
      #res = self.run.run_main(url,'POST',data)

      mock_test(self.run.run_main, data, url, 'POST', data) #调用mock——test方法（模拟的方法，请求数据，url，方法，响应数据）

      #print(res)
      #print(type(res))
      #self.assertEqual(res['loginModel'],'0')
      print('第一个case')