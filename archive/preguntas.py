#Preguntas
#Simpler, Spanish Version

## To Do
### keep track of score


## Steps
### load questions x
### ask question
### if right, continue
### if wrong, die.

import os, random, time, json

score=0
high_score=0

def load_vocab():
	global vocab
	if os.path.isfile("vocab.json"):
		#print ("vocab file exists")
		try:
			with open("vocab.json", "r") as readfile:
				vocab = json.load(readfile)
		except:
			print ("couldn't load vocab from file.")
	else:
		print ("vocab.json doesn't exist.")
	

def ask_question():
	global score
#	for i in vocab:
#		print(i)
#	for key,val in vocab.items():
#		print (key, "~>", val)
	word=random.choice(list(vocab.keys()))

	print (word)
	ans=input("what does that mean in English?")

	print ("The right answer is", vocab[word])
	response=input("were you close? y/n")
	if response==("y"):
		score+=1
		print ("your score is", score)
		ask_question()
	else:
		end_game()

def end_game():
	global high_score, score
	print ("your score was", score)
	if score>high_score:
		print ("You have acheived the high score!")
	ans=input("Do you want to play again? y/n")
	if ans=="yes" or ans=="y":
		score=0
		ask_question()

def turn():
#	global score
	ask_question()	

if __name__ == '__main__':
    load_vocab()
    turn()
   

