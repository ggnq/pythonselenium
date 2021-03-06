from src.testproject.sdk.drivers import webdriver


def simple_test():
    driver = webdriver.Chrome(token='FswaKyEYeFDewuAywiPWCBnvkR-WFrosjGNd7YmQXL41')
    driver.get("https://example.testproject.io/web/")

    driver.find_element_by_css_selector("#name").send_keys("John Smith")
    driver.find_element_by_css_selector("#password").send_keys("12345")
    driver.find_element_by_css_selector("#login").click()

    passed = driver.find_element_by_css_selector("#logout").is_displayed()

    print("Test passed") if passed else print("Test failed")

    driver.quit()


if __name__ == "__main__":
    simple_test()