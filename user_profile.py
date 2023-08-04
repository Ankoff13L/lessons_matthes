


# def build_profile(first, last, **user_info):
#     """Строит словарь user_info с информацией о пользователе, потому что стоит 2 звездочки
#     перед параметром user_info."""

#     print(user_info) # строка чисто чтобы увидеть, что находится в словаре, до добавления
#                      # имени и фамилии. Для Функции строка не нужна.


#     user_info['first_name'] = first # запись новой пары "ключ:значение" в словарь user_info
#     user_info['last_name'] = last   # запись новой пары "ключ:значение" в словарь user_info
#     return user_info # возращает словарь user_info в точку вызова функции

# user_profile = build_profile('albert', 'einstein',  # сначала эта строка является точкой вызова
#                              location='princeton',  # затем return передает в нее словарь user_info
#                              field='physics')

# print(user_profile) # выводит информацию созданного словаря user_info





# def build_profile(first, last, **user_info):

#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info

# user_profile = build_profile('albert', 'einstein',
#                              location='princeton',
#                              field='physics')

# print(user_profile)


# def making_sandwich(*args):
#     print(f"\nOrdered sandwich with ingredients:")
#     for arg in args:
#         print(f"- {arg}")

# making_sandwich("mushrooms")
# making_sandwich('extra chees', 'oak bark')
# making_sandwich('exra lucky', 'fly', 'magic force', 'divine light')



def build_profile(gender, height, **user_info):
    user_info['gender_pat'] = gender
    user_info['height_hair'] = height
    return user_info

conclusion = build_profile('bitch', 'bald', analyzes='spoiled', voice='coughs')
print(conclusion)




