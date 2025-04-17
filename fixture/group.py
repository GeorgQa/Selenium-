from selenium.webdriver.common.by import By


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "groups").click()

    def create(self):
        # Создание группы
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "groups").click()
        wd.find_element(By.NAME, "new").click()

    def filling_in_group_data(self, name, header, fouther):
        # Заполнение данных группы
        wd = self.app.wd
        wd.find_element(By.NAME, "group_name").send_keys(name)
        wd.find_element(By.NAME, "group_header").send_keys(header)
        wd.find_element(By.NAME, "group_footer").send_keys(fouther)

    def save(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "submit").click()
        wd.find_element(By.LINK_TEXT, "group page").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        #select
        wd.find_element(By.NAME, "selected[]").click()
        #delete
        wd.find_element(By.NAME, "delete").click()
        wd.find_element(By.LINK_TEXT, "group page").click()