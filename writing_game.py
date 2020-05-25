#writing game

##version 3.7


### |-------|   ____          -____     ____
###     |      /    \         |    \   /    \
###     |     /      \        |     \ /      \
###     |     \      /        |     / \      /
###     |      \____/         |____/   \____/

# restore basic funcitonality

## this game, at its core, is designed to make writing more fun. One of the unspoken assumptions is that writing has value. Another is that the writing game is as much a state of mind as anything, and therefore is really only keyed to an individual personality/associative matrix--my own.

### In order to advance to version four, A user must be able to
#### -load or create a data sheet.

#### set a goal of EITHER time spent writing, words to write, or wpm.
#### -have daily/game statistics saved in a file, along with the date.

### incorporate features from dev.py


readme="The writing game functions at a pseudo-level. Even when the code is completely broken, it is still possible to play the game simlply by reading through and then adding to this file. The text, in its plain versions, can be printed out by a print function. \n Variables hidden in the drift can resurface, randomly or with changes to the superficial codes."

def print_text():
    print (readme)
    print (text)
    print (side_quest)


# The print_text function can run at the beginning of the program. For this read-through, I am trying to generate 600 new words before 10:00, when I will change the stream info and start playing the table top role playing game Ironsworn.



# todo=["check loading mechanism","meta-rules","add story elements", "write journal"]

## make it so that you can add story elements.

text="An ecological utopia one hundred years in the future. One where the physical world may be falling apart, but as a response to environmental pressures social organizations evolved to be functionally efficient. Ironically, an alternative future would have ideal phsycial conditions but a paranoid, dystopian social structure."

# players should be able to enter in a target file, and get a wordcount.


meta_rule="You should be able to work your way through the file in one pomodoro, adding a small improvement with each pass. At the same time, reveling in the colors, the ability to create variables that are never called, to dance hobnatic and pandramatic."

### players should be able to see their score (words/minutes), as well as their average score.

#### If score > average:
    # win
### in the first iteration of this game, the only permanence/continuity is the text file

#### working one-shot (sprint) scoring system.


import random, json, os, time, math, matplotlib

#matplotlib has to be installed in order for this program to work.

#import timer.py as timer

import matplotlib.pyplot as plt
import numpy as np
#from error import *
#import enter_quotes.py

# CONTINUITY DRIFT ~ Lambent was gone. In his place was this woman, whose body Yillah had been intimate with, but whose mind she'd never met before. Whoever she was, though, must have a cognitive map simlilar to Lambent's, or they wouldn't have been compatible.

#spells:
#- open new folder
#- open new file
#    cost:
#- close file
#    cost: record for the longest line in the file.
#- close folder


words=[]
high_score=0
total_turns=0
average_score=0
sum_scores=0
sum_total_words=0
sum_total_minutes=0
turns=[]
main_file = "writing_game.py"




play_again = True

# That was the start of it, Yillah thought. The wanting to be alive, the weight being thrown into life rather than death. Existince as opposed to absence. Words instead of silence. Colors instead of grey.

# "All I ever wanted was to pick apart the day / put the pieces back together my way." --Aesop Rock

