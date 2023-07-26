
# person_data = {
#     'first_name' : "alex",
#     'last_name' : "kuznetsov",
#     'age' : 51,
#     'city' : 'ekb',
# }

# print(person_data)
# print(person_data['first_name'].title())
# print(person_data['last_name'].title())
# print(person_data['age'])
# print(person_data['city'].title())

# life_numbers = {
#     'alex' : 4,
#     'david' : 13,
#     'lida' : 23,
#     'fenya' : 1,
# }

# numbers = life_numbers['alex']
# print(f"Alex's favorite numbers is {numbers}!")

# numbers = life_numbers['david']
# print(f"David's favorite numbers is {numbers}!")

# numbers = life_numbers['lida']
# print(f"Lida's favorite numbers is {numbers}!")

# numbers = life_numbers['fenya']
# print(f"Fenya's favorite numbers is {numbers}!")


# glossarys = {
#     'lists' : 'is an ordered set of data',
#     'tuples' : 'this is an immutable list',
#     'dicts' : 'these are data structures',
# }

# glossarys_print = glossarys['lists']
# print(f"\nLists: \t{glossarys_print}.")

# glossarys_print = glossarys['tuples']
# print(f"\nTuples: \t{glossarys_print}.")

# glossarys_print = glossarys['dicts']
# print(f"\nDicts: \t{glossarys_print}.")


# glossarys = {
#     'lists' : 'is an ordered set of data',
#     'tuples' : 'this is an immutable list',
#     'dicts' : 'these are data structures',
# }

# glossarys['set'] = 'unordered collection of unique elements'
# glossarys['for'] = 'loop is used to iterate over a sequence'
# glossarys['if'] = 'this is a typical conditional construct'
# glossarys['range'] = 'allows you to generate a series of numbers'
# glossarys['print'] = 'displaying information on the screen'

# for key, value in glossarys.items():
#     print(f"\n{key.title()}: {value}!")

rivers = {
    'nile' : 'egypt',
    'thames' : 'england',
    'kongo' : 'africa',
}

# for key, value in rivers.items():
#     print(f"The {key.title()} runs through {value.title()}.")

# for key in rivers.keys():
#     print(key.title())

for value in rivers.values():
    print(value.title())
