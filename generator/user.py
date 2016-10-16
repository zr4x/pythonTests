from model.user_form import UserForm
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of users", "file ="])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/user.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix,maxlen):
    symbol = string.ascii_letters + string.digits + " " *10
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


testdata = [UserForm(firstname="first2name", lastname="Last2name", nickname="nick2name",
                     address="address112") ] + \
           [UserForm(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10),
             middlename=random_string("middlename:", 10),homepage=random_string("homepage:", 10),
             nickname=random_string("nickname:", 10), address=random_string("address:", 10),
             company=random_string("company:", 10), email=random_string("email:", 10))
            for i in range (n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)),"..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))