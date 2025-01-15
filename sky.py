"""
  _____ _             _                        
 / ____| |           | |   | (_)            
| (___ | |_ __ _ _ __| |_          |_   
 \___ \| __/ _` | '__| __|              | __ 
 ____) | || (_| | |  | |_         | _
|_____/ \__\__,_|_|   \__|          __,
                                           _ |
                                         |_
"""

"""
  _____ _                   _     _               
 / ____| |                 | |   | |              
| (___ | |_ _ __ _   _  ___| |__ | |__   ___ _ __ 
 \___ \| __| '__| | | |/ __| '_ \| '_ \ / _ \ '__|
 ____) | |_| |  | |_| | (__| | | | | | |  __/ |   
|_____/ \__|_|   \__,_|\___|_| |_|_| |_|\___|_|   
                                                  
"""


class Setting:
    """A class representing a setting with various attributes."""
    
    def __init__(self, name, location, climate, population, description=""):
        self.name = name          # Name of the setting
        self.location = location  # Location of the setting
        self.climate = climate    # Climate of the setting
        self.population = population  # Population of the setting
        self.description = description  # Description of the setting

# Example of creating an object with the Setting class
my_setting = Setting(
    name="Mystic Forest",
    location="Northern Hemisphere",
    climate="Temperate",
    population=500,
    description="A mysterious forest filled with ancient trees and magical creatures."
)

# Accessing attributes
print(f"Setting Name: {my_setting.name}")
print(f"Location: {my_setting.location}")
print(f"Climate: {my_setting.climate}")
print(f"Population: {my_setting.population}")
print(f"Description: {my_setting.description}")


# A strange and cumbersome way to write code, but it might work.
class Character:
    """A class representing a character."""
    
    def __init__(self, name, role, description, level):
        self.name = name
        self.role = role
        self.description = description
        self.level = level

class Artifact:
    """A class representing an artifact."""
    
    def __init__(self, name, origin, description, power_level):
        self.name = name
        self.origin = origin
        self.description = description
        self.power_level = power_level

class Quest:
    """A class representing a quest."""
    
    def __init__(self, name, objective, description, difficulty):
        self.name = name
        self.objective = objective
        self.description = description
        self.difficulty = difficulty

class Story:
    """A class representing a story."""
    
    def __init__(self, title, setting, description, length):
        self.title = title
        self.setting = setting
        self.description = description
        self.length = length

# Example of creating objects for each class
character = Character(name="Aragorn", role="Ranger", description="A skilled warrior and leader.", level=20)
artifact = Artifact(name="Excalibur", origin="Legendary", description="A powerful sword of myth.", power_level=100)
quest = Quest(name="Dragon Hunt", objective="Slay the dragon", description="A dangerous quest to defeat a dragon.", difficulty="Hard")
story = Story(title="The Great Adventure", setting="Fantasy World", description="An epic tale of heroism.", length="Long")

# Accessing attributes
print(f"Character: {character.name}, Role: {character.role}, Level: {character.level}")
print(f"Artifact: {artifact.name}, Origin: {artifact.origin}, Power Level: {artifact.power_level}")
print(f"Quest: {quest.name}, Objective: {quest.objective}, Difficulty: {quest.difficulty}")
print(f"Story: {story.title}, Setting: {story.setting}, Length: {story.length}")
