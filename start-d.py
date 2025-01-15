# -*- coding: utf-8 -*-

"""
Created on Sun Jan 30 10:24:58 2022

@author: continuitydrift
"""

import os
import json
import time
import random
from datetime import date

#               _|                            _|
#     _|_|_|  _|_|_|_|    _|_|_|  _|  _|_|  _|_|_|_|
#   _|_|        _|      _|    _|  _|_|        _|
#       _|_|    _|      _|    _|  _|          _|
#   _|_|_|        _|_|    _|_|_|  _|            _|_|

def file_exists(filename):
    """Check if a file exists."""
    return os.path.isfile(filename)

#               _|                            _|
#     _|_|_|  _|_|_|_|    _|_|_|  _|  _|_|  _|_|_|_|
#   _|_|        _|      _|    _|  _|_|        _|
#       _|_|    _|      _|    _|  _|          _|
#   _|_|_|        _|_|    _|_|_|  _|            _|_|

def start():
    """Start the program by checking for data and loading it."""
    does_data_exist()
    load_data()
    check_setting_deck()  # Check for setting deck
    menu()
    save_data()

#               _|                            _|
#     _|_|_|  _|_|_|_|    _|_|_|  _|  _|_|  _|_|_|_|
#   _|_|        _|      _|    _|  _|_|        _|
#       _|_|    _|      _|    _|  _|          _|
#   _|_|_|        _|_|    _|_|_|  _|            _|

def do_quotes_exist():
    """Check if the quotes file exists and is not empty."""
    global quotes
    if os.path.isfile("quotes.json"):
        print("Quotes are there")
        if os.path.getsize("quotes.json") > 0:
            print("They are greater than 0")
        else:
            print("Quotes file exists, but is empty")
            quotes = {}
            save_quotes()
    else:
        print("There is no quotes file. Making one now.")
        quotes = {}
        save_quotes()

#               __          __
#              |__\ |\/\ | /__|
#              |__ \|\ \ | \__|

class Card:
    """A class representing a card with various attributes."""
    
    def __init__(self, name, description="", notes="", xp=0, level=1, a=0, s=0, h=0, d=0, r=0, m=0):
        self.name = name         # Name of the card
        self.description = description # Description of the card
        self.notes = notes       # Any additional notes about the card
        self.xp = xp             # Experience points
        self.level = level       # Level of the card (default is 1)
        self.a = a               # Attribute A (customizable)
        self.s = s               # Attribute S (customizable)
        self.h = h               # Attribute H (customizable)
        self.d = d               # Attribute D (customizable)
        self.r = r               # Attribute R (customizable)
        self.m = m               # Attribute M (customizable)

def create_card(name, description="", notes="", xp=0, level=1, a=0, s=0, h=0, d=0, r=0, m=0):
    """Create a new card with the given attributes."""
    return Card(name, description, notes, xp, level, a, s, h, d, r, m)

def check_setting_deck():
    """Check if the setting deck exists and load it."""
    
