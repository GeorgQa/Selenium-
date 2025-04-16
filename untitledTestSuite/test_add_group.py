# -*- coding: utf-8 -*-
import unittest
import pytest

from lib.base_case import BaseCase
from selenium import webdriver
from selenium.common.exceptions import (NoAlertPresentException,
                                        NoSuchElementException)

from lib.session import SessionHelper


@pytest.fixture(scope="session")
def b_case(request):
    fixture  = BaseCase()
    request.add.finaluzer(fixture.destroy)
    return fixture



class TestAddGroup():
    def setup_method(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)

    def test_add_group(self):
        wd = self.wd
        BaseCase.open_home_page()
        SessionHelper.login()
        BaseCase.create()
        BaseCase.filling_in_group_data( "new_group", "Header", "vtgtr")
        BaseCase.save_and_exit()
        SessionHelper.Logout()

    def test_no_data_group(self):
        wd = self.wd
        BaseCase.open_home_page()
        SessionHelper.login()
        BaseCase.create()
        BaseCase.filling_in_group_data( " ", " ", " ")
        BaseCase.save_and_exit()
        SessionHelper.Logout()

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


if __name__ == "__main__":
    unittest.main()
