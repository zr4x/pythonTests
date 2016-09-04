from model.user_form import UserForm


def test_new_user_create(app):
    app.user.fill_new_user_form(UserForm(
                                firstname="Nikolo", middlename="Nikolo",
                                lastname="Nikolo", nickname="Nikolo",
                                title="Nikolo", company="Nikolo",
                                adress="Nikolo", home="Nikolo",
                                mobile="Nikolo", work="Nikolo",
                                fax="Nikolo", notes="Nikolo",
                                email="Nikolo", homepage="Nikolo",
                                byear="Nikolo", ayear="Nikolo",
                                address2="Nikolo", phone2="Nikolo"
                            ))


