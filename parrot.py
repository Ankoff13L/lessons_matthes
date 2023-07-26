


# prompt = "\nTell me something, and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program. "
# message = " "
# while message != 'quit': # цикл while производит сравнение
#     message = input(prompt)

#     if message != 'quit':
#         print(message)



# prompt = "\nTell me something, and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program. "

# active = True
# message = ""
# while active:       # цикл while без выполнения сравнения
#     message = input(prompt)

#     if message != 'quit':
#         print(message)
#     else:
#         active = False


prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    elif message == 'nooo':
         active = False
    else:
        print(message)

