import pytest

from fixture.applications import Applications


@pytest.fixture(scope= "session")
def app(request):
    fixture = Applications()
    request.addfinalizer(fixture.destroy)
    return  fixture
