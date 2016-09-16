from model.user_form import UserForm


def test_new_user_create(app):
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
    app.user.fill_new_user_form(user)
    new_users = app.user.get_users_list()
    assert len(old_users) + 1 == len(new_users)



