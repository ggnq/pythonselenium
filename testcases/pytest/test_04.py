import pytest

class Testcase04(object):

    @pytest.mark.do
    def test_01(self):
        print('123')

    @pytest.mark.undo
    def test_02(self):
        print('456')

