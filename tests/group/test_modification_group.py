from model.group import Group


def test_modification_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modification_first(Group("name", "header", "footer"))
    app.session.logout()
