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

def file_exists(filename):
    """Check if a file exists."""
    return os.path.isfile(filename)

def start():
    """Start the program by checking for data and loading it."""
    does_data_exist()
    load_data()
    check_deck()  # Check for deck
    menu()
    save_data()

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

def load_data():
    """Load data from data.JSON."""
    global data
    if not file_exists("data.JSON"):
        print("Data file does not exist. Creating a new one.")
        data = {}
        save_data()
        return
    
    with open("data.JSON", "r") as rf:
        data = json.load(rf)

def load_json_file(filename):
    """Load data from a JSON file if it exists."""
    if not file_exists(filename):
        print(f"Error: {filename} does not exist.")
        return None
    with open(filename, "r") as readfile:
        return json.load(readfile)

def load_quotes():
    """Load quotes from quotes.JSON and count them."""
    global quotes
    quote_count = 0
    if not file_exists("quotes.json"):
        print("Quotes file does not exist. Creating a new one.")
        quotes = {}
        save_quotes()
        return
    
    with open("quotes.json", "r") as rf:
        quotes = json.load(rf)
        
        for _ in quotes:
            quote_count += 1
    print("There are", quote_count, "quotes.")

def load_masks():
    """Load character masks from masks.json."""
    masks = load_json_file('masks.json')
    
    if masks is None:
        return

    print("Existing characters are:")
    for n, character in enumerate(masks.keys(), start=1):
         print(f"{n}: {character}")

    ans = input("Who do you want to play? ").strip()
    
    # Check if the selected character exists
    if ans in masks:
        character = masks[ans]
        for attribute, value in character.items():
            print(f"Your {attribute} is {value}.")
    else:
        print("Didn't quite catch that.")
        time.sleep(0.2)
        load_masks()  # Retry loading masks if input is invalid

def does_data_exist():
    """Check if data.JSON exists and is not empty."""
    global data

    if os.path.isfile("data.JSON"):
        print("Congratulations, data file exists!")
        
        if os.path.getsize("data.JSON") > 0:
            print("It is greater than 0")
        else:
            print("Data file exists, but is blank.")
            data = {}
            save_data()
    
    else:
        print("Data file does not exist. Creating a new one.")
        data = {}
        save_data()

def menu():
    """Display menu options to the user."""
    global data
    ans = input("What do you want to do? [b]urn the archive, [c]reate a card, or start a [n]ew turn? ").strip().lower()
    
    if ans == "b":
        print("The archive is burning.")
        try:
            data = {}
            save_data()
            menu()  # Loop back to menu after burning
            
        except Exception as e:
            print(f"The archive's walls prove more fireproof than we thought. Error: {e}")
    
    elif ans == "c":
        create_new_card()  # Call function to create a new card
    
    elif ans == "n":
        print("A new turn is starting.")
        turn()
    
    else:
        print("Didn't understand your answer. A new turn is starting.")
        turn()

def save_data():
    """Save current data to data.JSON."""
    global data
    with open("data.JSON", "w") as wf:
        json.dump(data, wf)

def save_quotes():
    """Save current quotes to quotes.json."""
    global quotes
    with open("quotes.json", "w") as wf:  
        json.dump(quotes, wf)

def save_deck():
     """Save current deck to deck.json."""
     global deck
     with open("deck.json", "w") as wf:  
         json.dump([card.__dict__ for card in deck], wf)  # Save card attributes

def check_deck():
     """Check if the deck exists and load it."""
     global deck
     if not file_exists("deck.json"):
         print("Deck does not exist. Creating a new one.")
         deck = []
         save_deck()
     else:
         with open("deck.json", "r") as rf:
             card_data = json.load(rf)
             deck = [Card(**data) for data in card_data]  # Recreate Card instances from saved data
             print(f"Loaded {len(deck)} cards from the deck.")

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

def create_new_card():
     """Prompt user for details and create a new card."""
     name = input("Enter card name: ")
     description = input("Enter card description: ")
     notes = input("Enter any notes for this card: ")
     xp = int(input("Enter XP for this card (default is 0): ") or 0)
     level = int(input("Enter level for this card (default is 1): ") or 1)
     a = int(input("Enter value for attribute A (default is 0): ") or 0)
     s = int(input("Enter value for attribute S (default is 0): ") or 0)
     h = int(input("Enter value for attribute H (default is 0): ") or 0)
     d = int(input("Enter value for attribute D (default is 0): ") or 0)
     r = int(input("Enter value for attribute R (default is 0): ") or 0)
     m = int(input("Enter value for attribute M (default is 0): ") or 0)

     new_card = create_card(name, description, notes, xp, level, a, s, h, d, r, m)
     global deck
     deck.append(new_card)  # Add new card to the deck
     save_deck()             # Save updated deck

def turn():
     """Start a new turn by loading masks."""
     load_masks()

# Start the program
start()
