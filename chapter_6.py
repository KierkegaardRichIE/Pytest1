kierkepz_ID = {
    'first_name': 'Kierke',
    'last_name': 'Qi',
    'age': '24',
    'city': 'Haidong',
}
favorite_language = {
    'kierkepz': 'python',
    'salah': 'c',
    'ada': 'assembly',
    'mike': 'ruby',
    'gates': 'c#',
    'linus': 'c++',
}
player_1 = {
    'name': 'ronaldo',
    'club': 'juventus',
    'back_num': '7'
}
player_2 = {
    'name': 'messi',
    'club': 'barcalona',
    'back_num': 10
}
player_3 = {
    'name': 'bale',
    'club': 'real madrid',
    'back_num': 7
}
players_top3 = [player_1, player_2, player_3]
for player in players_top3:
    print(player)
print('\n')
river_list = {
    'nile': 'egypt',
    'Yellow-river': 'China',
}

players = []

for player_number in range(11):
    new_player = {
        'speed': 15,
        'shoot': 12,
        'defend': 8
    }
    players.append(new_player)
for player in players[:7]:
    print(player)
print('...')
print('\n')

print('kierke is from ' +
      kierkepz_ID['city'] +
      '.' +
      ' He is ' +
      kierkepz_ID['age'] +
      ' years old!')

for key, value in kierkepz_ID.items():
    print('\nkey: ' + key)
    print('value: ' + value)
for name, language in favorite_language.items():
    print(name.title() + "'s favorite language is " +
          language.title() +
          '.')
print('\n')
for name in favorite_language.keys():
    print(name.title() +
          ', thank you for your talking the poll.')
print('\n')
for language in favorite_language.values():
    print(language.title())
del favorite_language['mike']
print('\n')

for language in favorite_language.values():
    print(language.title())
for player_number in range(11):
    new_player = {}
