from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from util import util
import pytest

class TestUserRegister(object):
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8080/jpress/user/register')
        self.driver.maximize_window()
        self.logger = util.get_logger()

    #测试登录验证码错误
    def test_register_code_error(self):
        username = 'test001'
        email = 'test001@qq.com'
        pwd = '123456'
        confirmPwd = '123456'
        captcha '666'
        expected = '验证码不正确'

        self.driver.find_element_by_name('username').send_keys(username)
        self.logger.debug('输入用户名称：%s', username)
        self.driver.find_element_by_name('email').send_keys(email)
        self.logger.debug('输入邮箱：%s', email)

        self.driver.find_element_by_name('pwd').send_keys(pwd)
        self.logger.debug('输入密码：%s', pwd)
        self.driver.find_element_by_name('confirmPwd').send_keys(confirmPwd)
        self.logger.debug('二次输入密码：%s', confirmPwd)

        self.driver.find_element_by_name('captcha').send_keys(captcha)
        self.logger.debug('输入验证码：%s', captcha)
        self.driver.find_elements_by_class_name('btn').click()
        self.logger.debug('点击注册')

        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        #python 断言
        try:
            assert alert.text == expected
        except AssertionError as ae:
            self.logger.error("提示：%s", "报错了", exc_info=1)

        alert.accept()

        sleep(5)


    #测试成功
    def test_register_ok(self):
        username = util.gen_random_str()
        email = username + '@qq.com'
        pwd = '123456'
        confirmPwd = '123456'

        #自动获取
        captcha = ''
        expected = '注册成功，点击确定进行登录。'

        self.driver.find_element_by_name('username').clear()
        self.driver.find_element_by_name('username').send_keys(username)
        self.logger.debug('输入用户名称：%s', username)

        self.driver.find_element_by_name('email').clear()
        self.driver.find_element_by_name('email').send_keys(email)
        self.logger.debug('输入邮箱：%s', email)

        self.driver.find_element_by_name('pwd').clear()
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        self.logger.debug('输入密码：%s', pwd)

        self.driver.find_element_by_name('confirmPwd').clear()
        self.driver.find_element_by_name('confirmPwd').send_keys(confirmPwd)
        self.logger.debug('二次输入密码：%s', confirmPwd)
        #在线API识别验证码
        captcha = util.get_code(self.driver, 'captcha-img')

        self.driver.find_element_by_name('captcha').clear()
        self.driver.find_element_by_name('captcha').send_keys(captcha)
        self.logger.debug('输入验证码：%s', captcha)

        self.driver.find_elements_by_class_name('btn').click()
        self.logger.debug('点击注册')

        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        # python 断言
        try:
            assert alert.text == expected
        except AssertionError as ae:
            self.logger.error("提示：%s", "报错了", exc_info=1)
        alert.accept()


if __name__ == '__main__':
    pytest.main(['test_user_register.py'])
