import zmq
import random

# Setup ZMQ
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

# Save nouns into lists
with open("list.txt", 'r') as f: random_lines = f.readlines()

with open("animals.txt", 'r') as f: animal_lines = f.readlines()

with open("feelings.txt", 'r') as f: feeling_lines = f.readlines()

with open("food.txt", 'r') as f: food_lines = f.readlines()

with open("vehicles.txt", 'r') as f: vehicle_lines = f.readlines()

# Retrieve noun/s
def get_noun(category):
    category = category.lower()
    if category == "animal":
        lines = animal_lines
    elif category == "feeling":
        lines = feeling_lines
    elif category == "food":
        lines = food_lines
    elif category == "vehicle":
        lines = vehicle_lines
    else:
        lines = random_lines
    return random.choice(lines).strip().lower()

def get_nouns(quantity, category = "random"):
    noun_string = ""
    for i in range(int(quantity)):
        noun_string += get_noun(category)
        if i < int(quantity) - 1:
            noun_string += " "
    return noun_string

# Send reply/ recieve request
while True:
    message = socket.recv()

    if len(message) > 0:
        s = message.decode().split()
        quantity = s[0]
        
        if len(s) > 1:
            category = s[1]
        else:
            category = "random"

        nouns = get_nouns(quantity, category)
        socket.send_string(nouns)