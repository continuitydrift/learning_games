

 # This is a program that I will add functionality to over time, in order to provide tools for writers (well, ok, me) to record their activity and motivate them to be more productive.

# Get beyond the primary dichotomy of public or private, allowing the intentionality of one to bleed into the other. Same with friendships, communication, and publication. There are wide grey swaths.

# The game will keep track of the amount of words a player writes, in this or a seperate file, either by counting the words automatically, or accepting imput from the player.

#

#  It is easy to see when I have been working for 25 minutes. The six different videos could be edited into a larger video, where the result (a text file, or image) could be shown in the background, progressing at six times the normal speed, while the six turns could appear in seperate windows.

# Complexification, in the game, has to be earned through succesful iteration of a quest or task of lesser difficulty.


# TODO:

## read through the entire program once. An end goal would be to have sufficient comments that someone who doesn't know or has forgotten how to code the game would be able to figure it out.

### I looked through the online information about literate programming, and couldn't find a free copy of the book. I figure it would be better to learn from trying to use the successors. I'm only interested in anything that is open source.


## poemify the drift

# Optional Rules

## within the writing game, there are six different possible texts, of ranked significance. for example:

### personal statement
#### game text

#### The discoveries these words are hiding are as much of a transmission from the synchronic otherwhere. This is even before the start. This is before the framework, the hexagonal grid, has been imported.
##### A rabbit appears, from the ditch.


# The first thing I need to do is import libraries I will need

import os, json, time, random
import os.path
from os import path
from datetime import date
from quotemachine import *

#
#               _|                            _|
#     _|_|_|  _|_|_|_|    _|_|_|  _|  _|_|  _|_|_|_|
#   _|_|        _|      _|    _|  _|_|        _|
#       _|_|    _|      _|    _|  _|          _|
#   _|_|_|        _|_|    _|_|_|  _|            _|_|
#
#

def start():

    ##  I can imagine a program where there are super-long comment lines, so without word wrap the vertical length of the file is dramatically shortened.

    does_data_exist()

    # this also loads the data. Meta and the Harlequin looked out over the poorly-drawn landscape, one with an invitation of wet media, splotches yet to be dropped as chaotic ink. The different levels shifted according to their depth.

    # you've been playing

    ## in thoughtless and careless keys, like a piano melody turned trite with repetition and commercial association.
    ## get the data, sure, but what data, and to what end?

    get_records()

    # Meta turned the mechanism on the cover of the book, with its pages of alien thinness and durability. She tended to find objects of extradimensional origin.

    # "Do you think it is appropriate for comments to try and be funny, or whimsical?"
    # "No," he answered. "Generally, no. There is a...implicit appreciation of elegance, of minimalism, compression, antithetical to, I think, a more artistic sense of fun."

    new_record()

    # There should be a mode, eventually, where you can get rewarded for editing. For now, though, the task is to find where there might be a bug in the file that causes the starting word count to be overestimated, or the score to be underestimated.
    # The reward for fixing it will be a weapon or shield of your devising.

    mask()


    menu()

#       this function will bring up the option to burn the archive (wipe records), or start a turn.


# The artifacts are back. They need to be worked, somehow, into the mythos, sesrvants of duchess of aphasia.
#
#    get_word_count()


    #except:
    #    print ("You fail! The cost is to write an error message better than this one.")

    create_record()
    save_data()

def does_data_exist():
    global data
    # I'm making this it's own function

    if os.path.isfile("data.JSON"):
#        print ("congratulations, data file exists!")
        pass
        # File exists, so checking if data size is > 0

        if os.path.getsize("data.JSON") > 0:
