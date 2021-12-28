import pytest

class TestCase1(object):

    @classmethod
    def setup_class(cls):
        print('setup_class')

    def test1(self):
        print('test1')

    def test2(self):
        print('test2')

def setup_function():
    print('setup_function')

def teardown_function():
    print('teardown_function')

def setup_module():
    print('setup_module')

def teardown_module():
    print('teardown_module')

def test1():
    print('test1')

def test2():
    print('test2')

if __name__ == '__main__':
    pytest.main(['test07.py', '-sv'])
