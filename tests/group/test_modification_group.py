from model.group import Group


def test_modification_group(app):
    app.group.modification_first(Group("name", "header", "footer"))


def test_modification_group_name(app):
    app.group.modification_first(Group(name="name"))


def test_modification_group_header(app):
    app.group.modification_first(Group(header="new_header"))


def test_modification_group_footer(app):
    app.group.modification_first(Group(footer="new_footer"))
