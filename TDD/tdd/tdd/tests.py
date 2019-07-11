from django.test import LiveServerTestCase
from selenium import webdriver


class StudentTestCase(LiveServerTestCase):
    def test_student_find_solos(self):
        self.fail('Incomplete Test')

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()
