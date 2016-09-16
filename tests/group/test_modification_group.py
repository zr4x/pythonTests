from model.group import Group


def test_modification_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="test", header="test", footer="test")
    group.id = old_groups[0].id
    if app.group.count() == 0:
        app.group.create(group)
    app.group.modification_first(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)


def test_modification_group_name(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test", footer="test"))
    app.group.modification_first(Group(name="name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modification_group_header(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test", footer="test"))
    app.group.modification_first(Group(header="new_header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modification_group_footer(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test", footer="test"))
    app.group.modification_first(Group(footer="new_footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
