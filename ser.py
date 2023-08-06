


def send_messages(short_messages):
    while short_messages:
        current_messag = short_messages.pop()
        print(current_messag)
        sent_messages.append(current_messag)



short_messages = ['hello', 'today', 'black', 'country']
sent_messages = []

send_messages(short_messages[:])
