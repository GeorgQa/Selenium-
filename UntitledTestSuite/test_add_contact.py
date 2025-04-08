# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from selenium.webdriver.common.by import By
from lib.base_case import BaseCase

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    
    def test_add_contact(self):
        #вызов драйвера
        wd = self.driver
        #Переход на Url для авторизации
        wd.get("http://localhost/addressbook/")

        #Авторизация
        BaseCase.login(wd)

        #Добавление контакта
        wd.find_element(By.LINK_TEXT, "add new").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys("Тест_отчество")
        wd.find_element(By.NAME, "middlename").clear()
        wd.find_element(By.NAME, "middlename").send_keys("Тест_фамилия")
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys("Тест_имя")
        wd.find_element(By.NAME, "nickname").clear()
        wd.find_element(By.NAME, "nickname").send_keys("Тестовый_ник")
        wd.find_element(By.NAME, "bday").click()
        wd.find_element(By.NAME, "bday").send_keys("16")
        wd.find_element(By.NAME, "bmonth").click()
        wd.find_element(By.NAME, "bmonth").send_keys("December")
        wd.find_element(By.NAME, "byear").click()
        wd.find_element(By.NAME, "byear").send_keys("2001")
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").send_keys("Тестовая компания")
        wd.find_element(By.NAME, "aday").click()
        wd.find_element(By.NAME, "aday").send_keys("20")
        wd.find_element(By.NAME, "amonth").click()
        wd.find_element(By.NAME, "amonth").send_keys("July")
        wd.find_element(By.NAME, "ayear").click()
        wd.find_element(By.NAME, "ayear").send_keys("2020")
        wd.find_element(By.NAME, "new_group").click()
        wd.find_element(By.NAME, "new_group").send_keys("Test_test_ran_123")

        #Сохранение и выход

        wd.find_element(By.NAME, "submit").click()
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
