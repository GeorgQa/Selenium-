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