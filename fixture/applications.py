from selenium import webdriver

from fixture.contacts import Сontact
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Applications:


        def __init__(self):
            self.wd = webdriver.Chrome()
            self.wd.implicitly_wait(60)
            self.session = SessionHelper(self)
            self.group = GroupHelper(self)
            self.contacts = Сontact(self)


        def open_home_page(self):
            # Открытие основной страницы
            wd = self.wd
            wd.get("http://localhost/addressbook/")



        def destroy(self):
            self.wd.quit()
