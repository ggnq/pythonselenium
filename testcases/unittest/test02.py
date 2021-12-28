import unittest
from selenium import webdriver

class MyTestcase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass')
        cls.drive = webdriver.Chrome()
        cls.drive.get('http://baidu.com')
        cls.drive.maximize_window()



    def test01(self):

        self.drive.find_element_by_id('kw').send_keys('selenium')
        print('test01')


    def test02(self):
        print('test02')
        self.assertEqual(1, 1)
        self.assertIn(1, [1, 2, 3])



    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')
        cls.drive.quit()


if __name__ == '__main__':
    unittest.main()
