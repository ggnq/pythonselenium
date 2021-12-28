import pytest

class TestLoginCase(object):

    def test01(self):
        print('test001')
        assert 1 == 1

    def test02(self):
        print('test002')
        assert 1 == 2
01




if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_01.py'])