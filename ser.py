
import print_fun

# def send_messages(short_messages):
#     while short_messages:
#         current_messag = short_messages.pop()
#         print(current_messag)
#         sent_messages.append(current_messag)



print_fun.short_messages = ['hello', 'today', 'black', 'country']
print_fun.sent_messages = []

print_fun.send_messages(print_fun.short_messages[:])

