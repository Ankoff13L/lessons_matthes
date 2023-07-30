

# prompt = "\nPlease enter the name of a city you have visited: "
# prompt += "\n(Enter 'quit' when you are finished.) "

# while True:
#     city = input(prompt)

#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love toqo to {city.title()}!")



def describe_city(city_name='reykjavik', country_name='iceland'):
    print(f"{city_name.title()} is in {country_name.title()}.")

describe_city()

describe_city(city_name='london', country_name='england')
describe_city(city_name='rome', country_name='italy')
describe_city(city_name='berlin', country_name='germany')


