
import pytest

from fixture.applications import Applications



def test_delete_first_group(app):
    app.open_home_page()
    app.session.login()
    app.group.delete_first_group()
    app.session.logout()



