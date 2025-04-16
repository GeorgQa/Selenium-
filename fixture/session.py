from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def logout(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def login(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.NAME, "user").send_keys("admin")
        wd.find_element(By.NAME, "pass").send_keys("secret")
        wd.find_element(By.ID, "LoginForm").submit()