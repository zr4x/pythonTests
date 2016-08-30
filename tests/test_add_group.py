# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.group import *


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_named_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group("NewGroup", "NewHeader", "NewFooter"))
    app.session.logout()


def test_empty_group(app):
    app.session.login("admin", "secret")
    app.create_group(Group("", "", ""))
    app.session.logout()
