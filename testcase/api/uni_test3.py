#uni_test.py# -*- coding: utf-8 -*-
import unittest
import json
from demo import RunMain3   #导入方法
class TestMethod(unittest.TestCase):
    def setUp(self):
      self.run = RunMain3()   #每次都实例化
      print('执行开始')
    def tearDown(self):
       print('执行结束')
    def test_01(self):
      url = 'http://10.1.30.118:3200/provider/user/user/login?loginName=15519560000&loginModel=0&password=12345678&loginType=01'
      data = {
    'loginName':'15519560000',
    'loginModel':'01',
    'password':'12345678',
    'loginModel':'0',
    'timeStamp':'1582616038764'
    }
      res = self.run.run_main(url,'POST',data)
      r = json.loads(res)                                    #需要用print（type（res））判断返回值的类型是不是字典，如果不是，应该把数据处理成json格式（字典）打印出来      self.assertEqual(r['code'],'501'，‘测试失败’)            #增加断言，判断返回的code是否等于501，如果相等，无输出，如果不等，输出测试失败

    def test_02(self):
      url = 'http://10.1.30.118:3200/provider/user/user/login?loginName=15519560001&loginModel=0&password=12345678&loginType=01'
      data = {
    'loginName':'15519560001',
    'loginModel':'01',
    'password':'12345678',
    'loginModel':'0',
    'timeStamp':'1582616038764'
    }
      res = self.run.run_main(url,'POST',data)
      r = json.loads(res)
      self.assertEqual(r['code'],'202'，‘测试失败’)
if __name__ == '__main__':
    unittest.main()