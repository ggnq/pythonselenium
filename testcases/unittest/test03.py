import unittest
import os


class MyTestcase03(unittest.TestCase):

    def test01(self):
        print('test01')

    def test02(self):
        print('test02')


class MyTestcase04(unittest.TestCase):

    def test03(self):
        print('test03')

    def test04(self):
        print('test04')


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    #通过测试用例类加载
    #suite.addTest(loader.loadTestsFromTestCase(MyTestcase03))
    #suite.addTest(loader.loadTestsFromTestCase(MyTestcase04))
    #通过测试用例模板加载
    #suite.addTest(loader.loadTestsFromModule(MyTestcase03))
    #suite.addTest(loader.loadTestsFromModule(MyTestcase04))
    #通过路径加载
    path = os.path.dirname(os.path.dirname(_file_))
    suite.addTest(loader.discover(path))


    runner = unittest.TextTestRunner()
    runner.run(suite)