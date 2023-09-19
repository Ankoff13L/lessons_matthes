# def get_formatted_name(first, last):
#     """Строит отформатированное имя."""
#     full_name = f"{first} {last}"
#     return full_name.title()


# def get_formatted_name(first, middle, last):
#     """Строит отформатированное имя."""
#     full_name = f"{first} {middle} {last}"
#     return full_name.title()



# """Найти и вывести число из списка кратное 2"""


# numbers = [1, 5, 3, 6, 0, -4]

# value_result = False
# index_list = 0

# while index_list < len(numbers):
#     value_result = numbers[index_list] % 2 == 0
#     if value_result:
#         break
#     index_list += 1

# print(value_result)


def get_formatted_name(first, last, middle=''):
    """Строит отформатированное имя."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()









