from selenium.webdriver import Remote
import time

# 定义node_hub与浏览器对应关系
nodes = {
    'http://192.168.199.1:4444/wd/hub': 'chrome'
    #'http://127.0.0.1:5556/wd/hub': 'safari',
    #'http://127.0.0.1:5557/wd/hub': 'firefox'
}

# 通过不同的浏览器执行测试脚本
for host, browser in nodes.items():
    print(host, browser)
    # 调用remote方法
    driver = Remote(command_executor=host,
                    desired_capabilities={'platform': 'WIN10', 'browserName': browser, 'version': '',
                                          'javascriptEnabled': True})

    # 打开百度首页并搜索词语，最后判断搜索跳转页面标题是否含有搜索词
    wd = 'selenium'
    driver.get('https://www.baidu.com')
    driver.find_element_by_id("kw").send_keys(wd)
    driver.find_element_by_id("su").click()
    time.sleep(1)
    assert wd in driver.title, '{0} not in {1}'.format(wd, driver.title.encode('utf-8'))
    # driver.quit()