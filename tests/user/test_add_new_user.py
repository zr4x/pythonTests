from model.user_form import UserForm
import random
import pytest
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata =[
    UserForm(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10),
             middlename=random_string("middlename:", 10),homepage=random_string("homepage:", 10),
             nickname=random_string("nickname:", 10), address=random_string("address:", 10),
             company=random_string("company:", 10), email=random_string("email:", 10))
    for i in range(5)
    ]


@pytest.mark.parametrize("user", testdata, ids=[repr(x) for x in testdata])
def test_new_user_create(app, user):
    old_users = app.user.get_users_list()
    app.user.create(user)
    new_users = app.user.get_users_list()
    assert len(old_users) + 1 == app.user.count()
    old_users.append(user)
    assert sorted(old_users, key=UserForm.id_or_max) == sorted(new_users, key=UserForm.id_or_max)



