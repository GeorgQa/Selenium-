
from selenium.webdriver.common.by import By


class BaseCase:
        @staticmethod
        def login(wd):
            wd.find_element(By.NAME, "user").send_keys("admin")
            wd.find_element(By.NAME, "pass").send_keys("secret")
            wd.find_element(By.ID, "LoginForm").submit()

        @staticmethod
        def open_home_page(wd):
            # Открытие основной страницы
            wd.get("http://localhost/addressbook/")
