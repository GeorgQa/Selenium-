from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def logout(self):
        wd = self.app.wd
        WebDriverWait(wd, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Logout"))
        )
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def login(self, user ="admin", password ="secret"):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.NAME, "user").send_keys(user)
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.ID, "LoginForm").submit()


    def is_logged_in_as(self, username):
        wd = self.app.wd
        wd.find_element(By.XPATH, '//*[@id="top"]/form/b').text == f"({username})"

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements(By.LINK_TEXT, "Logout")) > 0

