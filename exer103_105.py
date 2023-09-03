# filename = 'guest.txt'

# with open(filename, 'w') as open_object:
#     last_name = input("That is name: ")
#     open_object.write(last_name)


# filename = 'guest_book.txt'

# with open(filename, 'a') as open_object:
#     open_object.write(last_name)
#     while True:
#         last_name = input("That is name: ")
#         print(f"Hello {last_name.title()}!")



while True:
    filename = 'guest_book.txt'
    with open(filename, 'a', ) as open_object:
        last_name = input("That is name: ")
        if last_name == 'q':
            break
        print(f"Hello {last_name.title()}!")
        open_object.write(last_name + '\n')



# while True:
#     filename = 'like_programm.txt'
#     with open(filename, 'a') as open_object:
#         answers = input("Why do you like programming: ")
#         open_object.write(answers + '\n')