# checks if data file is not empty.
#
            pass
        # if so, opens and loads data
        # this logic gate has yet to be built.
        # a bridge intersecting with other bridges, zooming out, until
        # the mask file emerges, that run by the river, when I was working the idea of a future without the ears and mind I had become accustomed to a flaring proximity with.


        load_data()

        # I hereby for all perpetuity of my trying to write code the load_data() function, at least in theory, a kind of universal or meta-level spell.

        # At a meta-level, then, where is my character, and who are they? What mask did they choose from the hall of heroes?

        # The Captain.



    else:
        print ("data file does not exist.")


        #monster attack. The monster is 12: not a monster at all but a friendly NPC, 11-10: weak monster - high loot, 8-9: powerful monster - high loot 6-7: monster grows on death, 4-5: powerful monster-low loot, 2-3: two monsters.

        data = {}

        # 2d6 roll was an 8. A powerful monster can generate with an item that grants them +1 to one of their stats. Rolling for that stat now.

        # random note ~ I finally got the writing game to recognize a text other than the drift. Hopefully this will show up as new words.

        save_data()

#        I rolled a three, so that would be an artifact that grants +1 health for as long as it is equipped. Let's say this is a golem with a ring of health. ["golem", a:6,s:6,h:3,d:1,r:4,m:4,inventory: +1 ring of health, xp: 1]

def get_word_count():

    # Combat starts with a roll for distance. I rolled a 1, so that means that, for some reason, we start in close combat. Perhaps the golem was a statue activated by proximity.

    global today, word_count

    # Next I need to determine the turn order, which is just a comparison of speed [an alternate rule could add a role or virtue score here]

    word_count=input("How many words did you write?")

    # Capitano's stats are ["capitano", a:6,s:4,h:5,d:3, r:2,and m:1. i: [sword, +1 ring of health], xp:5] and the golem's are ["golem", a:6,s:6,h:3(4),d:1,r:4,m:4,inventory: , xp: 1]
    print ("you wrote", word_count, "words this turn.")

    # The golem goes first and it is within range. It attacks and rolls a 2, which added to it's attack score of 6, gives it an 8. My defense is 3, and I'm going to take a virtue score instead of a roll. I need a five or better to defend without losing any health.

    # I succeed. It is the Captain's turn to attack, which they do with the sword.

def get_records():


    global data, records

    # Capitano attacks. They roll a 2. With an attack score of 6, +1 from their magic, +1 from the sword, that is a total of 10. Golem rolled a 3, and they only have a 1 defense. So 10-4 is six, enough to destroy the golem, even with the ring of health.

    # ["capitano", a:6,s:4,h:5,d:3, r:2,and m:1. i: [sword, +1 ring of health], xp:5]

    if "records" in data:

        records = data["records"]
#        print ("I tried to create a variable from the records in data.")
        for i in records:
#            print (i)# if doesn't exist
            pass
    else:
        print("records not found.")
        try:
            records = {}
            data["records"] = records
            save_data()
        except:
            print ("You slip on the edge of the outer wall, and fall into the poison thorns.")

#    data = open("game-data/data.JSON", "w")
    #   os.mknod("game-data/data.JSON")
#    save_data()
#    load_data()

    #print("failed to create file data.")

#
#
#   _|_|_|      _|_|    _|      _|      _|
#   _|    _|  _|_|_|_|  _|      _|      _|
#   _|    _|  _|          _|  _|  _|  _|
#   _|    _|    _|_|_|      _|      _|
#

#
#                                                           _|
#   _|  _|_|    _|_|      _|_|_|    _|_|    _|  _|_|    _|_|_|
#   _|_|      _|_|_|_|  _|        _|    _|  _|_|      _|    _|
#   _|        _|        _|        _|    _|  _|        _|    _|
#   _|          _|_|_|    _|_|_|    _|_|    _|          _|_|_|
#
#
#

