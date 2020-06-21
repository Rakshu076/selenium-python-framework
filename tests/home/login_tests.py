
from pages.home.login import LoginPage
import unittest
import pytest
from utilities.teststatus import TestStatus

@pytest.mark.usefixtures("setup")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classsetup(self, setup):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_validlogin(self):
        #self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verifytitle()
        self.ts.mark(result1, "Title verified")
        result2 = self.lp.verifyloginsuccessfull()
        self.ts.markfinal("test_validlogin", result2, "logging in verified")
        self.driver.quit()

    # def test_invalidlogin(self):
    #     self.lp.login("test@email.com", "abcabcabc")
    #     result = self.lp.loginfailed()
    #     assert result == True

# if __name__ == '__main__':
#     unittest.main()