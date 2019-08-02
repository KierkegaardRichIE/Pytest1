current_users = ['Ada', 'Kierke', 'Donald', 'Eric', 'Dick']
new_users = ['Kierke', 'Trump', 'White', 'Pinkman', 'Pokeman', 'dick']
current_users_lower = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print('The ID: ' + new_user + ' is already in use, please enter a new ID!')
    else:
        print('You can use this ID, is it confirmed ?')