def new_record():


       # keep in mind the the game works at all levels, in all realities, all continuities. Once a character is created neither it nor its experience can be destroyed.

       # This stream is evidence--not on something as immutable as the blockchain, but, importantly, THEORETICALLY permanent, carried forward. This will be an important dynamic for the writing game as it evolves into a stronger gravitational well. For the moment, there is a convergence of two different, uncertain audiences. Those who might read this code on a github repository (highly unlikely), and those who might encounter this as a video stream (almost as unlikely.)


       # With this game, this stream, there is no wasted time. Mistakes are gathered, like the mast of ancient oaks, and boiled until palatable, until the tangled prose has homogenized into a mass of nutrients.

    global data, today

    # Today: the variability of stimuli

    # At base, at foundation, at the moss and loamy edge of a dichotomy, a break between the land and sky, a valuing and pursuit of variability.

    ## Music. Maybe above everything, above all metaphor, is the music. There is a horror story, about human subjugated to microbial, invisible, occupation.

    #  ["scapin", "a": 6,"s":6,"h": 1, "d": 1, "r":4, "m":5, "xp":1, "level": 1, "i":["touchstone":["mb":2],"scroll":["sab":1], "gp":0]]

    ## for this moment, this section, entertain the possibility that what I'm saying, despite the neck-bearded stupidity of the vessel from which it pours, has something of the nutrient savor of unmitigated/unanticipated truth.

    ## It is, I admit, a holographic performance. Any part could be substituted for any other part. That is the secret of the lazzi, as the disenfranchised doctor would whisper in the secret streets of Rome.

    ## Although this character is commented out, since I encounter him on this stream, according to the principles of fortuitous divination, Scapin the thief thief is initiated into the pantheon.

    ## What if there were a thief of language, one that lurked in the grainy videos of mismatched confessions, waiting and stalking the grass of truth. The blades that comforted his sleep with a thousand soporific cuts.

#    for i in data:
#        print (data[i], "is", i)

## Honor the logic that these fossilized functions afford. There is a data file. An arc of energies. Memory made slightly more sacrosanct by rote and repetition.

    ## The first thing that all memes call out is a desire to repeat, to clone themselves, to impose a rythym on a world still tuning, finding their instruments, waiting for a tune to emerge. Let there be sufficient energies cast by the thing that I am called to do, which is to send out these objects and verbs from addled fingers.

    # print ("You have set a new record, in that you have now played this game more total turns than you ever have before.")


    # theoretically, if I load data at the beginning of every function and save at the end, do I need data to be a global variable?
def get_turns():
    global data, turns
#try:
    if "turns" in data:
        print ("There are previous turns in the datafile.")
        turns= data["turns"]
        print ("you have played", turns, "turns")
        turns = turns + 1
        print ("This is turn", turns)
        data["turns"] = turns
        save_data()

    else:
        print ("no previous turns in file")
        data["turns"]= 0
        save_data()
        get_turns()
#except:
#        print ("well, you've isolated the problem. Data is missing")


#get_turns()

#    str(input("entering experimental zone!! press any key."))
def create_record():
    global data, turns, today
    try:
        get_turns()
    except:
        print ("couldn't get turns.")

    print ("this is turn", turns)

    data[turns]={}

    get_date()
#        print ("Just called the get_date function. Today's date is ", today)
    class Record:
        global today
        def __init__(self, date, words):
            self.date = today
            self.words = new_words

    turn_record = Record(today, 0)
    print ("turn_record.date is", turn_record.date)
    print ("words count is,", turn_record.words)
    print ("Okay, now I'm gonna try to enter the turn record into data.")
    this_turn_date=turn_record.date
    print ("this_turn_date variable is now", this_turn_date)

    data[turns]["date"]=str(this_turn_date)
    print ("within data there is now,", data[turns]["date"])
    print ("Now for words.")
    this_turn_words=turn_record.words
    print ("words for this turn are", this_turn_words)
    data[turns]["words"]=this_turn_words


#                data["records"][turns]["words"]=0
#                words_this_turn = data["records"][turns]["words"]
#                get_word_count()
#                words_this_turn = words_this_turn + word_count

#                print ("words for this turn is at", words_this_turn, "\n")
#                data["records"][turns]["words"] = words_this_turn
    save_data()

        #create_turn_record()
        #save_data()


#    except:
#        error_message()



def error_message():
    global data

