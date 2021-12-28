import time

from selenium import webdriver
from PIL import Image
from time import sleep
import pytesseract

def test1():
    browser = webdriver.Chrome()
    browser.get("http://localhost:8080/jpress/user/login")
    browser.maximize_window()

    sleep(2)
    #获取验证码图片
    t = time.time()
    picture_name1 = str(t)+'.png'
    browser.save_screenshot(picture_name1)

    ce = browser.find_element_by_id("captcha-img")
    print(ce.location)
    left = ce.location['x']
    top = ce.location['y']
    right = ce.size['width'] + left
    height = ce.size['height'] + top
    sleep(2)
    im = Image.open(picture_name1)
    #抠图
    img = im.crop((left, top, right, height))

    t = time.time()
    picture_name2 = str(t)+'.png'

    img.save(picture_name2)
    browser.close()


def test2():
    image1 = Image.open('图片路径')
    str = pytesseract.image_to_string(image1)

