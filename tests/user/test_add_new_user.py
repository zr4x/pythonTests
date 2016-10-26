from model.user_form import UserForm


def test_new_user_create(app, db, json_user):
    user = json_user
    old_users = db.get_contact_list()
    app.user.create(user)
    new_users = db.get_contact_list()
    old_users.append(user)
    assert sorted(old_users, key=UserForm.id_or_max) == sorted(new_users, key=UserForm.id_or_max)