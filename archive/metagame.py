# This is a metagame. The thing that I know how to do is write.

# Let's assume that there is some evil closing in, and that the only way to do battle is by mixing metaphors. Calling on the drift.

import os

# What if my real calling is a person who writes entertaining comments in lines of code, a kind of text adventure for nerds, although nerds that exercise and have a diverse set of intellectual interests. 

import json

# The trick is to have files that can drift between layers of operational interface. Lots of bridges between fiefdoms of competing format.

import random

# Continuity and Drift

# The thing about the metagame is that the program can exist only as speculation, as thought experiment. This is, after all, the beginning of the file,  so that by the time the functional code comes around, asking for review, there are already ants of icipation.


import time

# That is the key element, the vintage, the revisiting of things. You descend into the cellar for a cask of Amontillado. A rare vintage. The terror of brick by brick


gr = 1.6180339887498948482

# The golden ration, the standard of sequences to be remembered.

# 618-0339, like a phone number

buffer = "\n \n \n      "

# Here, is the first offering to the spirit of reusability, of modularity. We have a variable representing three blank lines and a bunch of spaces.

spacing = "   ~   "

#      


def welcome():

    print (buffer, "Welcome to the Drift.", buffer, spacing)
    time.sleep(gr)

#print ("\n\n\n", "Your quest has been restarted", "\n\n\n")

# pseudocode: display a menu, where the options are, [n]ew quest, [o]ld quest, [r]andom quest. Before that, though, display a quote. In order to display thequote, check to see if quotes.json exists, and if not, create it. Do all this, actually, by importing everything from another python file called quote_machine.py.

# from quotemachine import *

def start():
    check_if_fish()
#    check_if_masks()
#    load_fish()
#    load_masks()
#    menu()
    first_fish()

def menu():
    answer = str(input("would you like to [p]lay the metagame, or [a]dd xp to a mask?"))
    try:
        if answer == "p":
#            print ("You embark upon a quest. Set your intention.")
#            time.sleep(gr)
            play()
        elif answer == "a":
            print ("You have chosen to add xp to a mask")
            add_xp()
            # This will only be for manually adding xp. If I can get xp added to a mask in the save file by the end of this stream, I earn 100 xp for the mask of my choice.
        else:
            print ("excuse me?")
            time.sleep(2)
            menu()
    except:
        print ("you have failed")
        time.sleep(gr)
        error_message()

def clear():
    from os import system, name
    # for windows
    if name == 'nt':
#        _ = system('cls')
        pass
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def check_if_fish():
    global buffer, fish

    # checking if there is data at the same level as the metagame (root folder)
    if os.path.isfile("fish.json"):
        print (buffer, "fish file exists", buffer)
        time.sleep(1)
        clear()
        if os.path.getsize("fish.json")>0:
            pass
        else:
            first_fish()
    else:
        time.sleep(1)
        clear()
        print (buffer, "no fish file", buffer)
        time.sleep(1)
        clear()
        print (buffer, "making one now", buffer)
        try:
            fish = {}
            with open("fish.json", "w") as outfile:
                json.dump(fish, outfile)
                clear()
                print (buffer, "file created", buffer)
        except:
            clear()
            print (buffer, "you dead", buffer)
            error_message()

def check_if_masks():
    buffer = "\n \n \n \n \n \n      "
    if os.path.isfile("masks.json"):
        print (buffer, "masks file exists", buffer)
        time.sleep(1)
        clear()
    else:
        time.sleep(1)
        clear()
        print (buffer, "no masks file", buffer)
        time.sleep(1)
        clear()
        print (buffer, "making one now", buffer)
        try:
            masks = {}
            with open("masks.json", "w") as outfile:
                json.dump(masks, outfile)
                clear()
                print (buffer, "file created", buffer)
            time.sleep(1)
        except:
            clear()
            print (buffer, "you dead", buffer)

def check_if_monsters():
    buffer = "\n \n \n \n \n \n      "
    if os.path.isfile("monsters.json"):
        print (buffer, "monsters file exists", buffer)
        time.sleep(1)
        clear()
    else:
        time.sleep(1)
        clear()
        print (buffer, "no monsters file", buffer)
        time.sleep(1)
        clear()
        print (buffer, "making one now", buffer)
        try:
            monsters = {}
            with open("monsters.json", "w") as outfile:
                json.dump(monsters, outfile)
                clear()
                print (buffer, "file created", buffer)
            time.sleep(1)
        except:
            clear()
            print (buffer, "you dead", buffer)

def load_fish():
    global fish
    with open("fish.json", "r") as rf:
        fish = json.load(rf)
        if fish:
            for i in fish:
                print (i)
        else:
            fish = {}

def load_masks():
    global masks
    with open("masks.json", "r") as rf:
        masks = json.load(rf)
        if masks:
            for i in masks:
                print (i)
        else:
            masks = {}
            save_masks()

def turn():
    global fish
    buffer = "\n \n \n \n \n \n      "
    load_fish()
    wait = input("here is the break point.")
    if "turns" in fish:
        turns = fish["turns"]
        if turns > 0:
            turns += 1
            print (buffer, "this is turn", turns, buffer)
            fish["turns"] = turns
            save_fish()

            time.sleep(1)
        else:
            fish["turns"]=1
            turn()

    else:
        print (buffer, "there are no records. The library has been burned.", buffer)
        fish["turns"] = 1
        save_fish()
        time.sleep(4)
        turn()

