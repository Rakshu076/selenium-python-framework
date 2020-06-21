from selenium import webdriver
import os
import time
class WebDriverFactory:

    def __init__(self, browser):
        self.browser = browser

    def getwebdriverinstance(self):
        driver = None
        baseURL = "https://letskodeit.teachable.com/"

        if self.browser == 'chrome':

            chromedriver = "C:\\Selenium\\chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = chromedriver
            driver = webdriver.Chrome(chromedriver)

        elif self.browser == 'firefox':
            driver = webdriver.Firefox()

        else:
            print("enter valid brower")

        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        time.sleep(2)
        return driver
