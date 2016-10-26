from model.user_form import UserForm
import random


def test_user_delete(app, db, check_ui):
    if app.user.count() == 0:
        app.user.create(UserForm(firstname="nikili", middlename="lolo"))

    old_users = db.get_contact_list()
    user = random.choice(old_users)
    app.user.delete_user_by_id(user.id)
    new_users = db.get_contact_list()
    assert len(old_users) - 1 == len(new_users)
    old_users.remove(user)
    assert len(old_users) == len(new_users)
    if check_ui:
        assert sorted(new_users, key=UserForm.id_or_max) == sorted(app.user.get_users_list(), key=UserForm.id_or_max)
