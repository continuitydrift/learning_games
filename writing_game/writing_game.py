 # This is a program that I will add functionality to over time, in order to provide tools for writers (well, ok, me) to record their activity and motivate them to be more productive.

# The game will keep track of the amount of words a player writes, in this or a seperate file, either by couning the words automatically, or accepting imput from the player.

#  It is easy to see when I have been working for 25 minutes. The six different videos could be edited into a larger video, where the result (a text file, or image) could be shown in the background, progressing at six times the normal speed, while the six turns could appear in seperate windows.

# It's Saturday, September 26th. I have several coding lessons to teach today, and it seemed like a good idea to do some of my own "coding" after a run and shower, before lunch and the work of the afternoon.

# TODO:

## read through the entire program once. An end goal would be to have sufficient comments that someone who doesn't know or has forgotten how to code the game would be able to figure it out.

##  make the date part of new records
## (make record a class?)

# Optional Rules

## within the writing game, there are six different possible texts, of ranked significance. for example:

### 1. songs 2. continuity drift 3. journal 4. this file 5. new language 6. turtle
## The progression would always go to the numerically higher value. From this file I will proceed to new language, then to turtle.

# The first thing I need to do is import libraries I will need

import os, json, time, random
import os.path
from os import path
from datetime import date

# let's see if data.json exists

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
    # this also loads the data
    get_records()

#    new_record()

    menu()

#       this function will bring up the option to burn the archive (wipe records), or start a turn.


#    get_date()
#    the date, in this case, is December 117tht The typoos you are seeing aarerccts of an fowingbuffer. Too many windows open. Hitting backspace a few times seems to have fixed the prooblem.
##    december 27th, then, with a cup of cold coffee and an early morning, with no lesssons plannedd. The artifacts are back. They need to be worked, somehow, into the mythos, sesrvantss  fo duchess of aphasia.
#     so in oi suppose,     toto  seqqueecoun, I will lckiimm ovb add d cryptic then close them,m until either this  program  is wormking again or I can cllose it
#    get_word_count()


    #except:
    #    print ("You fail! The cost is to write an error message better than this one.")

def does_data_exist():
    global data
    # I'm making this it's own function

    if os.path.isfile("data.JSON"):
#        print ("contratulations, data file exists!")
        pass
        # File exists, so checking if data size is > 0

        if os.path.getsize("data.JSON") > 0:
#            print ("data file is not empty.")
            pass
        # if so, opening and loading data
        # this logic gate has yet to be built.

        load_data()

    else:
        print ("data file does not exist.")

        data = {}
        save_data()
#        load_data()

def get_word_count():
    global today, word_count

    word_count=input("How many words did you write?")
    print ("you wrote", word_count, "words this turn.")

def get_records():
    global data, records

    if "records" in data:
#        print ("records in data file exists!")

        # data exists, so checking if data size is > 0

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
    global data, today
#    for i in data:
#        print (data[i], "is", i)

    # this should be able to first create a turn.

    # print ("You have set a new record, in that you have now played this game more total turns than you ever have before.")


    # theoretically, if I load data at the beginning of every function and save at the end, do I need data to be a global variable?
    def get_turns():
        global data, turns
        if "turns" in data:
            #print ("There are previous turns in the datafile.")
            turns= data["turns"]
            print ("you have played", turns, "turns")
            turns = turns + 1
            print ("This is turn", turns)
            data["turns"] = turns
            save_data()
        else:
            data["turns"]= 0
            save_data()
            get_turns()
    get_turns()

#    str(input("entering experimental zone!! press any key."))
    def create_record():
        global data, turns, today
        data["records"][turns]={}
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

        data["records"][turns]["date"]=str(this_turn_date)
        print ("within data there is now,", data["records"][turns]["date"])
        print ("Now for words.")
        this_turn_words=turn_record.words
        print ("words for this turn are", this_turn_words)
        data["records"][turns]["words"]=this_turn_words


#                data["records"][turns]["words"]=0
#                words_this_turn = data["records"][turns]["words"]
#                get_word_count()
#                words_this_turn = words_this_turn + word_count

#                print ("words for this turn is at", words_this_turn, "\n")
#                data["records"][turns]["words"] = words_this_turn
        save_data()

            #create_turn_record()
            #save_data()

    create_record()
    save_data()
#    except:
#        error_message()



