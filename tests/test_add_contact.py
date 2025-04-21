

from faker import Faker


def test_add_contact(app):
    fake = Faker("ru_Ru")
    app.open_home_page()
    app.session.login()
    app.contacts.contact_to_ref()
    app.contacts.filling_out_form(firstName=fake.first_name(), middleName=fake.middle_name(), lastName=fake.last_name(),
                                  nick_name=fake.last_name_female(), company=fake.company(), group_add=fake.text(),
                                  day_birthday="16", birtday_year=fake.year(), amonth=fake.month(), a_year=fake.year())
    app.contacts.save_and_end()
    app.session.logout()

def test_add_contact_random(app):
    fake = Faker("ru_Ru")
    app.open_home_page()
    app.session.login()
    app.contacts.contact_to_ref()
    app.contacts.filling_out_form(firstName=fake.first_name(), middleName=fake.middle_name(), lastName=fake.last_name(),
                                  nick_name=fake.last_name_female(), company=fake.company(),
                                  group_add="Test_test_ran_123", day_birthday="16")

    app.contacts.save_and_end()
    app.session.logout()

def test_delete_contact(app):
    app.open_home_page()
    app.session.login()
    app.contacts.first_record_delete()
    app.session.logout()



def test_contact_modification(app):
    fake = Faker("ru_Ru")
    ranodom_number = fake.port_number()
    app.open_home_page()
    app.session.login()
    app.contacts.two_record_modification()
    app.contacts.filling_out_form(firstName=f"Тестовое имя {ranodom_number}", middleName=f"Тестовая фамилия",
                                  lastName=f"Олегович", nick_name=f"Любитель пива", company="Рога и копыта",
                                  group_add="Test_test_ran_123", day_birthday="16")
    app.contacts.update()
    app.session.logout()



