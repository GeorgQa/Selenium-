
import pytest

from fixture.applications import Applications


@pytest.fixture
def app(request):
    fixture = Applications()
    request.addfinalizer(fixture.destroy)
    return  fixture

def test_delete_group(app):
    app.open_home_page()
    app.session.login()
    app.group.create()
    app.group.filling_in_group_data( "new_group", "Header", "vtgtr")
    app.group.save()
    app.session.logout()



