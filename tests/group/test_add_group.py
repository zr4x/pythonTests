from model.group import *


def test_add_named_group(app):
    app.group.create(Group("NewGroup", "NewHeader", "NewFooter"))



def test_empty_group(app):
    app.group.create(Group("", "", ""))

