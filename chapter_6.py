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
players = []

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
for name in favorite_language.keys():
    print(name.title() +
          ', thank you for your talking the poll.')
for language in favorite_language.values():
    print(language.title())
for player_number in range(11):
    new_player={}