def plot(turns, words):
    #This below, right here, is something that I've forgotten how to do. Drawing attention to hull breaches of knowledge can be done by adding narrative or fictive text as ancillary comments.

    fig, ax = plt.subplots()
    #For the next twenty five (more like twenty, now) minutes, I am playing the writing game against itself, using the code as the file it is reading to determine word count. It will, I imagine, be able to meausre commented out words. Contributing to the health of the ecology and meme-spheres.

    ax.plot(turns, words)
    #The dark regions can breed textual monstrosities that collaborate for survival, not just symbiotic but probiotic.
    #   "Hi," the man says, stopping a polite distance away.
    #   "Hello," you answer, hiding what you were doing. The man pretends not to notice, looking down stream.
    #    "I'm the game ward," he informs you. "No," he answers, when you ask if he doesn't mean game warden.
    #    "Can you tell me how to get to the next level?" You ask.
    #    The game ward smiles, looking up at the island of drifted maze above your heads. "Always the same game, isn't it. You are searching for power, artifacts, love. As a general rule, you need to have no more than six comments between lines of code, and every time you read them you should try and make them better."
    #   You squint up at the labyrinth, draped in vines and the remnants of old ladders. Untold treasures, unspeakable danger.

    ax.set(xlabel='turns', ylabel='words',
           title='writing_game')
    #    The thing is that the game is set up to plot things as turns. The next step could be to key turns to a date somehow, or even a persistent count. Some way to compare written output over days instead of turns within one run of the program.
    #    "So the next level, in this case," you hear the game warden say, not out loud, but telepathically, "would be to have the game read and save a JSON file called word_counts.JSON, which would have the date on the x axis, and number of words (for that day) on the y axis. For extra points, you could try to have a different plot for the total words, either for the game or for a particular project."
    ax.grid()
    #    There are six character archetypes, and six different genres, from which to chose. The healer, thief, warrior, ranger, druid, and mage. Meta-game, far future, near future, recent past, distant past, prehistory.
    #     Gradually, there emerge an ecosystem of files, with funtions that can be swapped back and forth.
    fig.savefig("test.png")
    #    Healer in the meta-game. "No," she says, "don't let it be any less important than other continuities."
    #   so the scenery steps forward, the dropped backs called curtains
    #   The long term, persistent writing goal to stay alive would be to write more than the day before.
    #    Or to meet some kind of a minimum, say 600 words, or that character meets some kind of end determined by a list of fatal incidents.
    plt.show()
    #    Every archetype should have a particular playstyle. The healer mostly tries to wait out battles, absorbing damage and replenishing health. Healers are unique among character backgrounds in being able to transmute mana directly into health.
    #    Try, then, to keep the game running, with the druid, who extrudes roots out into other branches of file systems. As above, so below.
    #    Spells 6-resurrection 5-necrotic rot 4-fungal bloom 3-enhance growth 2-heal major wounds 1-heal minor wounds.
    #    At the end of the day, there could be some kind of a results round.


def get_word_count(text_file):
    word_count=0
    #ans=str(input("what scroll do you unroll? "))
    #with open(ans, "r+") as rf:
    #    for word in rf.read().split():
    #        word_count+=1
    #word_count=0
    with open(text_file, "r") as rf:

        for word in rf.read().split():
            word_count+=1
    print ("If you are reading this, then it means that the get_word_count function has been called. The text file it was called on has", word_count, "words.")
    #Idea: Character Level depends on word count.

journal_text = "There was a white guy at Chip's, who started talking to me while I was leaving and he was arriving. A cave explorer, lived near Huatla. Lived in Mexico part of the year, it seemed like. Talked about how unsafe the area was where he lived."


def turn(text_file):

    argument="A turn in the writing game. Ideally, there should be a way to enter the time manually, and the word count, or rely on the program."
    global high_score, total_turns, average_score, sum_scores, sum_total_minutes, sum_total_words, play_again
    #play_again=True
    score=0

    #sum_score escapes to the global level, while score is eternally born again at zero, with every turn of the wheel.
    total_turns+=1

    print ("It is now turn", total_turns,"\n")
    keys=[0,1,2,3,4,5,6,7]
    key_field=[]
    for i in keys:

        #print (lines.index(i))
        magnifier= keys.index(i)
            #print ("will be used to generate copies. Populations multiplied by magnifier in the new list.")
        count=0
            #oh, or the first one isn't even shown. I kind of like that.
        while count<magnifier:
            key_field.append(i)
            count+=1
    key = random.choice(key_field)

    genres=["fantasy","meta", "horror", "tragedy", "comedy","science fiction", "allegory", "epic fantasy", "solsticial" ]
    genre=genres[key]
    print ("This story is", genre)

    try:

        # checking to see if the data file exists.

        if os.path.isfile("game-data/data.JSON"):
            print ("file found, attempting to load data...")
            with open("game-data/data.JSON", "r") as rf:
                pass

