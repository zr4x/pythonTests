from model.user_form import UserForm
from random import randrange
from data.user import testdata
import random


# def test_modify_contacts_first_name(app, db):
#     user = UserForm(firstname="nikili", middlename="lolo")
#
#     if app.user.count() == 0:
#         app.user.create(user)
#
#     old_users = app.user.get_users_list()
#     index = randrange(len(old_users))
#     modified_user = UserForm(firstname="", lastname="Adasdasdasdasdaventure")
#     modified_user.id = old_users[index].id
#     app.user.editing_by_index(index, modified_user)
#     assert len(old_users) == app.user.count()
#     new_users = app.user.get_users_list()
#     old_users[index] = modified_user
#     assert sorted(old_users, key=UserForm.id_or_max) == sorted(new_users, key=UserForm.id_or_max)


def test_modify_contacts_first_name(app, db):
    if app.user.count() == 0:
        app.user.create(UserForm(firstname="add_name1"))
    old_users = db.get_contact_list()
    user_random = random.choice(old_users)
    user = UserForm(firstname="first_name", lastname="Last_name", middlename="Mid_name", nickname="nick_name",
                      company="company1", address="address11", homephone="1234")
    user.id = user_random.id
    app.user.modify_user_by_id(user_random.id, user)
    new_users = db.get_contact_list()
    old_users.remove(user_random)
    old_users.append(user)
    assert sorted(old_users, key=UserForm.id_or_max) == sorted(new_users, key=UserForm.id_or_max)