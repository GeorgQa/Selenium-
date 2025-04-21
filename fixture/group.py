from selenium.webdriver.common.by import By

from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "groups").click()

    def create(self):
        # Создание группы
        wd = self.app.wd
        self.open_group_page()
        wd.find_element(By.NAME, "new").click()

    def filling_in_group_data(self, group):
        # Заполнение данных группы
        wd = self.app.wd
        self.check_fill_value("group_name", group.name)
        self.check_fill_value("group_header", group.header)
        self.check_fill_value("group_footer", group.footer)

    def check_fill_value(self, filed_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, filed_name).click()
            wd.find_element(By.NAME, filed_name).clear()
            wd.find_element(By.NAME, filed_name).send_keys(text)

    def save(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "submit").click()
        wd.find_element(By.LINK_TEXT, "group page").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        wd.find_element(By.NAME, "delete").click()
        wd.find_element(By.LINK_TEXT, "group page").click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()


    def modify_first_group(self,new_group_data):
        wd = self.app.wd
        self.open_group_page()
        if self.count() == 0:
            self.create(Group(name="test"))
        self.select_first_group()
        wd.find_element(By.NAME, "edit").click()
        self.filling_in_group_data(new_group_data)
        wd.find_element(By.NAME, "update").click()
        wd.find_element(By.LINK_TEXT, "group page").click()

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        count_elements = wd.find_elements(By.NAME, "selected[]")
        elements_count = len(count_elements)
