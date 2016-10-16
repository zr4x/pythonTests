from model.user_form import UserForm


def test_new_user_create(app, json_user):
    user = json_user
    old_users = app.user.get_users_list()
    app.user.create(user)
    new_users = app.user.get_users_list()
    assert len(old_users) + 1 == app.user.count()
    old_users.append(user)
    assert sorted(old_users, key=UserForm.id_or_max) == sorted(new_users, key=UserForm.id_or_max)



