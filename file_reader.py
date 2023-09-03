# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
# print(contents)


# """
# Тот же код, только добавленsq метод rstrip() удаляем
# лишнюю пустую строку, которая появляется псоле применения метода read()
# """
# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
# print(contents.rstrip())



# filename = 'pi_digits.txt'

# with open(filename) as file_object:
#     for line in file_object:
#         print(line)


# """
# Тот же код, что и предыдущий. Только для удаления
# лишних строк добавили метод rstrip()
# """

# filename = 'pi_digits.txt'

# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())



# filename = 'pi_digits.txt'

# with open(filename) as file_object:
#     lines = file_object.readlines()

# for line in lines:
#     print(line.rstrip())



# filename = 'pi_digits.txt'

# with open(filename) as file_object:
#     lines = file_object.readlines()

# pi_string = ''
# for line in lines:
#     pi_string += line.rstrip()

# print(pi_string)
# print(len(pi_string))


# filename = 'pi_digits.txt'

# with open(filename) as file_object:
#     lines = file_object.readlines()

# pi_string = ''
# for line in lines:
#     pi_string += line.strip() # вместо rstrip()

# print(pi_string)
# print(len(pi_string))



# filename = 'pi_million_digits.txt' # Файл с количеством знаков числа пи 1_000_000

# with open(filename) as file_object:
#     lines = file_object.readlines()

# pi_string = ''
# for line in lines:
#     pi_string += line.strip()

# print(f"{pi_string[:1000]}...")
# print(len(pi_string))


filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in thhe form ddmmyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")



