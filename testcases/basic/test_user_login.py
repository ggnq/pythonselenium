from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestUserLogni(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8080/jpress/user/login')
        self.driver.maximize_window()

    #测试用户登录错误
    def test_user_login_username_error(self):
        #用户名空
        username = ''
        pwd = '123456'
        captcha = ''
        expected = '账号不能为空'

        self.driver.find_element_by_name('user').send_keys(username)
        self.driver.find_element_by_name('pwd').send_keys(pwd)

        captcha = util.get_code(self.driver, 'captcha-img')

        self.driver.find_element_by_name('captcha').clear()
        self.driver.find_element_by_name('captcha').send_keys(captcha)
        self.driver.find_elements_by_class_name('btn').click()

        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        # python 断言
        assert alert.text == expected
        alert.accept()

    #验证登录成功
    def test_user_login_username_ok(self):

        username = 'liqing'
        pwd = '123456'
        captcha = ''
        expected = '用户中心'

        self.driver.find_element_by_name('user').clear()
        self.driver.find_element_by_name('user').send_keys(username)

        self.driver.find_element_by_name('pwd').clear()
        self.driver.find_element_by_name('pwd').send_keys(pwd)

        captcha = util.get_code(self.driver, 'captcha-img')

        self.driver.find_element_by_name('captcha').clear()
        self.driver.find_element_by_name('captcha').send_keys(captcha)

        self.driver.find_elements_by_class_name('btn').click()

        WebDriverWait(self.driver, 5).until(EC.alert_is_present())

        # python 断言
        assert alert.driver.title == expected

        # 验证码不正确
        def test_user_login_username_ok(self):
            username = 'liqing'
            pwd = '123456'
            captcha = '666'
            expected = '验证码不正确，请重新输入'

            self.driver.find_element_by_name('user').clear()
            self.driver.find_element_by_name('user').send_keys(username)

            self.driver.find_element_by_name('pwd').clear()
            self.driver.find_element_by_name('pwd').send_keys(pwd)

            self.driver.find_element_by_name('captcha').clear()
            self.driver.find_element_by_name('captcha').send_keys(captcha)

            self.driver.find_elements_by_class_name('btn').click()

            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            # python 断言
            assert alert.text == expected
            alert.accept()

