# Welcome to Continuity Drift: Story Generator

## This program provides a randomized prompt for writing fiction.


import os, json, time, random
# I'm importing the opeting system (to be able to read files), Json, which lets me read and write to data files, time (which lets me pause), and random (which lets me draw random elements from a list)


play_again = True
# The play_again variable isn't currently used, but will eventually signal that the game is over.


def intro():
	print ("\nWelcome to Continuity Drift: Story Game\n\n")


def load_data():
# this function simply loads the game data from a file.	
	global data
    # finding out if data file exists

	if os.path.isfile("game-data/data.JSON"):
#		print ("contratulations, data file exists!")
   
   # File exist, checking if data size is > 0

		if os.path.getsize("game-data/data.JSON") > 0:

   	#if so, opening and loading data

#			print ("data in game file is bigger than zero.")
			with open("game-data/data.JSON", "r") as rf:
				data = json.load(rf)
        #                print ("upon loading the data/opening the box, you see the following values:")

        #                for i in data:
        #                    print (i, "is", data[i])
#				print ("data loaded successfully!")
        # if is empty
		else:
        	### here I might as well create the first story set, since this will be run after the file exists, but it is empty.

			data = {"characters": ["A likeable but incompetent amateur", "a disillusioned cynic, weary of the world, who is called on to help a cause he doesn't believe can succeed."], "events": ["An unexpected event or crisis propels the character to act.", "The character receives a visit from an old friend, with news of a mystery."] , "resolutions": ["The crisis or adventure is resolved, but in a way the character does not expect.", "The character fails, but learns a valuable lesson."]}
			save_data()
			load_data()


    # if doesn't exist
	else:
		print("data file not found. attempting to create.")

		data = open("game-data/data.JSON", "w")
        #   os.mknod("game-data/data.JSON")
		save_data()
		load_data()

        #print("failed to create file data.")


	if "total_games" in data:

		total_games = data["total_games"]
        
		total_games += 1
		print("You have now run this program", total_games, "times.\n")
        # save data
		data["total_games"] = total_games
		save_data()
	else:
		print("total games not detected.")
        #try:
        #    data["total_games"] = 0
        #except:
        #    print("couldn't set games turns to zero.")	
		try:
			total_games = 0
			data["total_games"] = total_games
			save_data()
			print("This is your first game\n")
		except:
			print("couldn't set total games to data\n")
            #load_messages()
            #give_message()

def menu():
# adding a menu function
	choice= input("What would you like to do? \n [g]enerate a story? \n add a [c]haracter?\n add an [e]vent,\n or add a [r]esolution?\n")	
	if choice == "g" or choice =="generate" or choice == "generate a story":
		print ("rolling up a story...")
		time.sleep(1)
		roll_story()

	if choice == "c" or choice =="character" or choice == "add a character":
		print ("you are now adding a character...")
		time.sleep(1)
		add_character()

	if choice == "e" or choice =="event" or choice == "add an event":
		print ("you are now adding an event...")
		time.sleep(1)
		add_event()

	if choice == "r" or choice =="resolution" or choice == "add a resolution":
		print ("you are now adding a resolution...")
		time.sleep(1)
		add_resolution()

def roll_story():
	global data, character, event, resolution

	roll_character()	
	roll_event()
	roll_resolution()
	# now we'll do the same thing for events
	print ("The character is", character, "the event is", event, "and the resolution is", resolution,".\n\n")

# new function to roll character

def roll_character():
	global data, character

	characters = data ["characters"]
	character= random.choice(characters)
	print ("This story is about", character)

	# Adding another function: ask if the user wants to keep this character or not. If so, continue, and make a copy of the character in the data. If not, then delete the chacter the character from the list, and choose another.

	answer= input ("Do you want to use this character? y/n")
	if answer == "y" or answer == "yes":
		# we need to make add another copy of the element to the list.
		data ["characters"].append(character)

	if answer == "n" or answer == "no":
		# I want to have the program check and see if there are other copies of the character, and if not, give a warning.

		population = data ["characters"].count(character)
		print ("The number copies of that character is", population)

		if population == 1:
			answer = input ("are you sure you want to delete the last copy of this character? y/n")
			if answer == "y" or answer == "yes":

				data ["characters"].remove(character)
			else: 
				print ("The charcater is spared absolute destruction.")

				#eventually, I need to make the rolls for charcater, event, etc. seperate functions, so I can call them without restarting the story roll.
		else: 
			data ["characters"].remove(character)

		roll_character()

def roll_event():
	# cut and pasted from roll_character, finding and replacing character --> event

	global data, event

	events = data ["events"]
	event= random.choice(events)
	print ("The main event in this story is that", event)


	answer= input ("Do you want to use this event? y/n")
	if answer == "y" or answer == "yes":
		# we need to make add another copy of the element to the list.
		data ["events"].append(event)

	if answer == "n" or answer == "no":
		# I want to have the program check and see if there are other copies of the event, and if not, give a warning.

		population = data ["events"].count(event)
		print ("The number copies of that event is", population)

		if population == 1:
			answer = input ("are you sure you want to delete the last copy of this event? y/n")
			if answer == "y" or answer == "yes":

				data ["events"].remove(event)
			else: 
				print ("The charcater is spared absolute destruction.")

				#eventually, I need to make the rolls for charcater, event, etc. seperate functions, so I can call them without restarting the story roll.
		else:
			data ["events"].remove(event)

		roll_event()

def roll_resolution():
	global data, resolution

	resolutions = data ["resolutions"]
	resolution= random.choice(resolutions)
	print ("The way this story resolves is", resolution)

	answer= input ("Do you want to use this resolution? y/n")
	if answer == "y" or answer == "yes":
		# we need to make add another copy of the element to the list.
		data ["resolutions"].append(resolution)

	if answer == "n" or answer == "no":
		# I want to have the program check and see if there are other copies of the resolution, and if not, give a warning.

		population = data ["resolutions"].count(resolution)
		print ("The number copies of that resolution is", population)

		if population == 1:
			answer = input ("are you sure you want to delete the last copy of this resolution? y/n")
			if answer == "y" or answer == "yes":

				data ["resolutions"].remove(resolution)
			else: 
				print ("The resolution is spared absolute destruction.")
		else:
			data ["resolutions"].remove(resolution)

		roll_resolution()


def add_character():
	global data
	
	new_character= input ("describe the character please. \n")
	print ("The new character is", new_character)
	data["characters"].append(new_character)
	for i in data["characters"]:
		print (i)
	save_data()
	time.sleep(1)
	menu()
	

def add_event():
	global data
	
	new_event= input ("describe the event please. \n")
	print ("The new event is", new_event)
	data["events"].append(new_event)
	#for i in data["events"]:
	#	print (i)
	time.sleep(1)
	save_data()
	menu()
	
def add_resolution():
	global data
	
	new_resolution= input ("describe the resolution please. \n")
	print ("The new resolution is", new_resolution)
	data["resolutions"].append(new_resolution)
	#for i in data["resolutions"]:
	#	print (i)
	save_data()
	time.sleep(1)
	menu()

# And now to save.
def save_data():
	global data
	with open("game-data/data.JSON", "w") as wf:
		json.dump(data, wf)


if __name__ == "__main__": 
	intro()
	load_data()
	menu()
	save_data()