# Improvisation, while facilitating a heightened sense of being in the moment, can also be a way of escaping the narrow confines of present experience, allowing the mind to cast back over itself, at least since the designation beginning of the scene or performance, pursuing threads or connections distributed over time and conceptual space.


        else:
            print ("data file not found. attempting to create.")
            #try:
            #   data = open("game-data/data.JSON", "w")
            #   os.mknod("game-data/data.JSON")
            try:
                data={"character": "drift", "background": "dimension mage", "location": "library"}
                with open("game-data/data.json","w") as outfile:
                    json.dump(data, outfile)

            except:
                print ("couldn't create data.JSON")
    except:
        print ("didn't work.")

# same thing for stories.json

    try:
        if os.path.isfile("game-data/stories.JSON"):
            print ("file found, attempting to load data...")
            with open("game-data/data.JSON", "r") as rf:
                data = json.load(rf)
                for i in data:
                    #print (i)
                    pass
        else:
            print ("stories file not found. attempting to create.")
            #try:
            #   data = open("game-data/data.JSON", "w")
            #   os.mknod("game-data/data.JSON")
            try:
                stories={}
                stories["hooks"]=[]
                with open("game-data/data.json","w") as outfile:
                    json.dump(stories, outfile)

            except:
                print ("couldn't create stories.JSON")
    except:
        print ("didn't work.")
   # hooks=


    #Comments can by convention compete for their greenness. There is comfort in the underground, an expansive hypotheticality. This collection of poems, harvested by a filter, randomized at several parts.

    try:
        print ("Okay, we're going try some tests. First of all, let's see if there is a key.")
        print ("the key is ", key)
    #

        with open("game-data/data.JSON", "r") as rf:
            data = json.load(rf)
            #for i in rf:
            #    print (i)
            for i in data["hooks"]:
                print ("There is an entry for the hook", i, "in the data file.")
            #for i in hooks:
            #    print (i)
        #let's see if we can read from rf
            hooks =data["hooks"]
            hook=hooks[key]
            print ("The hook for this turn is", hook)
            openers=data["openers"]
            opener=openers[key]
            good_endings=data["good_endings"]
            good_ending=good_endings[key]
            bad_endings=data["good_endings"]
            bad_ending=bad_endings[key]
    except:
        print ("Something failed in assigning data.")




#The better way to do this, of course, would be to have a dictionary. In fact, don't I already have a .json file for stories?

    ##bad_endings not complete, nor called.


    #pretwists and postwists added 6/7/2019
    pretwists=["and then","\n\n","the strange thing was", "in much the same way, and yet with this new intrusion of chance direction, the life of the protagonist continued.","Thus small hatchlings of future game-space, beetles of non-capricious carapace."]
    pretwist=random.choice(pretwists)

    twists=["should these stay in the writing game file itself, as permanent, meta-elements?"]

    twist=random.choice(twists)

    postwists=["After that, everything was different","A briefly human bloom","returning"]
    #print (twist)

    #alt_end=random.choice(alt_ends)
    #    Here, as undertones to these calls, can exist auditions for inclusions in alt_ends.
    #print (alt_end)
    #pretwist=random.choice(pretwists)
    print (pretwist)
    #new
    twist=random.choice(twists)
    print (twist)
    postwist=random.choice(postwists)
    print (twist)
    #alt_end=random.choice(alt_ends)
    #print (alt_end)






    #meta_high_score=25
    #

    with open(text_file, "r") as rf:
        word_count=0

