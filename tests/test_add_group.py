# -*- coding: utf-8 -*-
import pytest
from model.group import *
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_named_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group("NewGroup", "NewHeader", "NewFooter"))
    app.session.logout()


def test_empty_group(app):
    app.session.login("admin", "secret")
    app.group.create(Group("", "", ""))
    app.session.logout()
