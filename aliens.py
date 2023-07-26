


# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)




# Создание пустого списка для хранения пришельцев
# aliens = []

# # Создаем 30 зеленых пришельцев.
# for alien_number in range(30):
#     new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
#     aliens.append(new_alien)


# # вывод первых 5 пришельцев
# for alien in aliens[:5]:
#     print(alien)
# print("...") # просто для красоты

# # Вывод количества созданных пришельцев
# print(f"Total number of aliens: {len(aliens)}")


# aliens = []

# # Создаем 30 зеленых пришельцев.
# for alien_number in range(0, 30):
#     new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
#     aliens.append(new_alien)

# # Меняем цвет, очки и скорость для 3 пришельцев
# for alien in aliens[0:3]:
#     if alien['color'] == 'green':
#        alien['color'] = 'yellow'
#        alien['speed'] = 'medium'
#        alien['point'] = 10


# # вывод первых 5 пришельцев
# for alien in aliens[:5]:
#     print(alien)
# print("...") # просто для красоты

# # Вывод количества созданных пришельцев
# print(f"Total number of aliens: {len(aliens)}")



aliens = []

# Создаем 30 зеленых пришельцев.
for alien_number in range(30):
    new_alien = {'color' : 'green','speed' : 'slow', 'points' : 5}
    aliens.append(new_alien)

for alien in aliens[:10]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
        if alien['color'] == 'yellow':
            alien['color'] = 'red'
            alien['speed'] = 'fast'
            alien['points'] = 15

for alien in aliens[:]:
    print(alien)

print("..............")

print(len(aliens))