#     one of the things making videos can do is to take advantage of the practive ground, the area secrely in the drift.

        for word in rf.read().split():
            word_count+=1
    print ("That file has", word_count, "words.\n", opener)
    if word_count>60000:
        print ("This is currently the highest level a file can reach, the fourth.")
    elif word_count>2400:
        print ("There are now more than 2,400 words.")
        print("This is a third level file.")
    elif word_count>1200:
        print("There are more than 1,200 words. This file has reached.")
        print("second level.")
    elif word_count>600:
        print ("This is a first level file, with fewer than 600 words. The setting is still only sketched in pencil, and the character's wander around in a daze, their masks damaged.")
    else:
        print ("this file has fewer than 600 words.")


    time_goal = int(input("There is no harm in providing an impetus for expansion by alleviating redundancy and boredom. Ruptures occur, rewrites. New players emerge in the game. How many minutes would you like to spend in the drift?"))
    word_goal = int(input("How many ideoforms can you add to the scroll (how many words can you write)?"))
    start_time = time.time()
    print (hook)
    turns.append(total_turns)
    words.append(word_count)
    plot(turns, words)
    str(input("press enter when done"))

#####   RESULTS
## The meta game, where you are measuring the word count of this file, goes backwards on the second read-through, setting up goals for each turn/function.
##  within 25 minutes, what is possible? What have you been able to do in that length of beat in the past, a pulse of heavy attention.
#   1. Make a simple image with six layers.
##      a. accent
##      b. text
##      c. frame
##      x. pen
##      y. highly rendered
##      z. video
#   2. Write 600 words
#   3. Edit 12,00 words
#   4. Scavenge Files
#   5. Read
#   6. Focus


    total_time = time.time() - start_time
    print ("Your total time was ",total_time)
	#working_text = open("pseudo_text.txt", "r+")
    new_word_count=0
    with open(text_file, "r") as rf:

        for word in rf.read().split():
            new_word_count+=1
    print (text_file, "now has", new_word_count, "words.")
            #new_word_count+=1
    word_difference = new_word_count - word_count
    total_minutes = math.ceil(total_time/60)
    sum_total_minutes+=total_minutes
    sum_total_words+=word_difference

    print ("You wrote ", word_difference, "new words in", total_minutes, "minutes")
    score=math.ceil(word_difference/total_minutes)
    #print ("the high score is", high_score)
    print ("You wrote", score, "words per minute. Your score is", score)

    ####data to plot
    turns.append(total_turns)
    words.append(new_word_count)
    plot(turns, words)
    #the plot thickens



#    total_turns+=1
    #else:

    #if sum_scores in globals():
    #print ("globally store sum_scores is", sum_scores)
    #else:
    #    print ("the global ecosystem is without a viable population of sum_scores.")

    #if sum_scores in local():


    if total_minutes > time_goal:
        time_diff= total_minutes-time_goal
        print ("You exceed your time goal by", time_diff, "minutes!")
        roll = random.randint(1,6)
        score=score+roll
        print ("Now your score is", score)
        print ("The way the game works now is that a random roll is added to the initial score/word count")

    else:
        print ("You did not meet your time goal! Score lowered by 1d6.")
        roll = random.randint(1,6)
        score=score-roll
        print ("which makes your score", score)

    if word_difference > word_goal:
        over_goal=word_difference-word_goal
        print ("You exceeded your word goal by", over_goal, "words!")
	#	stats["xp"]+=1
        roll = random.randint(1,6)
        print ("As a reward for meeting the goal, a random number of points between one and six will be added.")
        score=score+roll
    else:
        print ("You did not meet your word goal! Subracting 1d6 from score.")
	#print (sent_list)
			#for i in range(roll):
        roll = random.randint(1,6)
        score=score-roll
            #I like that I keep these dice lying around.
    print ("Your final score for this turn is", score)

    if score> high_score:

        high_score = score
        print (high_score, "is the new high score!")
        print (good_ending)
    else:
        print ("Sadly, you did not beat the current high score, therefore, your story ends badly.")
        print (bad_ending)

    print ("the total words you have written are", sum_total_words)
    print ("in all you have written for", total_minutes, "minutes")
    sum_scores+=score
        #wait, score should reset to zero after this.
    #else:
    #    sum_scores=score

    average_score=sum_scores/total_turns
    #right?
    print ("In", total_turns, "turns, your average score has been", average_score)
    ans=str(input("play again?"))

    ## a seed-bearing epilogue. The gnoll wandered through the grass, knowing he could catch up to the rest of the party later.

    if ans =="y":
        play_again=True
    else:

        play_again=False
        #quit()



