from model.group import Group


def test_modification_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test", footer="test"))
    app.group.modification_first(Group("name", "header", "footer"))


def test_modification_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test", footer="test"))
    app.group.modification_first(Group(name="name"))


def test_modification_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test", footer="test"))
    app.group.modification_first(Group(header="new_header"))


def test_modification_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test", footer="test"))
    app.group.modification_first(Group(footer="new_footer"))
