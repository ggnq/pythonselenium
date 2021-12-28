
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
class TestArticle(object):
    def __init__(self, login):
        self.login = login

    #测试添加文章
    def test_add_ok(self):
        title = '我的文章'
        content = '我的文章内容'
        ecpected = '文章保存成功'

        self.login.driver.find_element_by_xpath().click()
        sleep(1)
        self.login.driver.find_element_by_xpath().click()
        sleep(1)
        self.login.driver.find_element_by_xpath().click()
        sleep(1)

        self.login.driver.find_element_by_id('articie-title').send_keys(title)
        #切入iframe
        frame1 = self.login.driver.find_element_by_xpath()

        self.login.driver.switch_to.default_content(frame1)
        sleep(1)

        self.login.driver.find_element_by_xpath().send_keys(content)
        #切出iframe
        self.login.driver.switch_to.default_content()

        self.login.driver.find_element_by_xpath().click()

        loc = (By.CLASS_NAME, 'toast-message')

        WebDriverWait(self.login.driver, 5).until(EC.visibility_of_element_located(loc))

        mag = self.login.driver.find_element(*loc).text

        assert msg == ecpected

    # 测试删除一个文章
    def test_delete_one_article_ok(self):

        self.login.driver.find_element_by_xpath().click()
        sleep(1)
        self.login.driver.find_element_by_xpath().click()
        sleep(1)

        link = self.login.driver.find_element_by_xpath()
        ActionChains(self.login.driver).move_to_element(link).perform()

        sleep(1)
        article_num = len(self.login.driver.find_element_by_class_name('jp-actiontr'))

        del_elem = self.login.driver.find_element_by_xpath()
        del_elem.click()

        sleep(1)

        article_num2 = len(self.login.driver.find_element_by_class_name('jp-actiontr'))

        assert article_num == article_num2 + 1

    #删除所有文章
    def test_delete_all_article_ok(self):
        self.login.driver.find_element_by_xpath().click()
        sleep(1)
        self.login.driver.find_element_by_xpath().click()
        sleep(1)

        link = self.login.driver.find_element_by_xpath()
        link.click()

        self.login.driver.find_element_by_id('batchDel').click()

        WebDriverWait(self.login.driver, 5).until(EC.alert_is_present())
        alert = self.login.driver.switch_to.alert
        alert.accept()

        sleep(1)

        artile_num = self.login.driver.find_element_by_class_name('jp-actiontr')
        assert len(artile_num) == 0