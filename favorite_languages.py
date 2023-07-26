


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

favorite_languages['anwei'] = 'c++'
favorite_languages[ 'vova'] = 'c#'
favorite_languages[ 'vera'] = 'python'

ex_user = ['jen', 'sarah', 'edward', 'phil']
for users in favorite_languages.keys():
    if users in ex_user:
        print(f"Thank you {users.title()} for participating in the survey!")
    else:
        print(F"\t{users.title()} take our survey.")

