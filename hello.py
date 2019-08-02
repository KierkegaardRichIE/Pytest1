users = ['Admin', 'Kierke', 'Ronaldo', 'vini bear', 'Ada', 'Trump']
users.sort()
for user in users:
    if user == 'Admin':
        print('Hello, ' + user + ' would you like to see a status report?')
    if user == 'Trump':
        print('The 93-year-old president of Zimbabwe was recently asked in a talk show: "If time passes, what do you want to do most?"Mugabe answered: "I want to go back to 1945, find Trump\'s father and give him a condom.')
    if user != 'Admin' and user != 'Trump':
        print('Hello,' + user + ' think you for you logging in!')
