from model.group import Group
from data.group import testdata
import random
import pytest

#
# @pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
# def test_modification_group(app, group):
#     if app.group.count() == 0:
#         app.group.create(group)
#     old_groups = app.group.get_group_list()
#     index = random.randrange(len(old_groups))
#     group.id = old_groups[index].id
#     app.group.modify_by_index(index, group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == app.group.count()
#     old_groups[index] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modification_group(app, db):
    if db.get_group_list() == 0:
        app.group.create(Group(name="aasddd1"))
    old_groups = db.get_group_list()
    group_random = random.choice(old_groups)
    group = Group(name="fel", header="ga", footer="felga")
    group.id = group_random.id
    app.group.modify_group_by_id(group_random.id, group)
    new_groups = db.get_group_list()
    old_groups.remove(group_random)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)