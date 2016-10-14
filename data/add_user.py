from model.user_form import UserForm
import random
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
