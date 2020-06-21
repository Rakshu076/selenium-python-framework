from tests.Courses.test_multiplecourses_enroll import TestCoursesEnroll
from tests.home.login_tests import LoginTests
import unittest


tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestCoursesEnroll)

testsuite = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner().run(testsuite)


