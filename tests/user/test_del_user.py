from model.user_form import UserForm


def test_first_user_delete(app):
    old_users = app.user.get_users_list()
    user = UserForm(firstname="nikili", middlename="lolo")

    if app.user.count() == 0:
        app.user.create(user)
        old_users = app.user.get_users_list()

    app.user.delete_fist_user()
    assert len(old_users) - 1 == app.user.count()
    new_users = app.user.get_users_list()
    old_users[0:1] = []
    assert old_users == new_users
