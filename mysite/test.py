from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class Hosttest(LiveServerTestCase):

    def testloginpage(self):
        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000/sign')
        user_email = driver.find_element("name", "lemail")
        user_password = driver.find_element("name", "lpass")
        login = driver.find_element("name", "login")

        user_email.send_keys("amanpandey9038@gmail.com")
        user_password.send_keys("Aman123")

        login.send_keys(Keys.RETURN)
        assert 'Aman Pandey' in driver.page_source