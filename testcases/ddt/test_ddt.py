import os
from ddt import ddt, data, unpack, file_data
import unittest

def get_data():
    testdata = [{'name': 'tom', 'age': 30}], [{'name': 'kite', 'age': 30}]
    return testdata

@ddt
class MyTestCase(unittest.TestCase):
    #读取元组数据-单组数据
    @data(1, 2, 3)
    def test01(self, value):
        print(value)

    #读取元组数据-多组数据
    @data((1, 2, 3), (4, 5, 6))
    def test02(self, value):
        print(value)

    # 读取元组数据-拆分数据
    @data((1, 2, 3), (4, 5, 6))
    @unpack  #拆分数据
    def test03(self, value1, value2, value3):
        print(value1, value2, value3)

    # 读取列表数据
    @data([{'name': 'tom', 'age': 30}], [{'name': 'kite', 'age': 30}])
    def test04(self, value):
        print(value)

    # 读取字典数据
    @data({'name': 'tom', 'age': 30}, {'name': 'kite', 'age': 30})
    def test05(self, value):
        print(value)

    # 读取字典数据-拆分
    @data({'name': 'tom', 'age': 30}, {'name': 'kite', 'age': 30})
    @unpack
    def test06(self, name, age):
        print(name, age)

    #变量调用
    testdata = [{'name': 'tom', 'age': 30}, {'name': 'kite', 'age': 30}]

    @data(*testdata)
    def test07(self, value):
        print(value)

    #方法调用
    @data(get_data())
    def test08(self, value):
        print(value)

    #读文件
    @file_data(os.getcwd() + '/test.json')
    def test09(self, value2):
        print(value2)

if __name__ == '__main__':
    unittest.main()