def error_message():
    global data

    if "error_messages" in data:
        print ("error messages found in the data file. As follows...")
        for i in data["error_messages"]:
            print (i)
    else:
        data["error_messages"] =["You seem to have made a critical error."]
        print (data["error_messages"])
        save_data()

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
    with open("data.JSON", "r") as rf:
        data = json.load(rf)

        for i in data:
            pass
#            print (i, "is", data[i])

def save_data():
    global data
    with open("data.JSON", "w") as wf:
        json.dump(data, wf)

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
    global data
    ans = str(input("what do you want to do? [b]urn the archive, start a [n]ew turn, or [o]ther?"))
    if ans == "b":
        print ("the archive is burning.")
        try:
            data = {}

            save_data()
        except:
            print ("the archive's walls prove more fireproof than we thought.")
    if ans == "n":
        print ("a new turn is starting.")
        turn()
    if ans == "o":
        print ("algorithm is othering")

#
#     _|
#   _|_|_|_|  _|    _|  _|  _|_|  _|_|_|
#     _|      _|    _|  _|_|      _|    _|
#     _|      _|    _|  _|        _|    _|
#       _|_|    _|_|_|  _|        _|    _|
#
#

def turn():
    global data, text, seconds, start_words, new_words, current_words

    # ask how long they want the turn to last, save as turn_minutes. default 25.
    turn_length = input("how many minutes do you want the turn to last? (press enter for 25 minutes)")
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
#        print ("a drift file exists.")
    else:
        print ("there is no file in which the drift can grow. A new text will be created.")
        text= open("drift.txt", "w+")

    ## count words in drift.txt.
    text = "drift.txt"
    count_words(text)
    ready = input("ready?")
    cls()
    # set seconds, minutes, and new words to zero.
    seconds = 0
    minutes = 0
    new_words = 0
    current_words = start_words
    def update():
        global seconds, current_words, start_words, new_words, hand
        fname = text
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
    new_record()
##### here is where you need to call the new_record function, and have the new words be entered as the word count for the turn.

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
    global start_words, hand
    fname = input("A gnoll walks up to you, his expression an uncertain balance between menace and a grin. He snarls and sings: 'Enter the name of the file to which words will be added': ")
    if len(fname) <1 : fname = text
    hand = open(fname)

    di = dict()
    lines =0
    words =0
    sentences = 0
    for lin in hand:
        lines += 1
        lin = lin.rstrip()
        # rstrip removes white space at begining and end of a string.
        stcs = lin.split(".")
        for s in stcs:
            sentences +=1
        wds = lin.split()
        for w in wds:
#            print(w)
            words+=1
    print("The object of this game is to add as many words into the chosen file as possible. Concerns of quality are, at this stage, secondary. Focus instead on the robust generation of verbiage. Ahem. There are presently", lines, "lines in the file you have chosen,", sentences, "sentences, and", words, "words.")
    start_words = words

    # tell them needed wpm. Ask if they would like to set a new wpm goal

    # THIS IS IMPORTANT ^^^^ and should perhaps be moved to a TODO list?

    # start turn. display countdown?
    # on end turn, count the number of new words for drift.txt
    ## prompt for words added in target document
start()

# NOTES

## 10/8/2020
## Another stream session, listening to 25 minutes of music that I recorded previously. Now, I'll see how much progress I can make on this writing game, which is a way to keep track of how many words I add to a file in a turn.

## 8/5/2020
##  I need to think about steps of basic functionality to acheive. Every time the game is run a record should be created for the turn. The record should have the day, month, and year, as well as the number of words written.

## 8/6/2020

### save record after made as a class with default data




# epiogue


## There is time, though, for edits and revisions. I won't update the repository until everything overtly extraneous has been removed.

## The impulse to put more effort into this writing game came just as my involvement on a gamification site, where you kept track of todos and daily habits, was coming to an end.


##  writing to a generalized you, the phrase drifting out into second person plurality.

## Take encouragement in the ephemerality of the unuploaded file.

#
#     _|                      _|
#   _|_|_|_|    _|_|      _|_|_|    _|_|
#     _|      _|    _|  _|    _|  _|    _|
#     _|      _|    _|  _|    _|  _|    _|
#       _|_|    _|_|      _|_|_|    _|_|
#
#

Todo = ["Make it so that there is a word_count for each turn.", "have a turncount object in the json file", "have a total_word_count object in the json data."]
