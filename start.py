# -*- coding: utf-8 -*-

"""
Main entry 
point 
for the application.

This 
file serves as the 
foundation for restructuring 
the entire repository.
"""

import os
import json
import time
import random



# Define the Card class
class Card:
    """A class representing a card with various attributes."""
    
    def __init__(self, name, description="", notes="", a=0, s=0, h=0, d=0, r=0, m=0, lv=0, w=0, x=0, y=0, z=0, n=0):
        self.name = name
        self.description = description
        self.notes = notes
        self.a = a
        self.s = s
        self.h = h
        self.d = d
        self.r = r
        self.m = m
        self.lv = lv
        self.w = w
        self.x = x
        self.y = y
        self.z = z
        self.n = n

class MaskCard(Card):
    """A class representing a mask card with character attributes."""
    def __init__(self, name, description="A mysterious figure", notes="", **kwargs):
        super().__init__(name=name, description=description, notes=notes, **kwargs)
        self.type = "mask"
        self.location = "starting_point"

class SettingCard(Card):
    """A class representing a setting card with location attributes."""
    def __init__(self, name, description="", notes="", location="", climate="", population="", **kwargs):
        super().__init__(name=name, description=description, notes=notes, **kwargs)
        self.type = "setting"
        self.location = location
        self.climate = climate
        self.population = population

class TurnCard(Card):
    """A class representing a turn card with additional attributes and methods."""
    
    def __init__(self, name, description="", notes="", a=0, s=0, h=0, d=0, r=0, m=0, lv=0, w=0, x=0, y=0, z=0, n=0, turn_effect=""):
        super().__init__(name, description, notes, a, s, h, d, r, m, lv, w, x, y, z, n)
        self.turn_effect = turn_effect  # Additional attribute specific to TurnCard

    def apply_turn_effect(self):
        """Apply the turn effect of the card."""
        print(f"Applying turn effect: {self.turn_effect}")


# Function to create a new card
def create_card(name, description="", notes="", a=0, s=0, h=0, d=0, r=0, m=0, lv=0, w=0, x=0, y=0, z=0, n=0):
    """Create a new card with the given attributes."""
    return Card(name, description, notes, a, s, h, d, r, m, lv, w, x, y, z, n)

# Function to save cards to a JSON file
def save_cards(cards, filename="cards.json"):
    """Save a list of cards to a JSON file."""
    with open(filename, "w") as wf:
        json.dump([card.__dict__ for card in cards], wf)

# Function to load cards from a JSON file
def load_cards(filename="cards.json"):
    """Load cards from a JSON file."""
    if not os.path.isfile(filename):
        print(f"{filename} does not exist. Creating a new one.")
        return []
    
    with open(filename, "r") as rf:
        card_data = json.load(rf)
        return [Card(**data) for data in card_data]




# Define the turn function
# Game state variables
current_mask = None
current_setting = None
turn_count = 0
deck = None

def create_initial_cards():
    """Create initial mask and setting cards if they don't exist."""
    cards = load_cards()
    if cards is None:
        cards = []

    # Create initial setting if none exists
    if not any(getattr(card, 'type', '') == 'setting' for card in cards):
        initial_setting = SettingCard(
            name="Starting Town",
            location="Crossroads",
            climate="Temperate",
            population="Small",
            description="A quiet town at the crossroads of many paths.",
            notes="starting hex"
        )
        cards.append(initial_setting)
        print("Created initial setting card")
    
    # Create initial mask if none exists
    if not any(getattr(card, 'type', '') == 'mask' for card in cards):
        initial_mask = MaskCard(
            name="Wanderer",
            description="A mysterious figure seeking their path",
            notes="starting mask",
            a=random.randint(1, 6),
            s=random.randint(1, 6),
            h=random.randint(1, 6),
            d=random.randint(1, 6),
            r=random.randint(1, 6),
            m=random.randint(1, 6)
        )
        cards.append(initial_mask)
        print("Created initial mask card")
    
    save_cards(cards)
    return cards