#  ################_#_###_########################
#  #__######___#__(_)#|_(_)_#__###__#_############
#  #\#\#/\#/#/#'__|#|#__|#|#'_#\#/#_`#|###########
#  ##\#V##V#/|#|##|#|#|_|#|#|#|#|#(_|#|###########
#  ###\_/\_/#|_|##|_|\__|_|_|_|_|\__,#|###########
##############======|_________________/
#  ##########/#/##\#\############
#  #########/#/####\#\############################
#  ########/#/######\#\###########################
#  #######/#/########\_\##########################
#  ######/#/######################################
#  #####/#/#######################################
#  ####/#/########################################
#  ###/_/_##__#_#_#__#___###___###################
#  ##/#_`#|/#_`#|#'_#`#_#\#/#_#\##################
#  #|#(_|#|#(_|#|#|#|#|#|#|##__/##################
#  ##\__,#|\__,_|_|#|_|#|_|\___|##################
#  ##|___/########################################
##############################version 3.6#########

#roll = random.randint(1,6)
#t

text_file="writing_game.py"
#print ("temporarily, for testing purposes, making the text_file automatically this one.")

side_quest="I recorded myself reading through this file, and the final thing I'll do is add this variable to the print_text function. For now, and until the Todo list is completed, the text file used for word counts is the progam itself.\n In addition to the goal of swimming again in pythonian syntax, I wanted to reinstate the mechanics of Telos. You, @, are a magician. Runeshadow, a blend of everything I love. You and I, after our quest is complete, may switch characters.\nMy goal, perhaps, is simpler than yours: to kep you safe. By which I mean write a lesson plan for today. Two pomodoros, like this one, should be sufficient. This will give us an extra roll.\nMy stats are a:6,s:5,h:4,d:3,r:2,m:1. Yours are a:1,s:2,h:3,d:4,r:5,m:6.\n'We are the most basic archetypes,' you say. 'The reader and the writer, lovers whose love has transcended into practical concerns and information."

print_text()


#str(input("The pseudo-ghost squirms into the smallest lines of code. /n what scroll do you want to open? "))
play_again=True
while play_again==True:
    text_file="writing_game.py"
    turn(text_file)

    ## when playing the meta-game, when you reach the end of the file you work your way backwards, function by function, room by room.

    ## your quest this time
    ## is you add 600 words to this file.

    ## This itself can be a kind of show, a performance. You score yourself, based on your goals, between one and six. The writing file, the text file, whichever one you use in the writing game, is not the permenant home or destination for the words that you create.

    ## For example, after I fail or meet the challenge of 600 words that I set myself in this stream/iteration, I will cut and paste the text below into a file I'm creating for IRONSWORN.

    ## It's 10:08 on a Sunday. There are ways of spending my time that would probably serve the coin-gatherer version of myself more than broadcasting random streams into the internet, but the hypothesis on which these games proceed is that everything is connected.

    ## The crucial stat, the feedback most relevant in a creative/biological system, other than simple breath, is enthusiasm. Learn how to maintain focus, and slowly climb the turtle-steps of goals, and everthing else will have already followed.

    ###  IRONSWORN

    ## Adda

    ### She fell the forest floor, exhausted by becoming, for hours of moonlight, something roots extending directly into the Earth. She had felt an unmitigated closeness to the soil, rife and rambling with generation and decay.
