from sys import maxsize


class UserForm:
    def __init__(self, firstname=None,
                 middlename=None,
                 lastname=None,
                 nickname=None,
                 title=None,
                 company=None,
                 address=None,
                 homephone=None,
                 mobilephone=None,
                 workphone=None,
                 fax=None,
                 email=None,
                 email2=None,
                 email3=None,
                 homepage=None,
                 byear=None,
                 ayear=None,
                 address2=None,
                 phone2=None,
                 notes=None,
                 id=None,
                 all_phones_from_home_page=None,
                 all_address_from_home_page=None,
                 all_emails_from_home_page=None):
        self.firstname = firstname
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_address_from_home_page = all_address_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = homephone
        self.mobile = mobilephone
        self.work = workphone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.byear = byear
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.firstname == other.firstname and self.lastname == other.lastname

    def __repr__(self):
        return "%s: %s: %s: %s: %s: %s: %s: %s: %s" % (self.id, self.firstname, self.lastname, self.middlename,
                                                       self.homepage, self.nickname, self.address, self.company,
                                                       self.email)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