# Here, at least, the code can relax, and tell some jokes. Let the reminder of mortality that running into an error induces flower into a garden of laughing plants.

    if "error_messages" in data:
        print ("error messages found in the data file. As follows...")
        for i in data["error_messages"]:
            print (i)

            ###### So far, I don't know if error_messages has ever been called. And yet, this root would grow into one of the main philosophies branching through the system--the creative embrace of the bugs, of glitches. The weird hauntings outside the scope of headphones. The earth, trembling.

    else:
        data["error_messages"] =["You seem to have made a critical error."]
        print (data["error_messages"])
        save_data()

##### The goal then becomes for this thread, this impulse of the drift, of destruction and reduction, of the glowering glow of entropic focus, the weeding and the winter, to survive.

#
#   _|                            _|
#   _|    _|_|      _|_|_|    _|_|_|
#   _|  _|    _|  _|    _|  _|    _|
#   _|  _|    _|  _|    _|  _|    _|
#   _|    _|_|      _|_|_|    _|_|_|
#
#
#         _|              _|
#     _|_|_|    _|_|_|  _|_|_|_|    _|_|_|
#   _|    _|  _|    _|    _|      _|    _|
#   _|    _|  _|    _|    _|      _|    _|
#     _|_|_|    _|_|_|      _|_|    _|_|_|
#
#

#

def load_data():
    global data

    #### The loading of data was kind of tribute to the ancestors. Sure, there were previous versions of himself, the glancing blows of curiosity that would gradually weakenhis resolve enough to overcome his egoistic fear of not being smart enough to understand the things that fascinated him.

    with open("data.JSON", "r") as rf:
        data = json.load(rf)

        for i in data:

            pass

#            print (i, "is", data[i])

#### Everything has to be echoed. The ancestors must have their due. Every time you look around this room, you see messages left by past versions of yourself.
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
    save_mask()


def save_mask():
    global character, data, masks
#    print ("Attempting to save the character data to mask file. Pray for us.")
#    time.sleep(2)
    print ("you are", character["name"])
#    print ("Now for the tricky part. Are you in masks?")
#    for i in masks:
#        print (masks[i])

    with open('../masks.json', "w") as outfile:
        json.dump(masks, outfile)
        print("masks saved!")

        ## Pseudo ghost

        ### as in pseudo-code, as in literate programming, translating everything, not just into human language, but into your language, the language that will most survive your mental decripitude in the future.

        ## trap door

        ### scene one, again. A repetition. The dottore gestures, frantically, at the bag of props. You ignore him.

        ### The 25th year high school reunion. Only a handful of people there. A football game. Monte E., who you remember as exactly as he appears now. An older version of himself. As you must be.

        ### "This must never be allowed onto Github," continuity says, and Drift nods, lazily. The more he can give away, the more points he can leave hanging out in the open, the more his point is made about the subconscious ruling over the supposedly soveriign fore-brains.

    time.sleep(1)

    print ("yeah, something went wrong.")
    error_message()

def get_date():
    global today
    today = date.today()
    print ("Today's date is", today)


#
#
#   _|_|_|  _|_|      _|_|    _|_|_|    _|    _|
#   _|    _|    _|  _|_|_|_|  _|    _|  _|    _|
#   _|    _|    _|  _|        _|    _|  _|    _|
#   _|    _|    _|    _|_|_|  _|    _|    _|_|_|
#
#

def menu():

    # The menu function can be a port of call for questing heroes. A place where massive amounts of experience can be gained.
    global data
    ans = str(input("what do you want to do? [b]urn the archive, start a [n]ew turn, or [e]dit a file?"))

# ~ Telepaths and Linguists

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
    if ans == "e":
        print ("algorithm is othering")
        edit()


#
#     _|
#   _|_|_|_|  _|    _|  _|  _|_|  _|_|_|
#     _|      _|    _|  _|_|      _|    _|
#     _|      _|    _|  _|        _|    _|
#       _|_|    _|_|_|  _|        _|    _|
#
#

