#uni_test.pyimport unittest

from demo import RunMain  #导入类
import unittest


class TestMethod(unittest.TestCase):

    def setUp(self):
        self.run = RunMain()   #每次都实例化

    def test_01(self):
        url = 'http://127.0.0.1:8000/login/?username=dajiu&password=123'
        data = {
         'username': 'dajiu2',
         'password': '123456'
        }
        res = self.run.run_main(url, 'POST', data)
        print(res)

    def test_02(self):
        url = 'http://127.0.0.1:8000/login/?username=dajiu&password=123'
        data = {
         'username': 'dajiu1',
         'password': '123456'
        }

        res = self.run.run_main(url, 'POST', data)
        print(res)

if __name__ == '__main__':
    unittest.main()