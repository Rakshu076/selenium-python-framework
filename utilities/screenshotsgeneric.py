

from selenium import webdriver
import time


class screenshots:

    def __init__(self, driver):
        self.driver = driver

    def TakeScreenshots(self):
        try:
            RandomNumber = str(round(time.time() * 1000)) + ".png"
            Directory = "C:\\Users\\RA20072908\\Desktop\\screenshots\\"
            Destination = Directory + RandomNumber

            self.driver.save_screenshot(Destination)
        except NotADirectoryError:
            print("Directory not found for screenshots")

