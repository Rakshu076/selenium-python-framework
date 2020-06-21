import pytest
import unittest
from pages.Courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
from ddt import unpack, ddt, data
import time
from utilities.readcsvdata import getcsvdata

@pytest.mark.usefixtures("setup")
@ddt
class TestCoursesEnroll(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classsetup(self, setup):
        self.rcp = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @data(*getcsvdata("C:\\Users\\RA20072908\\PycharmProjects\\letskodeit\\dataset.csv"))
    @unpack
    def test_courselink(self, coursename, cardnumber, exp, cvv, postal):
        self.rcp.enrollcourse(coursename, cardnumber, exp, cvv, postal)
        result = self.rcp.enrollfail()
        self.ts.markfinal("course enroll verify", result, "enroll verified")
        self.rcp.scrollup()
        time.sleep(2)
        self.rcp.logo_click()
        time.sleep(3)










