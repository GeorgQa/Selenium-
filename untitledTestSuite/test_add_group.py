# -*- coding: utf-8 -*-
import unittest

from lib.base_case import BaseCase
from selenium import webdriver
from selenium.common.exceptions import (NoAlertPresentException,
                                        NoSuchElementException)
from selenium.webdriver.common.by import By


class TestAddGroup():
    def setup_method(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    def test_add_group(self):
        wd = self.wd
        BaseCase.open_home_page(wd)
        BaseCase.login(wd)
        self.create_group(wd)
        self.filling_in_group_data(wd, "new_group", "Header", "vtgtr")
        self.save_and_end(wd)

    def test_no_data_group(self):
        wd = self.wd
        BaseCase.open_home_page(wd)
        BaseCase.login(wd)
        self.create_group(wd)
        self.filling_in_group_data(wd, " ", " ", " ")
        self.save_and_end(wd)

        # Сохранение и выход
    def save_and_end(self, wd):
        wd.find_element(By.NAME, "submit").click()
        wd.find_element(By.LINK_TEXT, "groups").click()
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def filling_in_group_data(self, wd, name, header, fouther):
        # Заполнение данных группы
        wd.find_element(By.NAME, "group_name").send_keys(name)
        wd.find_element(By.NAME, "group_header").send_keys(header)
        wd.find_element(By.NAME, "group_footer").send_keys(fouther)

    def create_group(self, wd):
        # Создание группы
        wd.find_element(By.LINK_TEXT, "groups").click()
        wd.find_element(By.NAME, "new").click()

    # def login(self, wd, username = "admin", password =  "secret"):
    #     # Логин
    #     wd.find_element(By.NAME, "user").click()
    #     wd.find_element(By.NAME, "user").clear()
    #     wd.find_element(By.NAME, "user").send_keys(username)
    #     wd.find_element(By.NAME, "pass").click()
    #     wd.find_element(By.NAME, "pass").clear()
    #     wd.find_element(By.NAME, "pass").send_keys(password)
    #     wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
