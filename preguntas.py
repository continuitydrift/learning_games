#Question Game
#Simpler, Spanish Version


## Steps
### load questions x
### ask question
### if right, continue
### if wrong, die.

import os, random, time, json



def load_vocab():
	global vocab
	if os.path.isfile("vocab.json"):
		print ("vocab file exists")
		try:
			with open("vocab.json", "r") as readfile:
				vocab = json.load(readfile)
		except:
			("couldn't load vocab from file.")
	

def ask_question():
#	global vocab
#	for i in vocab:
#		print(i)
#	for key,val in vocab.items():
#		print (key, "~>", val)
	word=random.choice(list(vocab.keys()))

	print (word)
	ans=input("what does that word mean in English?")

	print ("The right answer is", vocab[word])
	response=input("were you close? y/n")
	if response==("y"):
		ask_question()
	

if __name__ == '__main__':
    load_vocab()
    ask_question()

