

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



"""Программа c 2-мя функциями"""

def print_models(unprinted_designs, compled_models):
    """Имитирует печать моделей, пока список не станет пустым.
    Каждая модель после печати перемещается в compled_models"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        compled_models.append(current_design)

def show_completed_models(compled_models):
    """Выводит информацию обо всех напечатанных моделях."""
    print("\nThe following models have been printed: ")
    for compled_model in compled_models:
        print(compled_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
compled_models = []

print_models(unprinted_designs, compled_models)
show_completed_models(compled_models)















