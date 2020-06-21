from base.basepage import BasePage
import time


class RegisterCoursesPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super(RegisterCoursesPage, self).__init__(driver)

    #locators
    _MyCourses = "//a[contains(text(), 'My Courses')]"
    _AllCourses = "//a[contains(text(), 'All Courses')]"
    _CourseSearchBox = "search-courses"
    _CourseSearchBtn = "search-course-button"
    _courselink = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
    _enrollincoursebtn = "enroll-button-top"
    _cardnumberbox = "//div[@class='CardNumberField-input-wrapper']//span[@data-max='4242 4242 4242 4242 4240']/input"
    _expirationdatefield = "//span[@data-max='MM / YY0']/input"
    _CvcCode = "//span[@data-max='00000']/input"
    _postalCode = "//span[@data-max='902100']/input"
    _agreecheckbox = "agreed_to_terms_checkbox"
    _submitButton = "confirm-purchase"
    _textverify = "//div[@id='block-568987']//h1[contains(text(),'JavaScript for beginners')]"
    _logoclick = "//a[@class='navbar-brand header-logo']"

    def coursesearchbox(self, coursename):
        self.sendkeys(coursename, "id", self._CourseSearchBox)

    def coursesearchbtn(self):
        self.elementclick("id", self._CourseSearchBtn)

    def javacourseclick(self):
        self.elementclick("xpath", self._courselink)

    def selectcoursetoenroll(self, fullcoursename):
        self.elementclick("xpath", self._courselink.format(fullcoursename))

    def enrollcoursebtn(self):
        self.elementclick("id", self._enrollincoursebtn)

    def scrolldown(self):
        self.driver.execute_script("window.scrollBy(0, 800);")

    def scrollup(self):
        self.driver.execute_script("window.scrollBy(0, -900);")

    def allcourses(self):
        self.elementclick("xpath", self._AllCourses)

    def logo_click(self):
        self.elementclick("xpath", self._logoclick)

    def cardnumber(self, number):
        self.driver.switch_to.frame(0)
        self.sendkeys(number, "xpath", self._cardnumberbox)
        self.driver.switch_to.default_content()
        #"__privateStripeFrame16"

    def expirationfield(self, expirydate):
        self.driver.switch_to.frame(1)
        self.sendkeys(expirydate, "xpath", self._expirationdatefield)
        self.driver.switch_to.default_content()

    def cvc(self, cvccode):
        self.driver.switch_to.frame(2)
        self.sendkeys(cvccode, "xpath", self._CvcCode)
        self.driver.switch_to.default_content()

    def postalcode(self, postalcode):
        self.driver.switch_to.frame(3)
        self.sendkeys(postalcode, "xpath", self._postalCode)
        self.driver.switch_to.default_content()

    def agreeclick(self):
        self.elementclick("id", self._agreecheckbox)

    def enrollincourse(self):
        self.elementclick("id", self._submitButton)

    def Coursetextverify(self):
        self.iselementpresent("xpath", self._textverify)

    def coursesearchclick(self, coursename):
        self.coursesearchbox(coursename)
        self.coursesearchbtn()
        self.selectcoursetoenroll(coursename)
        self.Coursetextverify()
        self.enrollcoursebtn()

    def entercreditcardinfo(self, num, exp, cvc, postalcode):
        self.cardnumber(num)
        self.expirationfield(exp)
        self.cvc(cvc)
        self.postalcode(postalcode)
        self.agreeclick()

    def enrollcourse(self, coursename, num, exp, cvc, postalcode):
        self.coursesearchclick(coursename)
        self.scrolldown()
        time.sleep(3)
        self.entercreditcardinfo(num, exp, cvc, postalcode)

    def attributevalue(self):
        element = self.get_element("id", self._submitButton)
        value = element.get_attribute('class')
        enabled = "is-disabled" in value
        return enabled

    def enrollfail(self):
        result = self.attributevalue()
        if result:
            print("enroll is failed")
        else:
            print("enroll is successfull")
        return result

















