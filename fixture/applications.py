from selenium import webdriver

from fixture.contacts import Contact
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Applications:


        def __init__(self):
            self.wd = webdriver.Chrome()
            self.wd.implicitly_wait(5)
            self.session = SessionHelper(self)
            self.group = GroupHelper(self)
            self.contacts = Contact(self)

        def is_valid(self):
            try:
                self.wd.current_url
                return True
            except:
                return False



        def open_home_page(self):
            # Открытие основной страницы
            wd = self.wd
            wd.get("http://localhost/addressbook/")

        def destroy(self):
            self.wd.quit()