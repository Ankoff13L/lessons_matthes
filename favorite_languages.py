# favorite_languages = {
#     'jen' : 'python',
#     'sarah' : 'c',
#     'edward' : 'ryby',
#     'phil' : 'python',
# }

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")


# favorite_languages = {
#     'jen' : 'python',
#     'sarah' : 'c',
#     'edward' : 'ryby',
#     'phil' : 'python',
# }

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")


# favorite_languages = {
#     'jen' : 'python',
#     'sarah' : 'c',
#     'edward' : 'ryby',
#     'phil' : 'python',
# }

# print("The following languages have been mentioned:")
# for language in favorite_languages.values():
#     print(language.title())


# favorite_languages = {
#     'jen' : 'python',
#     'sarah' : 'c',
#     'edward' : 'ryby',
#     'phil' : 'python',
# }

# print("The following languages have been mentioned:")
# for language in set(favorite_languages.values()):
#      print(language.title())


# Словарь  с списками вместо простых значений
favorite_languages = {
    'jen' : ['python', 'ruby'],
    'sarah' : ['c'],
    'edward' : ['ryby', 'go'],
    'phil' : ['python', 'haskell'],
}


for name, languages in favorite_languages.items():
    if len(languages) < 2:
        print("Sarah's favorite language is C")
    elif len(languages) >= 2:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")




