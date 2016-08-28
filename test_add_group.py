# -*- coding: utf-8 -*-
import pytest
from group import *
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_named_group(app):
    app.login(username="admin",password="secret")
    app.create_group(Group("NewGroup", "NewHeader", "NewFooter"))
    app.logout()

def test_empty_group(app):
    app.login("admin", "secret")
    app.create_group(Group("", "", ""))
    app.logout()

