import pickle
import random
import string
import time
import logging
import logging.handlers
import datetime


from PIL import Image
from selenium import webdriver
import os

#识别验证码
def get_code(drive,id):

    t = time.time()
    path = os.path.dirname(os.path.dirname(__file__)) + '\\screenshots'
    picture_name1 = path + '\\' + str(t) + '.png'

    drive.save_screenshot(picture_name1)

    ce = drive.find_element_by_id(id)

    left = ce.location['x']
    top = ce.location['y']
    right = ce.size['width'] + left
    height = ce.size['height'] + top

    dpr = drive.execute_script('return window.devicePixelRatio')
    print(dpr)

    im = Image.open(picture_name1)
    img = im.crop((left, top, right, height))

    t = time.time()

    picture_name2 = path + '\\' + str(t) + '.png'
    img.save(picture_name2)

    from selenium import webdriver
    from ShowapiRequest import ShowapiRequest
    from PIL import Image

    # python3.6.5
    # 需要引入requests包 ：运行终端->进入python/Scripts ->输入：pip install requests

    r = ShowapiRequest("http://route.showapi.com/184-4", "showapi_appid", "showapi_sign")

    r.addFilePara("image", "验证图片路径")
    r.addBodyPara("typeId", "14")
    r.addBodyPara("convert_to_jpg", "0")
    r.addBodyPara("needMorePrecise", "0")
    res = r.post()
    text = res.json()["showapi_res_body"]
    code = text["Result"]
    return code

def get_logger():
    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG)

    rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7,
                                                           atTime=datetime.time(0, 0, 0, 0))
    rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

    f_handler = logging.FileHandler('error.log')
    f_handler.setLevel(logging.ERROR)
    f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

    logger.addHandler(rf_handler)
    logger.addHandler(f_handler)
    return logger


#生成随机字符串
def gen_random_str():
    rand_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    return rand_str

#保存cookie
def save_cookie(driver, path):
    with open(path, 'wb') as filehandler:
        cookies = driver.get_cookies()
        print(cookies)
        pickle.dump(cookies, filehandler)


#加载cookie
def load_cookie(driver, path):
    with open(path, 'rb') as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            driver.add_cookie(cookie)




