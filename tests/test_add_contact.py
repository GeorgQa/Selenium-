

from faker import Faker



def test_add_contact(app):
    fake = Faker("ru_Ru")
    app.open_home_page()
    app.session.login()
    app.contacts.filling_out_form(firstName= fake.first_name(),
                         company=fake.company(),
                         nick_name=fake.last_name_female(),
                         group_add=fake.text(),
                         lastName= fake.last_name(),
                         middleName=fake.middle_name(),
                         a_year=fake.year(),
                         amonth=fake.month(),
                         birtday_year=fake.year())
    app.contacts.save_and_end()
    app.session.logout()

def test_add_contact_random(app):
    fake = Faker("ru_Ru")
    app.open_home_page()
    app.session.login()
    app.contacts.filling_out_form(firstName=fake.first_name(),
                         middleName=fake.middle_name(),
                         lastName= fake.last_name(),
                         nick_name=fake.last_name_female(),
                         company= fake.company())
    app.contacts.save_and_end()
    app.session.logout()



