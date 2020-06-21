import pytest
from base.webdriverfactory import WebDriverFactory
from pages.home.login import LoginPage

@pytest.fixture(scope="class")
def setup(request, browser):
    wdf = WebDriverFactory(browser)
    driver = wdf.getwebdriverinstance()
    lp = LoginPage(driver)
    lp.login("test@email.com", "abcabc")

    print("I will run only at first method")
    # if browser == 'firefox':
    #     print("running firefox")

    # if browser == 'chrome':
    #     baseURL = "https://letskodeit.teachable.com/"
    #     driver = webdriver.Chrome(executable_path="C:\\Selenium\\chromedriver.exe")
    #     driver.maximize_window()
    #     driver.implicitly_wait(5)
    #     driver.get(baseURL)
    #     print('running chrome')
    #
    # else:
    #     driver = webdriver.firefox
    #     print('not a valid browser')

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("I will run at last ")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")

# @pytest.yield_fixture(scope="module")
# def oneTimeSetUp(browser, osType):
#     print("Running one time setUp")
#     if browser == 'firefox':
#         print("Running tests on FF")
#     else:
#         print("Running tests on chrome")
#     yield
#     print("Running one time tearDown")
#
# def pytest_addoption(parser):
#     parser.addoption("--browser")
#     parser.addoption("--osType", help="Type of operating system")
#
# @pytest.fixture(scope="session")
# def browser(request):
#     return request.config.getoption("--browser")
#
# @pytest.fixture(scope="session")
# def osType(request):
#     return request.config.getoption("--osType")



