
# age = 12

# if age < 4:                              # младше 4 лет
#     print("Your admission cost is $0.")
# elif age < 18:                            # от 4 до 18 лет
#     print("Your admission cost is $25.")
# else:                                    # от 18 и старше
#     print("Your admission cost is $40.")

# для посетителей младше 4 леит билет бесплатный
# для посетителей от 4 до 18 лет билет стоит $25
# для постетителей от 18 лет и старше билет стоит $40


# Упрощение кода

# age = 12

# if age < 4:                              
#     price = 0
# elif age < 18:                            
#     price = 25
# else:                                    
#     price = 40

# print(f"Your admission cost is ${price}.")


age = 66

if age < 4:                              
    price = 0    # если меньше 4 лет то цена $0
elif age < 18:                            
    price = 25   # если старше 4 лет и но меньше 18 лет то цена $25
elif age < 65:                            
    price = 40   # если старше 18 лет и но меньше 65 лет то цена $40
else:                                    
    price = 20   # во всех остальных случаях цена $20.  
                 # А остальные случаи это если 65 лет и старше

print(f"Your admission cost is ${price}.")

