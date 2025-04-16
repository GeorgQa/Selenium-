from selenium import webdriver
from selenium.webdriver.common.by import By

from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Applications:


        def __init__(self):
            self.wd = webdriver.Chrome()
            self.wd.implicitly_wait(60)
            self.session = SessionHelper(self)
            self.group = GroupHelper(self)


        def open_home_page(self):
            # Открытие основной страницы
            wd = self.wd
            wd.get("http://localhost/addressbook/")



        def destroy(self):
            self.wd.quit()
