
import pytest

from faker import Faker


from fixture.contacts import Сontact

@pytest.fixture
def contact_app(request):
    fixture = Сontact()
    request.addfinalizer(fixture.destroy)
    return  fixture


def test_add_contact(contact_app):
    fake = Faker("ru_Ru")
    contact_app.open_home_page()
    contact_app.login()
    contact_app.filling_out_form(firstName= fake.first_name(),
                                 company=fake.company(),
                                 nick_name=fake.last_name_female(),
                                 group_add=fake.text(),
                                 lastName= fake.last_name(),
                                 middleName=fake.middle_name(),
                                 a_year=fake.year(),
                                 amonth=fake.month(),
                                 birtday_year=fake.year()  )
    contact_app.save_and_end()

def test_add_contact_random(contact_app):
    fake = Faker("ru_Ru")
    contact_app.open_home_page()
    contact_app.login()
    contact_app.filling_out_form( firstName=fake.first_name(),
                                  middleName=fake.middle_name(),
                                  lastName= fake.last_name() ,
                                  nick_name=fake.last_name_female(),
                                  company= fake.company())
    contact_app.save_and_end()



