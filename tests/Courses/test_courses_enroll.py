import pytest
import unittest
from pages.Courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus

@pytest.mark.usefixtures("setup")
class TestCoursesEnroll(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classsetup(self, setup):
        self.rcp = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    def test_courselink(self):
        self.rcp.enrollcourse("javascript", "12345678", "22/22", "329", "577301")
        result = self.rcp.enrollfail()
        self.ts.markfinal("course enroll verify", result, "enroll verified")








