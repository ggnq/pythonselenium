import pytest

class Testcase02(object):

    def test01(self):
        print('test01')
        self.add()

    def add(self):
        print('add')

    def test02(self):
        print('test02')



if __name__ == '__main__':
    pytest.main('test_02')