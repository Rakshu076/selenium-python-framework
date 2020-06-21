from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from traceback import print_stack
from utilities.customlogger import customlogger as cl
import logging.config
import time
import os


class SeleniumDriver:
    log = cl.customlogg(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def gettitle(self):
        return self.driver.title

    def screenshot(self, testname):
        filename = testname + "." + str(round(time.time() * 1000)) + ".png"
        screenshotdir = "..\\screenshots\\"
        relativefilename = screenshotdir + filename
        currentdir = os.path.dirname(__file__)
        destinationfile = os.path.join(currentdir, relativefilename)
        destinationdir = os.path.join(currentdir, screenshotdir)

        try:
            if not os.path.exists(destinationdir):
                os.makedirs(destinationdir)

            self.driver.save_screenshot(destinationfile)
            self.log.info("screenshot saved in directory " + destinationdir)

        except:
            self.log.error("Directory not avaiable")

    def getbytype(self, locatortype):
        locatortype = locatortype.lower()
        if locatortype == "id":
            return By.ID
        elif locatortype == "xpath":
            return By.XPATH
        elif locatortype == "name":
            return By.NAME
        elif locatortype == "link":
            return By.LINK_TEXT
        elif locatortype == "class":
            return By.CLASS_NAME
        else:
            self.log.info('locatortype is  not valid')

    def get_element(self, locatortype, locator):
        try:
            element = None
            locatortype = locatortype.lower()
            getype = self.getbytype(locatortype)
            element = self.driver.find_element(getype, locator)
            self.log.info('element found with locator : ' + locator + ' and locatortype :' + locatortype)
            return element
        except:
            self.log.info('Element not found')
            print_stack()

    def get_elements(self, locatortype, locator):

        element = None
        locatortype = locatortype.lower()
        getype = self.getbytype(locatortype)
        element = self.driver.find_elements(getype, locator)
        self.log.info('elements found with locator : ' + locator + ' and locatortype :' + locatortype)
        return list(element)

    def elementclick(self, locatortype, locator):
        try:
            element = self.get_element(locatortype, locator)
            element.click()
            self.log.info("clicked on element with locator : " + locator + " and locatorType :" + locatortype)
        except:
            self.log.info("Cannot click on element with locator: " + locator + " and locatorType: " + locatortype)
            print_stack()

    def sendkeys(self, data, locatortype, locator):
        try:
            element = self.get_element(locatortype, locator)
            element.send_keys(data)
            self.log.info("sent data on element with locator : " + locator + " and locatorType :" + locatortype)
        except:
            self.log.info("Cannot sent data on element with locator: " + locator + " and locatorType: " + locatortype)
            print_stack()

    def iselementpresent(self, locatortype, locator):

        try:
            element = self.get_element(locatortype, locator)
            if element is not None:
                return True
            else:
                return False
        except:
            self.log.info('Element not found')
            return False

    def waitforelement(self, locator, locatortype, timeout=25, pollfrequency=1):
        element = None
        bytype = self.getbytype(locatortype)
        try:
            wait = WebDriverWait(self.driver, timeout, pollfrequency, ignored_exceptions={NoSuchElementException,
                                                                                          ElementNotVisibleException})
            element = wait.until(EC.element_to_be_clickable((bytype, locator)))
        except:
            self.log.info('element not available')
        return element
