# -*- coding: utf-8 -*-
import unittest
import pytest
from selenium.webdriver.common.by import By

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
        # self.session = SessionHelper(self)

    def logout(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def login(self):
        wd = self.wd
        wd.find_element(By.NAME, "user").send_keys("admin")
        wd.find_element(By.NAME, "pass").send_keys("secret")
        wd.find_element(By.ID, "LoginForm").submit()

    def open_home_page(self):
        # Открытие основной страницы
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def test_add_group(self):
        self.open_home_page()
        self.login()
        self.create_group()
        self.filling_in_group_data( "new_group", "Header", "vtgtr")
        self.save()
        self.logout()
        self.wd.quit()

    def test_no_data_group(self):
        wd = self.wd
        self.open_home_page()
        self.login()
        self.create_group()
        self.filling_in_group_data( " ", " ", " ")
        self.save()
        self.logout()
        self.wd.quit()

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

    def open_group_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "groups").click()


    def create_group(self):
        # Создание группы
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "groups").click()
        wd.find_element(By.NAME, "new").click()


    def filling_in_group_data(self, name, header, fouther):
        # Заполнение данных группы
        wd = self.wd
        wd.find_element(By.NAME, "group_name").send_keys(name)
        wd.find_element(By.NAME, "group_header").send_keys(header)
        wd.find_element(By.NAME, "group_footer").send_keys(fouther)


    def save(self):
        wd = self.wd
        wd.find_element(By.NAME, "submit").click()
        wd.find_element(By.LINK_TEXT, "groups").click()


    def destroy(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
