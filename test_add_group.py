# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from group import *

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def return_to_group_page(self, wd):
        # return to group page
        wd.find_element_by_link_text("group page").click()

    def create_group(self, wd, group):
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()

    def open_groups_page(self, wd):
        # open group's page
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def opent_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def test_add_named_group(self):
        wd = self.wd
        self.opent_home_page(wd)
        self.login(wd, "admin", "secret")
        self.open_groups_page(wd)
        self.create_group(wd, Group("NewGroup", 'NewHeader', 'NewFooter'))
        self.return_to_group_page(wd)
        self.logout(wd)

    def test_empty_group(self):
        wd = self.wd
        self.opent_home_page(wd)
        self.login(wd, "admin", "secret")
        self.open_groups_page(wd)
        self.create_group(wd, Group('', '', ''))
        self.return_to_group_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
