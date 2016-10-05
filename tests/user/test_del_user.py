from model.user_form import UserForm
from random import randrange


def test_user_delete(app):
    user = UserForm(firstname="nikili", middlename="lolo")

    if app.user.count() == 0:
        app.user.create(user)

    old_users = app.user.get_users_list()
    index = randrange(len(old_users))
    app.user.delete_user_by_index(index)
    assert len(old_users) - 1 == app.user.count()
    new_users = app.user.get_users_list()
    old_users[index:index+1] = []
    assert old_users == new_users
