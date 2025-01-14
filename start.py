# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 10:24:58 2022

@author: continuitydrift
"""

#from quotemachine import *


import os, json, time, random
import os.path
from os import path
from datetime import date


#               _|                            _|
#     _|_|_|  _|_|_|_|    _|_|_|  _|  _|_|  _|_|_|_|
#   _|_|        _|      _|    _|  _|_|        _|
#       _|_|    _|      _|    _|  _|          _|
#   _|_|_|        _|_|    _|_|_|  _|            _|_|
#
#

def start():
    pass
    do_quotes_exist()
    load_quotes()
    does_data_exist()
    load_data()
    menu()
    save_data()
    from quotemachine import quote
    
def do_quotes_exist():
    global quotes
    if os.path.isfile("quotes.json"):
        print ("quotes are there")
        
        if os.path.getsize("quotes.json") > 0:
            print ("they are greater than 0")
        else:
            print ("quotes file exists, but is empty")
            quotes = {}
            save_quotes()
    else: 
        print ("there is no quotes file. making one now.")
        quotes = {}
        save_quotes()

#
#   _|                            _|
#   _|    _|_|      _|_|_|    _|_|_|
#   _|  _|    _|  _|    _|  _|    _|
#   _|  _|    _|  _|    _|  _|    _|
#   _|    _|_|      _|_|_|    _|_|_|
#
               
def load_data():
    global data
   # does_data_exist()
    with open("data.JSON", "r") as rf:
        data = json.load(rf)

        for i in data:

            pass

def load_quotes():
    global quotes
    quote_count=0
    with open("quotes.JSON", "r") as rf:
        quotes = json.load(rf)

        for i in quotes:

            quote_count +=1
    print ("there are", quote_count, "quotes.")

def load_masks():
    with open('masks.json', "r") as readfile:
        masks = json.load(readfile)
    print ("existing characters are:")
    n=0
    for i in masks:
		#print ("A mask for", i)
		#print ("your", i, "is", mask[i])
        n+=1
        print (n,": ", i)
    ans = str(input("who do you want to play?"))
    try:
        character = masks[ans]
          ##check to see if exists?
        for x in character:
            print ("your", x, "is", character[x], ".")
    except:
        print("didn't quite catch that.")
        time.sleep(.2)
        load_masks()

  

    
def does_data_exist():
    global data
    if os.path.isfile("data.JSON"):
        print ("congratulations, data file exists!")
        pass
        # File exists, so checking if data size is > 0
        if os.path.getsize("data.JSON") > 0:
# checks if data file is not empty.
#
            print ("it is greater than 0")
 



        else:
            print ("data file does not exist, or is blank.")
    
    
            #monster attack. The monster is 12: not a monster at all but a friendly NPC, 11-10: weak monster - high loot, 8-9: powerful monster - high loot 6-7: monster grows on death, 4-5: powerful monster-low loot, 2-3: two monsters.
    
            data = {}
            save_data()
          #  load_data()
    
            # 2d6 roll was an 8. A powerful monster can generate with an item that grants them +1 to one of their stats. Rolling for that stat now.
    
    else:
        data = {}
        save_data()
        #load_data()
    
def menu():
    global data
    ans = str(input("what do you want to do? [b]urn the archive, or start a [n]ew turn?"))
    
    if ans == "b":
        print ("the archive is burning.")
        try:
            data = {}

            save_data()
            menu()

            # Fire. That was one thing everyone revered, and everyone feared. It was the memory killer, the bringer of searing pain and forgetting. Cause of scars and nightmares. Sudden screaming in the night.


        except:

            # A fire spirit spoke to her. It said that she had to escape. That something was coming. None of the spirits the linguists had warned her about manifested, despire her heresy.
            print ("the archive's walls prove more fireproof than we thought.")
    if ans == "n":
        print ("a new turn is starting.")
        turn()
    else:
        print ("didn't understand your answer. /n a new turn is starting.")
        turn()

    #
#
#     _|_|_|    _|_|_|  _|      _|    _|_|
#   _|_|      _|    _|  _|      _|  _|_|_|_|
#       _|_|  _|    _|    _|  _|    _|
#   _|_|_|      _|_|_|      _|        _|_|_|
#
#
#         _|              _|
#     _|_|_|    _|_|_|  _|_|_|_|    _|_|_|
#   _|    _|  _|    _|    _|      _|    _|
#   _|    _|  _|    _|    _|      _|    _|
#     _|_|_|    _|_|_|      _|_|    _|_|_|
#
#

def save_data():
    global data
    with open("data.JSON", "w") as wf:
        json.dump(data, wf)

def save_quotes():
    global quotes
    with open("quotes.json"), "w" as wf:
        json.dump(quotes.wf)

#
#     _|
#   _|_|_|_|  _|    _|  _|  _|_|  _|_|_|
#     _|      _|    _|  _|_|      _|    _|
#     _|      _|    _|  _|        _|    _|
#       _|_|    _|_|_|  _|        _|    _|
#
#

def turn():
    global data, masks
    load_masks()
    

start()