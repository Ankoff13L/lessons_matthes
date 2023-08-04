

# pizza = {
#     'crust' : 'thick',
#     'toppings' : ['mushrooms', 'extra cheese'],
# }

# print(f"You order a {pizza['crust']} - crust pizza "
#     "with the followinng topings:")

# for topping in pizza['toppings']:
#     print("\t" + topping)


def make_pizza(size, *toppings):
    """Выводит описание пиццы."""
    print(f"\nMaking a {size} - inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperone')
make_pizza(12, 'mushrooms', 'green ppers', 'extra cheese')

