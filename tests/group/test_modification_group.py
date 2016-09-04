from model.group import Group


def test_modification_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modification_first(Group("name", "header", "footer"))
    app.session.logout()


def test_modification_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modification_first(Group(name="name"))
    app.session.logout()


def test_modification_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modification_first(Group(header="new_header"))
    app.session.logout()


def test_modification_group_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.modification_first(Group(footer="new_footer"))
    app.session.logout()