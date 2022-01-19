# -*- coding: utf-8 -*-
import unittest
import json
from demo import RunMain# 导入方法
from lib import HTMLTestRunner_PY3


class TestMethod(unittest.TestCase):
    def setUp(self):
        self.run = RunMain()  # 每次都实例化

    def test_01(self):
        url = 'http://10.1.30.118:3200/provider/user/user/login?loginName=15519560000&loginModel=0&password=12345678&loginType=01'
        data = {
            'loginName': '15519560000',
            'loginModel': '01',
            'password': '12345678',
            'loginModel': '0',
            'timeStamp': '1582616038764'
        }

    res = self.run.run_main(url, 'POST', data)
    r = json.loads(res)
    self.assertEqual(r['code'], '501')
    print('第一个case')


# globals()['userid'] = '999'  #定义全局变量，把test01和test02建立依赖关系，可用于平时需要保存信息，比如token等


# @unittest.skip('test_02')   #跳过第二个case，只执行第一个case

    def test_02(self):
        # print(userid)
        url = 'http://10.1.30.118:3200/provider/user/user/login?loginName=15519560001&loginModel=0&password=12345678&loginType=01'
        data = {
            'loginName': '15519560001',
            'loginModel': '01',
            'password': '12345678',
            'loginModel': '0',
            'timeStamp': '1582616038764'
        }
        res = self.run.run_main(url, 'POST', data)
        r = json.loads(res)
        self.assertNotEqual(r['code'], '202', '测试失败')  # 不等于
        print('第二个case')


if __name__ == '__main__':
    filepath = "../report/test_report.html"  # 打开文件
    fp = open(filepath, 'wb')  # 以读写模式打开文件
    sutie = unittest.TestSuite()  # 创建一个容器，放case
    sutie.addTest(TestMethod('test_02'))
    sutie.addTest(TestMethod('test_01'))  # 想放几个case就放几个case，一个case一条语句，按照添加case的顺序作为执行顺序
    runner = HTMLTestRunner_PY3.HTMLTestRunner(stream=fp, title='This is my first testreport')  # 设置报告的流文件和报告名字
    runner.run(sutie)  # 调用case集合，使htmltestrunner与unittest结合起来
    # unittest.TextTestRunner().run(sutie)
