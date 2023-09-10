# first_number = input("Enter first number: ")
# last_number = input("Enter last number: ")

# while True:
#     try:
#         sum = int(first_number) + int(last_number)
#     except ValueError:
#         print("Numbers must be entered in digits only!")
#     else:
#         print(sum)

# while True:
#     first_number = input("Enter first number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Enter second number: ")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) + int(second_number)
#     except ValueError:
#         print("Numbers must be entered in digits only!")
#     else:
#         print(answer)

# def reader(filename):
#     try:
#         with open(filename, encoding='utf-8') as f:
#             message = f.read()
#     except FileNotFoundError:
#         # print("File not found!\n")
#         pass
#     else:
#         print(message)

# filenames = ['cats.txt', 'pets.txt', 'dogs.txt']
# for filename in filenames:
#     reader(filename)


def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print("Фал не существует")
    else:
        word = contents.lower().count('the')
        print(word)

# count_words('moby_dick.txt')

filenames = ['alice.txt', 'little_women.txt', 'moby_dick.txt', 'cats.txt', 'berty.txt' ]
for filename in filenames:
    count_words(filename)


