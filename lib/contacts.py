from selenium import webdriver
from selenium.webdriver.common.by import By


class Сontact:

    def __init__(self):
           self.wd = webdriver.Chrome()
           self.wd.implicitly_wait(60)

    def filling_out_form(self, firstName,
                         middleName,
                         lastName,
                         nick_name,
                         company,
                         group_add="Test_test_ran_123",
                         day_birthday="16",
                         mouht_bday="December",
                         birtday_year="2001",
                         aday="20",
                         amonth="July",
                         a_year="2020"):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "add new").click()
        wd.find_element(By.NAME, "firstname").send_keys(firstName)
        wd.find_element(By.NAME, "middlename").send_keys(middleName)
        wd.find_element(By.NAME, "lastname").send_keys(lastName)
        wd.find_element(By.NAME, "nickname").send_keys(nick_name)
        wd.find_element(By.NAME, "bday").click()
        wd.find_element(By.NAME, "bday").send_keys(day_birthday)
        wd.find_element(By.NAME, "bmonth").send_keys(mouht_bday)
        wd.find_element(By.NAME, "byear").click()
        wd.find_element(By.NAME, "byear").send_keys(birtday_year)
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").send_keys(company)
        wd.find_element(By.NAME, "aday").click()
        wd.find_element(By.NAME, "aday").send_keys(aday)
        wd.find_element(By.NAME, "amonth").click()
        wd.find_element(By.NAME, "amonth").send_keys(amonth)
        wd.find_element(By.NAME, "ayear").click()
        wd.find_element(By.NAME, "ayear").send_keys(a_year)
        wd.find_element(By.NAME, "new_group").click()
        wd.find_element(By.NAME, "new_group").send_keys(group_add)

    def save_and_end(self):
        wd = self.wd
        wd.find_element(By.NAME, "submit").click()
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def destroy(self):
        self.wd.quit()

    def open_home_page(self):
        # Открытие основной страницы
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def login(self):
        wd = self.wd
        wd.find_element(By.NAME, "user").send_keys("admin")
        wd.find_element(By.NAME, "pass").send_keys("secret")
        wd.find_element(By.ID, "LoginForm").submit()