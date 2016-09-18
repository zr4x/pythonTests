from model.user_form import UserForm


def test_modify_contacts_first_name(app):
    user = UserForm(firstname="nikili", middlename="lolo")

    if app.user.count() == 0:
        app.user.create(user)

    old_users = app.user.get_users_list()
    modified_user = UserForm(firstname="Fin", lastname="Adventure")
    modified_user.id = old_users[0].id
    app.user.editing_user(modified_user)
    assert len(old_users) == app.user.count()
    new_users = app.user.get_users_list()
    old_users[0] = modified_user
    assert sorted(old_users, key=UserForm.id_or_max) == sorted(new_users, key=UserForm.id_or_max)
