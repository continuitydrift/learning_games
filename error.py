import random, json

## put this in your python file:
## from messages import load_messages, give_message


def load_messages():
    global messages
    with open("messages.json", "r") as readfile:
        messages= json.load(readfile)

def give_message():
    message=random.choice(messages)
    print (message)

if __name__ == "__main__":
    load_messages()
    give_message()

load_messages()
give_message()
