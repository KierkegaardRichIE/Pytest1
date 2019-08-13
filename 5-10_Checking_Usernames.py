current_users = ['Ada', 'Kierke', 'Donald', 'Eric', 'Dick']
new_users = ['Kierke', 'Trump', 'White', 'Pinkman', 'Pokeman', 'dick']
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
current_users_lower = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print('The ID: ' + new_user + ' is already in use, please enter a new ID!')
    else:
        print('You can use this ID, is it confirmed ?')
for number in numbers_list:
    if number == 1:
        print('1st')
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    else:
        print(str(number) + 'th')