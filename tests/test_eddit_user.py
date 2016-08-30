from model.user_form import UserForm


def test_eddit_first_user(app):
    app.session.login("admin", "secret")
    app.user.editing_user(UserForm(
                                firstname="2", middlename="3",
                                lastname="Nik5olo", nickname="Nikolo",
                                title="asd", company="hgf",
                                adress="sdf", home="mfd4",
                                mobile="sdfg34", work="dfgd",
                                fax="jgjfd", notes="Nikolo",
                                email="Nikolo", homepage="Nikolo",
                                byear="Nikolo", ayear="Nikolo",
                                address2="Nikolo", phone2="Nikolo"
                            ))
    app.session.logout()

