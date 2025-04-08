# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from selenium.webdriver.common.by import By
from lib.base_case import BaseCase
from faker import Faker

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def test_add_contact(self):
        #вызов драйвера
        wd = self.driver
        #Переход на Url для авторизации
        BaseCase.open_home_page(wd)
        #Авторизация
        BaseCase.login(wd)
        #Дейстивия с формой
        self.filling_out_form(wd, "Имя_имя", "Тест_фамилия", "Иванов", "Тестовый ник", "Тестовая компания")
        #Сохранение и выход
        self.save_and_end(wd)

    def test_add_contact_random(self):
        fake = Faker("ru_Ru")
        wd = self.driver
        BaseCase.open_home_page(wd)
        BaseCase.login(wd)
        self.filling_out_form(wd, firstName=fake.first_name(),   middleName=fake.middle_name(), lastName= fake.last_name() , nick_name="Тестовый ник", company= fake.company())


        self.save_and_end(wd)


    def filling_out_form(self, wd, firstName, middleName, lastName, nick_name, company, group_add="Test_test_ran_123"):
        wd.find_element(By.LINK_TEXT, "add new").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys(firstName)
        wd.find_element(By.NAME, "middlename").clear()
        wd.find_element(By.NAME, "middlename").send_keys(middleName)
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys(lastName)
        wd.find_element(By.NAME, "nickname").clear()
        wd.find_element(By.NAME, "nickname").send_keys(nick_name)
        wd.find_element(By.NAME, "bday").click()
        wd.find_element(By.NAME, "bday").send_keys("16")
        wd.find_element(By.NAME, "bmonth").click()
        wd.find_element(By.NAME, "bmonth").send_keys("December")
        wd.find_element(By.NAME, "byear").click()
        wd.find_element(By.NAME, "byear").send_keys("2001")
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").send_keys(company)
        wd.find_element(By.NAME, "aday").click()
        wd.find_element(By.NAME, "aday").send_keys("20")
        wd.find_element(By.NAME, "amonth").click()
        wd.find_element(By.NAME, "amonth").send_keys("July")
        wd.find_element(By.NAME, "ayear").click()
        wd.find_element(By.NAME, "ayear").send_keys("2020")
        wd.find_element(By.NAME, "new_group").click()
        wd.find_element(By.NAME, "new_group").send_keys(group_add)

    def save_and_end(self, wd):
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
