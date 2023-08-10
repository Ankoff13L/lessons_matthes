
import printing_functions

# """Программа без использования функций"""

# # Список моделей, которые необходимо напечатать.
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# compled_models = []

# # Цикл последовательно печатает каждую модель до конца списка.
# # После печати каждая модель перемещается в список compled_models.
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     compled_models.append(current_design)

# # Вывод всех готовых моделей.
# print("\nThe following models have been printed: ")
# for compled_model in compled_models:
#     print(compled_model)



# """Программа c 2-мя функциями"""

# def print_models(unprinted_designs, compled_models):
#     """Имитирует печать моделей, пока список не станет пустым.
#     Каждая модель после печати перемещается в compled_models"""
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         compled_models.append(current_design)

# def show_completed_models(compled_models):
#     """Выводит информацию обо всех напечатанных моделях."""
#     print("\nThe following models have been printed: ")
#     for compled_model in compled_models:
#         print(compled_model)

printing_functions.unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
printing_functions.compled_models = []

printing_functions.print_models(printing_functions.unprinted_designs,
                                printing_functions.compled_models)
printing_functions.show_completed_models(printing_functions.compled_models)



# def show_messages(short_messages):
#     for short_messag in short_messages:
#         print(short_messag)

# print_fun.short_messages = ['hello', 'today', 'black', 'country']
# print_fun.show_messages(short_messages)



# def send_messages(short_messages):
#     while short_messages:
#         current_messag = short_messages.pop()
#         print(current_messag)
#         sent_messages.append(current_messag)



# send_messages.short_messages = ['hello', 'today', 'black', 'country']
# send_messages.sent_messages = []

# send_messages(short_messages)

# print(short_messages)
# print(sent_messages)



# def send_messages(short_messages):
#     while short_messages:
#         current_messag = short_messages.pop()
#         print(current_messag)
#         sent_messages.append(current_messag)



# short_messages = ['hello', 'today', 'black', 'country']
# sent_messages = []

# send_messages(short_messages[:])

# print(short_messages)
# print(sent_messages)



# def send_messages(short_messages):
#     while short_messages:
#         current_messag = short_messages
#         # current_messag = short_messages.pop()
#         # print(current_messag)
#         # sent_messages.append(current_messag)
#         print(current_messag)


# short_messages = ['hello', 'today', 'black', 'country']
# send_messages(short_messages)

