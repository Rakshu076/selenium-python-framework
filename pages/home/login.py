import time
import logging
from utilities.customlogger import customlogger as cl
from utilities.screenshotsgeneric import screenshots
from base.basepage import BasePage

class LoginPage(BasePage):
    log = cl.customlogg(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.screenshot = screenshots(driver)


    # Locators
    _login_link = "//div[@id='navbar']//a[contains(text(),'Login')]"
    _email_name = "user_email"
    _password = "user_password"
    _loginbtn = "//form[@id='new_user']//input[contains(@name,'commit')]"


    # def loginlink(self):
    #     return self.driver.find_element_by_xpath(self._login_link)
    #
    # def emailfield(self):
    #     return self.driver.find_element_by_id(self._email_name)
    #
    # def passwordfield(self):
    #     return self.driver.find_element_by_id(self._password)
    #
    # def loginbutton(self):
    #     return self.driver.find_element_by_xpath(self._loginbtn)

    def login_link_click(self):
        self.elementclick("xpath", self._login_link)

    def emailname(self, email):
        self.sendkeys(email, "id", self._email_name)


    def password_value(self, password):
        self.sendkeys(password, "id", self._password)

    def click_loginbtn(self):
        self.elementclick("xpath", self._loginbtn)

    # def click_homebtn(self):
    #     self.elementclick("xpath", self._homebtn)

    def login(self, email="", password=""):
        self.login_link_click()
        time.sleep(2)

        self.emailname(email)

        self.password_value(password)

        time.sleep(1)
        self.click_loginbtn()


    def verifyloginsuccessfull(self):
        result = self.iselementpresent("xpath", "//img[@alt='test@email.com']//following-sibling::span")
        # if result is True:
        #     self.log.info("Login Successfull")
        # else:
        #     self.log.info("login Failed")
        return result

    def loginfailed(self):
        result = self.iselementpresent("xpath", "//div[contains(text(),'Invalid email or password.')]")
        return result

    def verifytitle(self):
        return self.verifyPageTitle("Let's Kode it")
















