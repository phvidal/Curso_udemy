players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(f'Esses são os três primeiros jogadores de nosso time:')
for player in players[:3]:
    print(player.title())


# COPIANDO PARTE DE UMA LISTA

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods [:]

print(f'My favorite food are: {my_foods}')
print(f"\nMy friend's favorite foods are: {friend_foods}")

my_foods.append('ice cream')
friend_foods.append('cannoli')

print(my_foods)
print(friend_foods)
