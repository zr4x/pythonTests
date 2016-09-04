class UserHelper:
    def __init__(self, app):
        self.app = app

    def add_new_user(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def fill_new_user_form(self, user_form):
        wd = self.app.wd
        self.fill_user_form(user_form)
        self.confirm_new_user()
        self.return_to_home_page()

    def confirm_new_user(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def select_first_user(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_fist_user(self):
        wd = self.app.wd
        self.select_first_user()
        wd.find_element_by_xpath(".//*[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def go_to_edit_page(self):
        wd = self.app.wd
        self.select_first_user()
        wd.find_element_by_xpath(".//*[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()

    def editing_user(self, user_form):
        wd = self.app.wd
        self.go_to_edit_page()
        self.fill_user_form(user_form)
        # Update user Profile
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def fill_user_form(self, user_form):
        self.change_user_fill_value("firstname",user_form.firstname)
        self.change_user_fill_value("middlename",user_form.middlename)
        self.change_user_fill_value("lastname",user_form.lastname)
        self.change_user_fill_value("nickname",user_form.nickname)
        self.change_user_fill_value("title",user_form.title)
        self.change_user_fill_value("company",user_form.company)
        self.change_user_fill_value("address",user_form.adress)
        self.change_user_fill_value("home",user_form.home)
        self.change_user_fill_value("mobile",user_form.mobile)
        self.change_user_fill_value("work",user_form.work)
        self.change_user_fill_value("fax",user_form.fax)
        self.change_user_fill_value("email",user_form.email)
        self.change_user_fill_value("homepage",user_form.homepage)
        self.change_user_fill_value("byear",user_form.byear)
        self.change_user_fill_value("ayear",user_form.ayear)
        self.change_user_fill_value("address2",user_form.address2)
        self.change_user_fill_value("phone2",user_form.phone2)
        self.change_user_fill_value("notes",user_form.notes)


    def change_user_fill_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)
