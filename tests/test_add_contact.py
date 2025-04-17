

from faker import Faker


def test_add_contact(app):
    fake = Faker("ru_Ru")
    app.open_home_page()
    app.session.login()
    app.contacts.contact_to_ref()
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
    app.contacts.contact_to_ref()
    app.contacts.filling_out_form(firstName=fake.first_name(),
                         middleName=fake.middle_name(),
                         lastName= fake.last_name(),
                         nick_name=fake.last_name_female(),
                         company= fake.company())

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

    app.contacts.filling_out_form(firstName= f"Тестовое имя {ranodom_number}",
                                  middleName= f"Тестовая фамилия",
                                  lastName= f"Олегович",
                                  company= "Рога и копыта",
                                  nick_name=f"Любитель пива"
    )
    app.contacts.update()
    app.session.logout()



