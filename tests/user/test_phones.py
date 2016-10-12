import re
from random import randrange
from model.user_form import UserForm


# def test_phones_on_home_page(app):
#     user_from_home_page = app.user.get_users_list()[0]
#     user_from_edit_page = app.user.get_users_info_from_edit_page(0)
#     assert user_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(user_from_edit_page)
#
#
# def test_phones_on_user_view_page(app):
#     users_from_view_page = app.user.get_users_from_view_page(0)
#     user_from_edit_page = app.user.get_users_info_from_edit_page(0)
#     assert users_from_view_page.home == user_from_edit_page.home
#     assert users_from_view_page.mobile == user_from_edit_page.mobile
#     assert users_from_view_page.work == user_from_edit_page.work
#     assert users_from_view_page.phone2 == user_from_edit_page.phone2
#
#
def test_home_page_vs_edit_page(app):
    if app.user.count() == 0:
        app.user.create(UserForm(firstname="Nikolo", lastname="Kozlov", nickname="rott",
                    homephone="33", mobilephone="895125646", workphone="+79999",
                    phone2="898998", address="volodarskogo 50", email="new@keepa.ru"))
    index = randrange(app.user.count())
    user_from_home_page = app.user.get_users_list()[index]
    user_from_edit_page = app.user.get_users_info_from_edit_page(index)
    assert user_from_home_page.firstname == user_from_edit_page.firstname
    assert user_from_home_page.lastname == user_from_edit_page.lastname
    assert user_from_home_page.address == user_from_edit_page.address
    assert user_from_home_page.email == user_from_edit_page.email
    assert user_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(user_from_edit_page)


# def merge_emails_like_on_home_page(user):
#     return "\n".join(filter(lambda x: x != "",
#                             map(lambda x: clear(x),
#                                 filter(lambda x: x is not None,
#                                        [user.email, user.email2, user.email3]))))


#def merge_address_like_on_home_page(user):
    # return "\n".join(filter(lambda x: x != "",
    #                         map(lambda x: clear(x),
    #                             filter(lambda x: x is not None,
    #                                  [user.address]))))

def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(user):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [user.home, user.mobile, user.work, user.phone2]))))
