

def test_new_user_create(app):
    app.session.login("admin", "secret")
    app.user.delete_fist_user()
    app.session.logout()


