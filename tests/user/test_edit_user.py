from model.user_form import UserForm


def test_edit_first_user(app):
    old_users = app.user.get_users_list()
    user = UserForm(
    firstname="Nikolo", middlename="Nikolo",
    lastname="Nikolo", nickname="Nikolo",
    title="Nikolo", company="Nikolo",
    adress="Nikolo", home="Nikolo",
    mobile="Nikolo", work="Nikolo",
    fax="Nikolo", notes="Nikolo",
    email="Nikolo", homepage="Nikolo",
    byear="Nikolo", ayear="Nikolo",
    address2="Nikolo", phone2="Nikolo"
    )
    if app.user.count() == 0:
        app.user.fill_new_user_form(user)
    app.user.editing_user(user)
    new_users = app.user.get_users_list()
    assert len(old_users) == len(new_users)