def turn():
  

    # This , what I and you are doing now, is an example of a turn.
    ## TODO
    ### One of the things that I need to internalize is how transferable words and ideas are from file to file. I have a todo list open on this screen, in Sublime, and on the other, in Obsidian.
    ### Before a commit is made with the changes, non-public content should be deleted. Maybe the deletion and editing can happen in the mornings, while growth stages might happen in the evening? Should that be reversed? Write near the reckless edges of sleep.
     

    global data, text, seconds, start_words, new_words, current_words, fname

    # ask how long they want the turn to last, save as turn_minutes. default 25.
    turn_length = input("How many minutes do you want the turn to last? (press enter for 25 minutes)")
    # All of these lines of code can be hijacked, filled with previously inert content from the comments. 
    if turn_length:
        print ("this turn will last for", turn_length, "minutes.")
        time.sleep(.2)
    else:
        turn_length = 25
        print ("this turn will last for", turn_length, "minutes.")
        time.sleep(.2)
    # prompt for word goal for the turn. If nothing then there is no word goal.
    word_goal = input("how many words do you want to write? (press enter for none)")
    if word_goal:

        print ("You will write", word_goal, "words")
        time.sleep(.2)
    else:
        word_goal = 0
        print("word goal set to", word_goal)
    ## create drift.txt if it doesn't exist
    if path.exists("drift.txt"):
        pass
        print ("a drift file exists.")
    else:
        print ("there is no file in which the drift can grow. A new text will be created.")
        text= open("drift.txt", "w+")

    ## count words in drift.txt.

# This right here is what has been causing problems. The text is set to drift.txt by default.
    fname = input("A gnoll walks up to you, his expression an uncertain balance between menace and a grin. He snarls and sings: 'Enter the name of the file to which words will be added': ")

# 



    count_words(fname)
    ready = input("ready?")
    cls()
    # set seconds, minutes, and new words to zero.
    seconds = 0
    minutes = 0
    new_words = 0
    current_words = start_words
    def update():
        global seconds, current_words, start_words, new_words, hand, fname
        hand = open(fname)

        di = dict()
        lines =0

        seconds+=1
        current_words =0
        for lin in hand:
#            lines += 1
            lin = lin.rstrip()
            # rstrip removes white space at begining and end of a string.
            stcs = lin.split(".")
#            for s in stcs:
#                sentences +=1
            wds = lin.split()
            for w in wds:
    #            print(w)
                current_words+=1
        new_words = current_words - start_words
        print ("this turn has lasted", minutes, "minutes, and", seconds, "seconds. \n You started with", start_words, "and now there are", current_words, "which means you have written", new_words, "new words into the drift.")
        time.sleep(1)
        cls()

    try:
        while int(minutes) < int(turn_length):

            update()
            if seconds >59:
                minutes +=1
                seconds = 0
    except:
        print ("turn ended early")

    # after this, the code will only be triggered after the time for the turn is over.
    print ("the turn is over.")
    score()

    new_record()
##### here is where you need to call the new_record function, and have the new words be entered as the word count for the turn.


#
#                   _|  _|    _|
#     _|_|      _|_|_|      _|_|_|_|
#   _|_|_|_|  _|    _|  _|    _|
#   _|        _|    _|  _|    _|
#     _|_|_|    _|_|_|  _|      _|_|
#
#

def edit():
    global data, text, seconds, start_words, new_words, current_words, fname

    # This is just a copy of the turn function with a few things changed.
    turn_length = input("How many minutes to you want to feed into the drift? (press enter for 25 minutes)")
    if turn_length:
        print ("this turn will last for", turn_length, "minutes.")
        time.sleep(.2)
    else:
        turn_length = 25
        print ("this turn will last for", turn_length, "minutes.")
        time.sleep(.2)
    # prompt for word goal for the turn. If nothing then there is no word goal.
    edit_goal = input("how many words do you want to remove? (press enter for none)")
    if edit_goal:

        print ("You will remove", edit_goal, "words")
        time.sleep(.2)
    else:
        edit_goal = 0
        print("edit goal set to", edit_goal)


#
    fname = input("Continuity looks around the group, to stunned with travel to notice the figure approaching, slowly lifting above the dry horizon.")
