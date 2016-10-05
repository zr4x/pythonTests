from model.user_form import UserForm


def test_new_user_create(app):
    old_users = app.user.get_users_list()
    user = UserForm(firstname="Nikolo", lastname="Kozlov", nickname="rott",
                    homephone="33", mobilephone="895125646", workphone="+79999",
                    phone2="898998")
    app.user.create(user)
    new_users = app.user.get_users_list()
    assert len(old_users) + 1 == app.user.count()
    old_users.append(user)
    assert sorted(old_users, key=UserForm.id_or_max) == sorted(new_users, key=UserForm.id_or_max)