def save_masks():
    global masks
    buffer = "\n \n \n \n \n \n      "

    with open("masks.json", "w") as outfile:
        json.dump(masks, outfile)
        clear()
        print (buffer, "file saved", buffer)

#
#
#     _|_|_|    _|_|_|  _|      _|    _|_|
#   _|_|      _|    _|  _|      _|  _|_|_|_|
#       _|_|  _|    _|    _|  _|    _|
#   _|_|_|      _|_|_|      _|        _|_|_|
#       _|_|  _|            _|
#     _|            _|_|_|  _|_|_|
#   _|_|_|_|  _|  _|_|      _|    _|
#     _|      _|      _|_|  _|    _|
#     _|      _|  _|_|_|    _|    _|
#
#

def save_fish():
    global fish
    buffer = "\n \n \n \n \n \n      "

    with open("fish.json", "w") as outfile:
        json.dump(fish, outfile)
        clear()
        print (buffer, "file saved", buffer)

def check_if_fish():

    global fish


    # this check if fish is huge. If I'm going to write, if I'm going to code, then I'll do it my way.

    # Things can always be exported to other places. Language can always glance wistfully, almost pleadingly, at the sky. Hoping to be beamed up, to be remembered.


    # This function should simply see if fish exist, and if not, create first_fish

    # The challenge, the technical puzzle I would like to solve, is to be able to have fish both be a class object, and also savable and loadable




#
#       _|_|  _|            _|
#     _|            _|_|_|  _|_|_|
#   _|_|_|_|  _|  _|_|      _|    _|
#     _|      _|      _|_|  _|    _|
#     _|      _|  _|_|_|    _|    _|
#
#


class Fish():

    # You are standing in front of a pool of clear intent. It is fed, high up in the mountains, by revenue streams. Don't think, for a moment, of the goblin villages, of the fish, floating mutated and bloated.

    # Think instead of those tasks, those intentions, those fish made trinkets, pleiagic horrors.

    # fish will outlive humans. You stare at them, primitive spear in hand, knowing that your task is two-fold. One of quickness, of piercing the liquid with your bit of wood, and the other a question, now, of adjusting for the mistakes you made in past attempts. The fish, that bit of food and brightness, isn't there. It's there, adjusted. I know you don't believe me, that your instincts of having survived as yourself shout at you to turn, but hold.

    # There is now a class called Fish. When we create a fish object it will have an attribute 'points'

    def __init__(self, points):
        self.points = points
#        self.dict =
#        self.total_points = points
#        self.average_points = points


#    def get_fish_dict(self):
#        global fish_dict
#        print ("congratulations, you got a class method to work.")
#        fish_dict = {'points': self.points, 'total_points': self.points, 'average_points': self.points}

#test_fish = Fish(4)

#print ("You see a fish swimming in the stream. It is worth", test_fish.points, "points.")
#try:
#    test_fish_dict = {}
#    test_fish_dict["points"]= test_fish.points
#except:
#    print ("couldn't create dictionary from class object")



        #


#
#       _|_|  _|                        _|
#     _|          _|  _|_|    _|_|_|  _|_|_|_|
#   _|_|_|_|  _|  _|_|      _|_|        _|
#     _|      _|  _|            _|_|    _|
#     _|      _|  _|        _|_|_|        _|_|
#       _|_|  _|            _|
#     _|            _|_|_|  _|_|_|
#   _|_|_|_|  _|  _|_|      _|    _|
#     _|      _|      _|_|  _|    _|
#     _|      _|  _|_|_|    _|    _|
#
#




def first_fish():
    global fish
    # create a class object instance of fish
    first_fish = Fish(1)

    print ("this fish is worth", first_fish.points, "point")

    first_fish_str = json.dumps(first_fish.__dict__)

    print ("the json string is:", first_fish_str)

    fish = first_fish_str
    save_fish()


def random_error():
    global fishes
#    print ("You have made the worst mistake, and claimed the greatest victory. You are dead, and get to make a new character.")
#    time.sleep(3)
#    print ("The magic of things is this: you can hear yourself singing. You know where things were sour, and where they were, for a moment, sweet.\nTend your garden.\n")
    time.sleep(gr)
    print ("You need to have a fish. No one may pass beyond this point with out a fish. That is what I have decided.")
    try:
        if fishes:
            pass
        else:

            print ("I mean, c'mon, you didn't expect that to work, did you?")
    except:
#        print ("At the end of this function, at the end of this turn for the stream, which can't come to soon, let me say this: your singing sucks. You have no understanding of any kind of codes. ")
        pass

def add_xp():
    global masks

    print ("here are the extant masks:")
    for i in masks:
        print (masks[i])
    answer = input(str("which mask do you want to add xp to?"))
    try:
        print ("you have chosen", masks[answer]["name"])
        additional_xp = input("How much additional experience do you want to award?")
        print ("we will add", additional_xp)
        try:
            print ("your original xp was", masks[answer]["xp"])
            try:
                additional_xp = int(additional_xp)
                masks[answer]["xp"] += additional_xp
            except:
                print ("couldn't add xp")
            print (masks[answer]["name"], "now has", masks[answer]["xp"], "experience")
        except:
            print ("the part where you tried to add xp failed.")
    except:
        error_message()

    time.sleep(gr)
    save_masks()
    #print ("placeholder for add xp")
start()