#



    count_words(fname)
    ready = input("ready?")
    cls()
    # set seconds, minutes, and new words to zero.
    seconds = 0
    minutes = 0
    new_words = 0
    current_words = start_words
    def update():
        global seconds, current_words, start_words, new_words, hand, fname
        hand = open(fname)

        di = dict()
        lines =0

        seconds+=1
        current_words =0
        for lin in hand:
#            lines += 1
            lin = lin.rstrip()
            # rstrip removes white space at begining and end of a string.
            stcs = lin.split(".")
#            for s in stcs:
#                sentences +=1
            wds = lin.split()
            for w in wds:
    #            print(w)
                current_words+=1
        edited_words = start_words - current_words
        print ("this turn has lasted", minutes, "minutes, and", seconds, "seconds. \n You started with", start_words, "and now there are", current_words, "which means you have thrown", edited_words, "words into the drift.")
        time.sleep(1)
        cls()

    try:
        while int(minutes) < int(turn_length):

            update()
            if seconds >59:
                minutes +=1
                seconds = 0
    except:
        print ("turn ended early")

    # after this, the code will only be triggered after the time for the turn is over.
    print ("the turn is over.")
    score()

    new_record()
#   _______  _______  _______  ______    _______
#  |       ||       ||       ||    _ |  |       |
#  |  _____||       ||   _   ||   | ||  |    ___|
#  | |_____ |       ||  | |  ||   |_||_ |   |___
#  |_____  ||      _||  |_|  ||    __  ||    ___|
#   _____| ||     |_ |       ||   |  | ||   |___
#  |_______||_______||_______||___|  |_||_______|


#
#
#     _|_|_|    _|_|_|    _|_|    _|  _|_|    _|_|
#   _|_|      _|        _|    _|  _|_|      _|_|_|_|
#       _|_|  _|        _|    _|  _|        _|
#   _|_|_|      _|_|_|    _|_|    _|          _|_|_|
#
#

def score():
    global data, character, new_words
    manual_words = int(input("How many words did you write in other files?"))
    try:
        print ("words counted automatically were", new_words)
        new_words = new_words + manual_words
        print ("with the additional words entered, you have written", new_words)
    except:
        print ("couldn't add words manually")
        error_message()
    print ("These print statements. \n /n rather than get rid of them, use them as points of (re)-entry. \n ")

    # Trust that there are points invisible for deleted words, for experiences forgotten that are still incarnated in patterns of deep
    time.sleep(2)

    # A simple exercise. A random number, and a selection from a list.
    #print ("This is where a performativity aspect could come in, streaming to an audience, typing to them, talking at the same time, impressive people with the speed of your mind and fingers.")
    time.sleep(2)
    print ("Pseudocode. This is how progress is marked in the game. After every turn, a score can be calculated, and experience added to the character sheet.")
    try:
        print ("If new words are here, you'll see this line and new words:", new_words)
    except:
        time.sleep(2)
        print ("there are no words.")
        error_message()
    try:
        print ("I'm gonna try to read experience points for the character from the mask file. Your character is", character["name"], "and your xp is", character["xp"])
        print ("So far, so good. Now imma try to add new words to the xp.")
        character["xp"]+= new_words
        time.sleep(1)
        print ("the new xp is", character["xp"])
    except:
        print ("You lack experience.")
        error_message()
#
#       _|_|_|_|_|
#     _|          _|
#   _|    _|_|_|  _|
#   _|  _|    _|  _|
#   _|    _|_|_|_|
#     _|
#       _|_|_|_|_|_|

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
#
#                                             _|
#     _|_|_|    _|_|    _|    _|  _|_|_|    _|_|_|_|
#   _|        _|    _|  _|    _|  _|    _|    _|
#   _|        _|    _|  _|    _|  _|    _|    _|
#     _|_|_|    _|_|      _|_|_|  _|    _|      _|_|
#
#
#                                                 _|
#   _|      _|      _|    _|_|    _|  _|_|    _|_|_|    _|_|_|
#   _|      _|      _|  _|    _|  _|_|      _|    _|  _|_|
#     _|  _|  _|  _|    _|    _|  _|        _|    _|      _|_|
#       _|      _|        _|_|    _|          _|_|_|  _|_|_|
#
#

