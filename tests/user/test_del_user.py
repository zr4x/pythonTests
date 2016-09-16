from model.user_form import UserForm


def test_first_user_delete(app):
    old_users = app.user.get_users_list()
    if app.user.count() == 0:
        app.user.fill_new_user_form(UserForm(firstname="nikili", middlename="lolo"))
    app.user.delete_fist_user()
    new_users = app.user.get_users_list()
    old_users[0:1] = []
    assert old_users == new_users