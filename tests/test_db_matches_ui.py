from model.group import Group
from model.user_form import UserForm
from timeit import timeit


def test_group_list(app, db):
    print(timeit(lambda: app.group.get_group_list(), number=1))
    ui_list = app.group.get_group_list()

    def clean(group):
        return Group(id=group.id, name=group.name.strip())

    print(timeit(lambda: map(clean, db.get_group_list()), number=1))
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def test_user_list(app, db):
    print(timeit(lambda: app.user.get_users_list(), number=1))
    ui_list = app.user.get_users_list()

    def clean(user):
        return UserForm(id=user.id, firstname=user.firstname.strip(), lastname=user.lastname.strip())

    db_list = map(clean, db.get_contact_list())
    assert sorted(ui_list, key=UserForm.id_or_max) == sorted(db_list, key=UserForm.id_or_max)