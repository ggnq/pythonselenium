from selenium import webdriver

chrome_capabilities = {
    "browserName": "chrome",  #浏览器名称
    "version": "",               #浏览器版本
    "platform": "WIN10",           #平台 windows、linux、andriod/ANY
    "javascriptEnabled": True,   #是否启用js
}


driver = webdriver.Remote("http://localhost:4444/wd/hub", desired_capabilities=chrome_capabilities)
driver.get("http://www.baidu.com")
print(driver.title)