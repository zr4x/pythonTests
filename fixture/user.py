from model.user_form import UserForm
import re


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
        self.delete_user_by_index(0)

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
        self.change_user_fill_value("address", user_form.address)
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

    def return_to_contact(self):
        wd = self.app.wd
        if len(wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img")) > 0 \
                and len(wd.find_elements_by_xpath("//div[@id='content']/form[2]/div[1]/input")) > 0:
            return
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.return_to_contact()
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
                all_phones = cells[5].text
                all_address = cells[3].text
                all_emails = cells[4].text
                self.users_cache.append(UserForm(firstname=firstname, lastname=lastname, id=id,
                                                 all_phones_from_home_page=all_phones,
                                                 address=all_address,
                                                 email=all_emails
                                                 ))
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
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        # home task 14
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        return UserForm(firstname=firstname, lastname=lastname, id=id,
                        homephone=homephone, mobilephone=mobilephone, workphone=workphone,
                        phone2=phone2, email=email, email2=email2, email3=email3, address=address)

    def get_users_from_view_page(self, index):
        wd = self.app.wd
        self.open_user_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return UserForm(homephone=homephone, mobilephone=mobilephone, workphone=workphone,
                        phone2=phone2)
