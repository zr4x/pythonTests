from model.user_form import UserForm


class UserHelper:
    def __init__(self, app):
        self.app = app

    def add_new_user(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, user_form):
        self.add_new_user()
        self.fill_user_form(user_form)
        self.confirm_new_user()
        self.return_to_home_page()
        self.users_cache = None

    def confirm_new_user(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def select_first_user(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def return_main_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")

    def delete_user_by_index(self, index):
        wd = self.app.wd
        self.select_user_by_index(index)
        wd.find_element_by_xpath(".//*[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.return_main_page()
        self.users_cache = None

    def delete_first_user(self):
        self.delete_user_by_index()

    def select_user_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def editing_by_index(self, index, user_form):
        wd = self.app.wd
        self.go_to_edit_page(index)
        self.fill_user_form(user_form)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.users_cache = None

    def fill_user_form(self, user_form):
        self.change_user_fill_value("firstname", user_form.firstname)
        self.change_user_fill_value("middlename", user_form.middlename)
        self.change_user_fill_value("lastname", user_form.lastname)
        self.change_user_fill_value("nickname", user_form.nickname)
        self.change_user_fill_value("title", user_form.title)
        self.change_user_fill_value("company", user_form.company)
        self.change_user_fill_value("address", user_form.adress)
        self.change_user_fill_value("home", user_form.home)
        self.change_user_fill_value("mobile", user_form.mobile)
        self.change_user_fill_value("work", user_form.work)
        self.change_user_fill_value("fax", user_form.fax)
        self.change_user_fill_value("email", user_form.email)
        self.change_user_fill_value("homepage", user_form.homepage)
        self.change_user_fill_value("byear", user_form.byear)
        self.change_user_fill_value("ayear", user_form.ayear)
        self.change_user_fill_value("address2", user_form.address2)
        self.change_user_fill_value("phone2", user_form.phone2)
        self.change_user_fill_value("notes", user_form.notes)

    def change_user_fill_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    users_cache = None

    def get_users_list(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/addressbook"):
            wd.get("http://localhost/addressbook/")
        if self.users_cache is None:
            wd = self.app.wd
            self.users_cache = []
            for element in wd.find_elements_by_name("entry"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                cells = element.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                self.users_cache.append(UserForm(firstname=firstname, lastname=lastname, id=id))
        return self.users_cache

    def open_user_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def go_to_edit_page(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def get_users_info_from_edit_page(self, index):
        wd = self.app.wd
        self.go_to_edit_page(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("work").get_attribute("value")
        workphone = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("home").get_attribute("value")
        return UserForm(firstname=firstname, lastname=lastname, id=id,
                        homephone=homephone, mobilephone=mobilephone, workphone=workphone,
                        phone2=phone2)

