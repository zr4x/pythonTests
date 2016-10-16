from model.user_form import UserForm
from random import randrange
from data.user import testdata



def test_modify_contacts_first_name(app):
    user = UserForm(firstname="nikili", middlename="lolo")

    if app.user.count() == 0:
        app.user.create(user)

    old_users = app.user.get_users_list()
    index = randrange(len(old_users))
    modified_user = UserForm(firstname="", lastname="Adasdasdasdasdaventure")
    modified_user.id = old_users[index].id
    app.user.editing_by_index(index, modified_user)
    assert len(old_users) == app.user.count()
    new_users = app.user.get_users_list()
    old_users[index] = modified_user
    assert sorted(old_users, key=UserForm.id_or_max) == sorted(new_users, key=UserForm.id_or_max)
