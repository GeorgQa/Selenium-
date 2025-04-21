import pytest

from fixture.applications import Applications

fixture = None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Applications()

    else:
        if not fixture.is_valid():
            fixture = Applications()
    fixture.session.ensure_login(username="admin", password='secret')
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return  fixture

@pytest.fixture(autouse=True)
def open_home_page(app):
    app.open_home_page()