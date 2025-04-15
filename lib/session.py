from selenium.webdriver.common.by import By


class SessionHelper:



    def Logout(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def login(self):
        wd = self.wd
        wd.find_element(By.NAME, "user").send_keys("admin")
        wd.find_element(By.NAME, "pass").send_keys("secret")
        wd.find_element(By.ID, "LoginForm").submit()