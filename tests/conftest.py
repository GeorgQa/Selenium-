import pytest

from fixture.applications import Applications


@pytest.fixture(scope= "session")
def app(request):
    fixture = Applications()
    fixture.session.login(user="admin", password='secret')
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return  fixture

@pytest.fixture(autouse=True)
def open_home_page(app):
    app.open_home_page()