def initialize_game():
    """Initialize the game with a new mask and setting."""
    global current_mask, current_setting, deck
    
    # Load or create initial cards
    deck = create_initial_cards()
    
    # Choose mask
    mask_cards = [card for card in deck if getattr(card, 'type', '') == 'mask']
    if mask_cards:
        print("\nAvailable masks:")
        for i, mask in enumerate(mask_cards, 1):
            print(f"{i}. {mask.name}")
        
        print("\nOptions:")
        print("1-{}: Select existing mask".format(len(mask_cards)))
       
       
       
       
       
        print("R: Random mask")
        print("N: Create new mask")
        
        while True:
            choice = input("\nYour choice: ").upper()
            
            if choice == 'R':
                current_mask = random.choice(mask_cards)
                break
            elif choice == 'N':
                name = input("Enter mask name: ")
                if any(mask.name == name for mask in mask_cards):
                    print("A mask with that name already exists!")
                    continue
                
                description = input("Enter mask description (or press Enter for default): ")
                if not description:
                    description = "A mysterious figure seeking their path"
                
                current_mask = MaskCard(
                    name=name,
                    description=description,
                    notes="player created mask",
                    a=random.randint(1, 6),
                    s=random.randint(1, 6),
                    h=random.randint(1, 6),
                    d=random.randint(1, 6),
                    r=random.randint(1, 6),
                    m=random.randint(1, 6)
                )
                deck.append(current_mask)
                save_cards(deck)
                break
            else:
                try:
                    index = int(choice) - 1
                    if 0 <= index < len(mask_cards):
                        current_mask = mask_cards[index]
                        break
                except ValueError:
                    pass
            print("Invalid choice! Please try again.")
        
        print("\nYour mask:", current_mask.name)
        print("Stats:")
        for stat in ['a', 's', 'h', 'd', 'r', 'm']:
            print(f"{stat}: {getattr(current_mask, stat)}")
    else:
        print("No mask cards available!")
        return False
    
    # Find a setting card
    setting_cards = [card for card in deck if getattr(card, 'type', '') == 'setting']
    if setting_cards:
        current_setting = setting_cards[0]  # For now, use the first setting
        print(f"\nYou find yourself in {current_setting.name}")
        print(current_setting.description)
    else:
        print("No setting cards available!")
        return False
    
    return True


def turn():
    """Main game engine for handling turns."""
    global turn_count
    
    if turn_count == 0:
        if not initialize_game():
            return False
    
    turn_count += 1
    print(f"\n=== Turn {turn_count} ===")
    print(f"Location: {current_setting.name}")
    
    # Basic turn options
    print("\nWhat would you like to do?")
    print("1. View mask stats")
    print("2. Explore setting")
    print("3. End turn")
    
    choice = input("Choose an action (1-3): ")
    
    if choice == "1":
        print("\nMask Stats:")
        for stat in ['a', 's', 'h', 'd', 'r', 'm']:
            print(f"{stat}: {getattr(current_mask, stat)}")
    elif choice == "2":
        print(f"\nExploring {current_setting.name}...")
        print(f"Climate: {current_setting.climate}")
        print(f"Population: {current_setting.population}")



    elif choice == "3":
        print("\nEnding turn...")
    else:
        print("\nInvalid choice. Turn ended.")
    
    time.sleep(1)





def main():
    """Main function to start the game."""
    print("Welcome to the Writing Game!")
    print("Starting a new journey...")
    
    try:
        while True:
            if not turn():
                print("Game initialization failed!")
                break
                
            # Ask if player wants to continue
            if input("\nContinue playing? (y/n): ").lower() != 'y':
                print("Saving game state...")
                save_cards(deck)  # Save before exit
                print("Thank you for playing!")
                break
    except KeyboardInterrupt:
        print("\nGame interrupted. Saving state...")
        save_cards(deck)  # Save on interrupt
        print("Game state saved. Goodbye!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Attempting to save game state...")
        save_cards(deck)  # Try to save even on error
        raise




if __name__ == "__main__":
    main()




# the game now becomes
## trying to preserve these human
## asides
# in the face of
# robotic interference
"""
For the next 25 minutes:

6. type
5. think
4. stretch
3. rest
2. play
1. map

"""