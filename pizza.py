

# pizza = {
#     'crust' : 'thick',
#     'toppings' : ['mushrooms', 'extra cheese'],
# }

# print(f"You order a {pizza['crust']} - crust pizza "
#     "with the followinng topings:")

# for topping in pizza['toppings']:
#     print("\t" + topping)



# def make_pizza(*toppings):
#     """Вывод списка заказанных топпингов"""
#     print(toppings)

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'exra cheese')




def make_pizza(*toppings):
    """Выводит описание пиццы."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'exra cheese')


