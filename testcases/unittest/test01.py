import unittest

class MyTestcase(unittest.TestCase):
    def setUp(self) -> None:
        print('setup....')

    def test01(self):
        print('test01')
        self.assertEqual(1+2, 3)
    def test02(self):
        print('test02')
        self.assertGreaterEqual(5, 4)

    def aaa(self):
        print('aaa')

    def tearDown(self) -> None:
        print('tearDown....')

if __name__ == '__main__':
    unittest.main()
