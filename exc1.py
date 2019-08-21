players = {
    'ronaldo': {
        'first': 'Christiano',
        'last': 'Ronaldo',
        'location': 'Turin'
    },
    'messi': {
        'first': 'Leo',
        'last': 'Messi',
        'location': 'Barcalona'
    },
}

for player_name, player_info in players.items():
    print("\nPlayer_name: " + player_name)
    full_name = player_info['first'] + ' ' + player_info['last']
    location = player_info['location']
    
    print("\tFull_name: " + full_name.title())
    print("\tLocation: " + location.title())