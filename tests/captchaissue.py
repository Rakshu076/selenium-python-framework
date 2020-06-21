from selenium import webdriver
import time

opt = webdriver.ChromeOptions()
opt.add_argument("user-data-dir=C:\\Users\\RA20072908\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
driver = webdriver.Chrome(options=opt)
driver.maximize_window()
driver.implicitly_wait(10)
