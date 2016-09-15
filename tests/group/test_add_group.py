from model.group import *


def test_add_named_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group("NewGroup", "NewHeader", "NewFooter"))
    new_groups = app.group.get_group_list()
    assert len(old_groups)+1 == len(new_groups)


def test_empty_group(app):
    app.group.create(Group("", "", ""))

