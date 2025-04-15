
from selenium.webdriver.common.by import By


class BaseCase:

        @staticmethod
        def open_home_page(self):
            # Открытие основной страницы
            wd = self.wd
            wd.get("http://localhost/addressbook/")

        @staticmethod
        def open_group_page(self):
            wd = self.wd
            wd.find_element(By.LINK_TEXT, "groups").click()

        @staticmethod
        def create(self):
            # Создание группы
            wd = self.wd
            wd.find_element(By.LINK_TEXT, "groups").click()
            wd.find_element(By.NAME, "new").click()

        @staticmethod
        def filling_in_group_data(self,  name, header, fouther):
            # Заполнение данных группы
            wd = self.wd
            wd.find_element(By.NAME, "group_name").send_keys(name)
            wd.find_element(By.NAME, "group_header").send_keys(header)
            wd.find_element(By.NAME, "group_footer").send_keys(fouther)


        @staticmethod
        def save_and_exit(self):
            wd = self.wd
            wd.find_element(By.NAME, "submit").click()
            wd.find_element(By.LINK_TEXT, "groups").click()

        @staticmethod
        def destroy(self):
            self.wd.quit()

        @staticmethod
        def delete_first_group(self):
            wd = self.wd
            self.open_group_page()
            #select
            wd.find_element(By.NAME, "selected[]").click()
            #delete
            wd.find_element(By.NAME, "delete").click()