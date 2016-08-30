# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.user_form import UserForm


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_new_user_create(app):
    app.login("admin", "secret")
    app.add_new_user()
    app.fill_new_user_form(UserForm(
                                firstname="Nikolo", middlename="Nikolo",
                                lastname="Nikolo", nickname="Nikolo",
                                title="Nikolo", company="Nikolo",
                                adress="Nikolo", home="Nikolo",
                                mobile="Nikolo", work="Nikolo",
                                fax="Nikolo", notes="Nikolo",
                                email="Nikolo", homepage="Nikolo",
                                byear="Nikolo", ayear="Nikolo",
                                address2="Nikolo", phone2="Nikolo"
                            ))
    app.logout()
