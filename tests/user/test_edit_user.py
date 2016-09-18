from model.user_form import UserForm


def test_modify_contacts_first_name(app):
   old_users = app.user.get_users_list()
   user = UserForm(firstname='Nikolo',lastname='Detroid')
   modified_user = UserForm(firstname ='Fin',lastname='Adventure')
   modified_user.id = old_users[0].id
   if app.user.count() == 0:
        app.user.add(user)
   app.user.editing_user(modified_user)
   new_users = app.user.get_users_list()
   assert len(old_users) == len(new_users)
   old_users[0] = modified_user
   assert sorted(old_users, key=UserForm.id_or_max) == sorted(new_users, key=UserForm.id_or_max)