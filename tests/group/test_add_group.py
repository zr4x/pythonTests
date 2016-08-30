from model.group import *


def test_add_named_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group("NewGroup", "NewHeader", "NewFooter"))
    app.session.logout()


def test_empty_group(app):
    app.session.login("admin", "secret")
    app.group.create(Group("", "", ""))
    app.session.logout()
