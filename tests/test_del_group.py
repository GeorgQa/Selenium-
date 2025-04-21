
import pytest

from fixture.applications import Applications


def test_delete_first_group(app):
    app.group.delete_first_group()



