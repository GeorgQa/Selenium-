from selenium.webdriver.common.by import By


class FieldFiller:
    def __init__(self, app):
        self.app = app

    def check_fill_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)