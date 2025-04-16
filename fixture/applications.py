from selenium import webdriver
from selenium.webdriver.common.by import By

from fixture.session import SessionHelper


class Applications:


        def __init__(self):
            self.Session = None
            self.wd = webdriver.Chrome()
            self.wd.implicitly_wait(60)
            self.session = SessionHelper(self)

        # def logout(self):
        #     wd = self.wd
        #     wd.find_element(By.LINK_TEXT, "Logout").click()

        # def login(self):
        #     wd = self.wd
        #     wd.find_element(By.NAME, "user").send_keys("admin")
        #     wd.find_element(By.NAME, "pass").send_keys("secret")
        #     wd.find_element(By.ID, "LoginForm").submit()

        def open_home_page(self):
            # Открытие основной страницы
            wd = self.wd
            wd.get("http://localhost/addressbook/")


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
