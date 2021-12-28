from src.testproject.sdk.drivers import webdriver

def test_create_a_chrome_driver_instance():
    driver = webdriver.Chrome(token='FswaKyEYeFDewuAywiPWCBnvkR-WFrosjGNd7YmQXL41')
    # Your test code goes here
    driver.quit()