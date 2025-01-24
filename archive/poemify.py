import random, os

# TODO
##### ABOUT: This file will display a short poem based on continuity variables within the program. Then it will prompt the player for a text file, and then produce a poem based on that file. The poemify file/module will be able to:
## Uncomment main poemify function
#### read through file
### create poem as a class
###### full functionality

lines=["For any list like this one, the implicit sorting algorithm should be best to worst.","The spirit of the school in Ollantay was learning by doing, experimenting, using whatever materials came to hand.","I have always been curious about the use of languages, both human or programming, and how they are used in various environments. While the study of literature and culture may not seem to be directly related to entry-level information technology work like writing lines of Javascript, I would argue that a close reading of texts requires an understanding the codes used (and the libraries referred to). In addition, 'soft' skills like group colloboration and public speaking, transfer across occupations.","Experiences in my life or career where I could have used a certain type of technical knowledge has motivated me to learn new tools, languages to leverage and contribute to open digital information.","This is a hidden message, sent from the morning into night. There are umbilical codes to cut.","The pattern for these lines should be clear, just by reading them as a list. They are meant to be the main bones of the selective process, the best memes that have wormed their way inside an internal list. These lines won't be able to be changed within the program, but must be altered in the program file directly."]

# So now we have a variable called "lines".

if __name__ == "__main__":
	print ("Welcome to Poemify, a program to turn text files into poems.")
#text_file=random.choice(text_files)
#raw_text_file= open("drift.txt", "r")
	answer= input("what text do you want to poemify?")
	raw_text_file=open(answer, "r")

	print ("this is the raw read of the text file: \n\n")
	text_file=raw_text_file.read()

# current_meta=


def write_poem(length):

	def write_poem(length):
		key_phrases=["noise into the signal.","Whenever a new file is created this text will appear.","sybiosis, parasitism, all of the other strategies for survival all play a symbiotic role in a meta-sense, for they contribute to a fully articulated landscape.", "It is nice, sometimes, to have these signal tower sideways sidescraper or shape ship launch, a side-scrolling new high score.","This is a minimalist python script, but it might be worth adding a if __main___ or whatever file.","A meta-game could be how long of a list you can make without breaking it, to later be assuaged into a more JSON friendly format.","So yes, what if one of these microcasting delinquints.", "An epic line, of a length where much of it is lost in the clouds of soft wrapping.", "each poem, of course, should start as a class object with certain default attributes. One of the functions, maybe even the first function, should be generating a meta-poem in the game files folder.", "What if the convention became that the ultimate position in a list was the most verbiose, had sank the deepest into the blind oceanic clue. The chances of the expansive text coming up could be weighted or normal, but it would mean that a hexagon could benefit the player upon multiple explorations. The game could be geared towards rewards for defending territory."]

		title=random.choice(key_phrases)
		print ("the title of the poem is", title)
		meta_poem=[]
		print ("attempting to write poem")


		try:
			n=0
			while n< length:
				line=random.choice(key_phrases)
				meta_poem.append("\n")
				meta_poem.append(line)
				n+=1
			for i in meta_poem:
				print (i)
		except:
			print ("failed to write a poem from key_phrases")

		print ("trying to save poem")
		try:
			with open("game-data/meta_poem.json","w") as outfile:
				json.dump(meta_poem, outfile)
		except:
			print ("couldn't dump file.")

	write_poem(6)


def poemify(text_file):
	sentences=[]
	phrases = []
	#with open(text_file, "r") as rf:
	#	for sentence in rf.read().split("."):

	for sentence in text_file.split("."):
		sentences.append(sentence)
		for phrase in sentence.split(","):
			phrases.append(phrase)
	#for sentence in sentences:
	#	print (sentence)
	#for phrase in phrases:
	#	print (phrase)
	key_sentence=random.choice(sentences)
	print (key_sentence)
	print("\n")
	for line in range (1,6):
		line=random.choice(phrases)
		print (line)
	print("\n")
	print (key_sentence)


if os.path.isfile("game-data/meta_poem.JSON"):
	print ("file found, attempting to load data...")
	try:
		if os.path.getsize("game-data/meta_poem.JSON") > 0:
			print ("meta_poem bigger than zero.")
			with open("game-data/meta_poem.JSON", "r") as rf:
				for i in rf:
					print (i)
		else:
			try:
				write_poem(4)
			except:
				print ("calling the write_poem function didn't work.")
	except:
		print("either failed to read or write poem.")
else:
	print ("meta poem file not found. attempting to create.")
	try:
		meta_poem = open("game-data/meta_poem.JSON", "w")
	# Classic escape scenario. A free write on a single line, one of the things that could break a poemify program that didn't break things up further than lines. The long term arrow for this poemify program would be to tie it into some rudimentary form either of machine learning or crowd sourcing. It can be a bookmark or loadscreen for other games, including the writing game, once I get that working again. While my focus will be on Ishtar, there isn't any reason not to stretch narrative muscles in a way that will improve my raw word count, if not my score once adjusted for multipliers. In the game-data file, there should be a file called word_scores.json. Same deal, with checking if it is there, and creating it if it is not.




	except:
		print ("failed to create file meta_poem. However, even failures are opportunities to develop a story. What can this outcome signify about what will be at stake for future editions of the story or poem?")

# CALL
poemify(text_file)

# The last line of the program will be calling the function.
