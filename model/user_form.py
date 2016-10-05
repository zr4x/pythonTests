from sys import maxsize


class UserForm:
    def __init__(self, firstname=None,
                 middlename=None,
                 lastname=None,
                 nickname=None,
                 title=None,
                 company=None,
                 adress=None,
                 homephone=None,
                 mobilephone=None,
                 workphone=None,
                 fax=None,
                 email=None,
                 homepage=None,
                 byear=None,
                 ayear=None,
                 address2=None,
                 phone2=None,
                 notes=None,
                 id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.adress = adress
        self.home = homephone
        self.mobile = mobilephone
        self.work = workphone
        self.fax = fax
        self.email = email
        self.homepage = homepage
        self.byear = byear
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
