

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import (NoAlertPresentException,
                                        NoSuchElementException)

from lib.session import SessionHelper


class TestAddGroup():
    def setup_method(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)

    def delete_first_group(self):
        wd = self.wd
        self.BaseCase.open_home_page()
        # select
        wd.find_element(By.NAME, "selected[]").click()
        # delete
        wd.find_element(By.NAME, "delete").click()
        wd.find_element(By.NAME,  "group page").click()

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True


    def tearDown(self):
        self.BaseCase.destroy()
