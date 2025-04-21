
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Contact:

    def __init__(self, app):
        self.app = app


    def contact_to_ref(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()

    def filling_out_form(self, firstName, middleName, lastName, nick_name, company, group_add, day_birthday,
                         mouht_bday="December", birtday_year="2001", aday="20", amonth="July", a_year="2020"):
        wd = self.app.wd

        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys(firstName)
        wd.find_element(By.NAME, "middlename").clear()
        wd.find_element(By.NAME, "middlename").send_keys(middleName)
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys(lastName)
        wd.find_element(By.NAME, "nickname").clear()
        wd.find_element(By.NAME, "nickname").send_keys(nick_name)
        wd.find_element(By.NAME, "bday").click()
        wd.find_element(By.NAME, "bday").send_keys(day_birthday)
        wd.find_element(By.NAME, "bmonth").send_keys(mouht_bday)
        wd.find_element(By.NAME, "byear").click()
        wd.find_element(By.NAME, "byear").send_keys(birtday_year)
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").clear()
        wd.find_element(By.NAME, "company").send_keys(company)
        wd.find_element(By.NAME, "aday").click()
        wd.find_element(By.NAME, "aday").send_keys(aday)
        wd.find_element(By.NAME, "amonth").click()
        wd.find_element(By.NAME, "amonth").send_keys(amonth)
        wd.find_element(By.NAME, "ayear").click()
        wd.find_element(By.NAME, "ayear").send_keys(a_year)


        try:
            WebDriverWait(wd, 2).until(
                EC.presence_of_element_located((By.NAME, "new_group")))
            wd.find_element(By.NAME, "new_group").click()
            wd.find_element(By.NAME, "new_group").send_keys(group_add)
        except:
            pass

    def save_and_end(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "submit").click()


    def first_record_delete(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home").click()
        wd.find_element(By.XPATH, '//*[@id="maintable"]/tbody/tr[2]/td[8]/a/img').click()
        wd.find_element(By.XPATH, '//*[@id="content"]/form[2]/input[2]').click()

    def two_record_modification(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home").click()
        wd.find_element(By.XPATH, '//*[@id="maintable"]/tbody/tr[3]/td[8]/a/img').click()


    def update(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, '//*[@id="content"]/form[1]/input[21]').click()   #///*[@id="content"]/form[1]/input[21] //*[@id="content"]/form[1]/input[21]
        wd.find_element(By.PARTIAL_LINK_TEXT, "home page").click()

    def filling_in_contacts(self, contact):
        wd = self.app.wd
        self.filler.check_fill_value("firstname", contact.firstname)
        self.filler.check_fill_value("lastname", contact.lastname)
        self.filler.check_fill_value("nick_name", contact.nick_name)
        self.filler.check_fill_value("company", contact.company)
        self.filler.check_fill_value("group_add", contact.group_add)
        self.filler.check_fill_value("bday", contact.day_birthday)




