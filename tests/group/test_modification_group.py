from model.group import Group
from data.add_group import testdata
import random
import pytest


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_modification_group(app, group):
    if app.group.count() == 0:
        app.group.create(group)
    old_groups = app.group.get_group_list()
    index = random.randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.modify_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == app.group.count()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