# The @ symbol is important to me from rogue-like role playing games, which I play frequently. The signification, for me, for now, is this: the writing game is a way to focus on a single task, a single file, for a "pomodoro" of 25 minutes.




def count_words(text):
    global start_words, hand, fname

    if len(fname) <1 : fname = text
    hand = open(fname)

# Todo:rewrite the above so it is more like:
## with open(fname) as hand: [then the for lin in hand]

    di = dict()
    lines =0
    words =0
    sentences = 0
    for lin in hand:
        lines += 1
        lin = lin.rstrip()
        # rstrip removes white space at begining and end of a string.
        stcs = lin.split(".")

# gnoll: okay, so the preceding line is super cool and key. It makes a list, I guess, of sentences, by splitting periods.
        for s in stcs:
            sentences +=1
# gnoll: below, the program divides the sentences into words.
        wds = lin.split()
        for w in wds:
#            print(w)
            words+=1
    print("The object is robust verbiage. Ahem. There are presently", lines, "lines in the file you have chosen,", sentences, "sentences, and", words, "words.")
    start_words = words

    # tell them needed wpm. Ask if they would like to set a new wpm goal

    # THIS IS IMPORTANT ^^^^ and should perhaps be moved to a TODO list?


    # on end turn, count the number of new words for drift.txt
    ## prompt for words added in target document
    try:
        #
        other_words = 0
        other_words_imput= int(imput("do you have any words you typed into other files that you would like to add to the count? If so, enter here. Othewise, press enter."))
        other_words= other_words + other_words_imput
        print (other_words, "words will be added to ")
    except:
        pass

def other():
    global data, new_words
    print ("well, you have been redirected here. There is a study, a room in a house you are unfamiliar with, perhaps a cousins. They have a computer game, but the packaging is almost like an LP, amazing art.")
    time.sleep(1)

    print ("For fun and practice, let's try to set up...well a couple things. One, a manual way of entering in new words.")
    new_words = int(input("how many words did you write?"))
    if type(new_words) == int or float:
        print ("that was a number")
    else:
        print ("that's not a number")
        time.sleep(1)
        other()

    # you know, close enough.

def mask():

    global masks, character
    with open('../masks.json', "r") as readfile:
        masks = json.load(readfile)
    print ("existing characters are:")
    n=0
    for i in masks:
		#print ("A mask for", i)
		#print ("your", i, "is", mask[i])
        n+=1
        print (n,": ", i)
    ans = str(input("who do you want to play?"))
    character = masks[ans]


    ##check to see if exists?
    for x in character:
        print ("your", x, "is", character[x], ".")

start()

# NOTES

## A card pops up into your mental space, with an eye-catching logo you vaguely remember designing.


##  writing to a generalized you, the phrase drifting out into second person plurality.


    # Green, with gold overlay. The art is traditional, knotwork combined with ascii characters.

#
#     _|                      _|
#   _|_|_|_|    _|_|      _|_|_|    _|_|
#     _|      _|    _|  _|    _|  _|    _|
#     _|      _|    _|  _|    _|  _|    _|
#       _|_|    _|_|      _|_|_|    _|_|
#
#

Todo = [".", "have a turncount object in the json file", "have a total_word_count object in the json data."]

drift_text= " "
drift_sentences = ["I want to start building up a syntactical database, possible random things a character could say.","On the website, there could be an image, with another .png file on top of it, that would contain a comic style text box."]
# Humility of comment. Generosity of conent. The gnoll, woodenlegs, taps you on the shoulder with his staff, like he is knighting you. "A general principle," he says. "The records can be altered to reflect the spirit of the narrative. Don't let quantificaiton get in the way of telling an accurate story."

side_missions = ["have a more fun turn, maybe not even part of the writing game itself. This folder, by the way...it can have the feel of a massive multiplayer, using the parts of your own mind as players. Distributed temporally."]
