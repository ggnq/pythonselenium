from selenium import webdriver
from selenium.webdriver.common.by import By
from testcases.pom.BasePage import BasePage
from time import sleep

class SearchPage(BasePage):
    seaech_input = (By.ID, u'kw')
    seaech_btn = (By.ID, u'su')

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def goto_baidu_home(self):
        self.driver.get('http://www.baidu.com')
        self.driver.maximize_window()

    def input_kw(self):
        self.type_text('selenium', *self.seaech_input)

    def click_search_btn(self):
        self.click(*self.seaech_btn)
        sleep(2)