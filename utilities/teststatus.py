
from base.basepage import BasePage

class TestStatus(BasePage):

    def __init__(self, driver):
        self.resultlist = []
        self.driver = driver
        super(TestStatus, self).__init__(driver)

    # def __init__(self, driver):
    #     super(TestStatus, self).__init__(driver)

    def setresult(self, result, resultmessage):
        try:
            if result is not None:
                if result:
                    self.resultlist.append("pass")
                    self.log.info("### Verification successfull " + resultmessage)
                else:
                    self.resultlist.append("fail")
                    self.log.error("### Verification failed " + resultmessage)
                    self.screenshot(resultmessage)
            else:
                self.resultlist.append("fail")
                self.log.error("### Verification failed " + resultmessage)
                self.screenshot(resultmessage)
        except:
            self.resultlist.append("fail")
            self.log.error("### Exception occured " + resultmessage)
            self.screenshot(resultmessage)

    def mark(self, result, resultmessage):
        self.setresult(result, resultmessage)

    def markfinal(self, testname, result, resultmessage):

        self.setresult(result, resultmessage)

        if "fail" in self.resultlist:
            self.log.error(testname + "##Test failed")
            self.resultlist.clear()
            assert True == False

        else:
            self.log.info(testname + "## Test Pass")
            assert True == True

