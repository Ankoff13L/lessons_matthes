# from random import randint, choice

# my_randint = randint(1, 15)
# print(my_randint)

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# first_up = choice(players)
# print(first_up)



# from random import randint

# class Die():
#     """Создает кубик с числами"""

#     def __init__(self, sides=6):
#         self.sides = sides

#     def roll_die(self):
#         """Бросает кубик"""
#         result = randint(1, self.sides)
#         print(result)

# side_6 = Die()     # 6-ти гранный кубик
# side_6.roll_die()

# side_10 = Die(10)  # 10-ти гранный кубик
# side_10.roll_die()


# side_20 = Die(20)   # 20-ти гранный кубик
# side_20.roll_die()





# from random import choice

# series = [13,'r', 4, 'd', 7, 'a', 9, 'c', 8, 23, 5, 10, 2, 1]

# def run_select():
#     part_numb_1 = choice(series)
#     part_numb_2 = choice(series)
#     part_numb_3 = choice(series)
#     part_numb_4 = choice(series)
#     print(f"Won tickets containing combinations: {part_numb_1}, {part_numb_2}, {part_numb_3}, {part_numb_4}!")


# run_select()


# """
# Измененный вариант предудущей программы. Вместо функции choice()
# применена функция choices(). Код стал короче. Применение параметра k=4 сокращает
# код на 3 строчки
# """
# from random import choices

# series = [13,'r', 4, 'd', 7, 'a', 9, 'c', 8, 23, 5, 10, 2, 1]

# def run_select():
#     final_nunb = choices(series, k=4)
#     print(f"Won tickets containing combinations: {final_nunb}!")


# run_select()



# from random import choice """Неправильный код, оставил для примера"""


# def run_select():
#     win_part = ['c','c','c']
#     if win_part != comb_part:
#         while my_ticket:
#             comb_part.append(choice(my_ticket))
#             comb_part.append(choice(my_ticket))
#             comb_part.append(choice(my_ticket))
#             return(comb_part)
#     else:
#         print(f"Combination won: {win_part}")
#         # print(f"There were {} executions of the cycle before receiving a winning combination.")



# comb_part = []
# my_ticket = ['a','b','c']

# comb = run_select()
# print(comb)

# """А это правильный код, предыдущей идеи, после того как, ознакомился с док. модуля и применил к=3"""

# from random import choices


# my_ticket = ['a','b','c', 'd', 'e']
# com_par = choices(my_ticket, k=3)

# print(com_par)




from random import choices


my_ticket = ['a','b','c', 'd', 'e']
won_combination = ['c', 'c', 'c']

counter = 1

while True:
    com_par = choices(my_ticket, k=3)
    counter +=1

    if won_combination == com_par:
        break
    else:
        print(com_par)


print(com_par)
print(f"To get a winning combination, it took {counter} cycles!")





