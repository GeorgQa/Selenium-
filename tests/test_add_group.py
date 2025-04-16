# -*- coding: utf-8 -*-
import unittest
import pytest

from lib.applications import Applications

from lib.session import SessionHelper


@pytest.fixture
def app(request):
    fixture = Applications()
    request.addfinalizer(fixture.destroy)
    return  fixture

def test_add_group(app):
    app.open_home_page()
    app.login()
    app.create_group()
    app.filling_in_group_data( "new_group", "Header", "vtgtr")
    app.save()
    app.logout()

def test_no_data_group(app):
    app.open_home_page()
    app.login()
    app.create_group()
    app.filling_in_group_data( " ", " ", " ")
    app.save()
    app.logout()


if __name__ == "__main__":
    unittest.main()
