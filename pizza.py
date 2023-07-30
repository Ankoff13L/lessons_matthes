

pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms', 'extra cheese'],
}

print(f"You order a {pizza['crust']} - crust pizza "
    "with the followinng topings:")

for topping in pizza['toppings']:
    print("\t" + topping)

