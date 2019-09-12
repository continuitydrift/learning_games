#  ~~~~~~~~~~~~~~~~~~~~___~~~~~~~~~~~___~~~~~~~~~~~___~~~~~~~~~~~~~~~~~
#  ~~~~~~___~~~~~~~~~~/__/\~~~~~~~~~/~~/\~~~~~~~~~/~~/\~~~~~~~~~~___~~~
#  ~~~~~/~~/\~~~~~~~~~\~~\:\~~~~~~~/~~/:/_~~~~~~~/~~/:/_~~~~~~~~/~~/\~~
#  ~~~~/~~/::\~~~~~~~~~\~~\:\~~~~~/~~/:/~/\~~~~~/~~/:/~/\~~~~~~/~~/:/~~
#  ~~~/~~/:/\:\~~~~___~~\~~\:\~~~/~~/:/~/:/_~~~/~~/:/~/::\~~~~/~~/:/~~~
#  ~~/~~/:/~/::\~~/__/\~~\__\:\~/__/:/~/:/~/\~/__/:/~/:/\:\~~/~~/::\~~~
#  ~/__/:/~/:/\:\~\~~\:\~/~~/:/~\~~\:\/:/~/:/~\~~\:\/:/~/:/~/__/:/\:\~~
#  ~\~~\:\/:/__\/~~\~~\:\~~/:/~~~\~~\::/~/:/~~~\~~\::/~/:/~~\__\/~~\:\~
#  ~~\~~\::/~~~~~~~~\~~\:\/:/~~~~~\~~\:\/:/~~~~~\__\/~/:/~~~~~~~~\~~\:\
#  ~~~\__\/~~~~~~~~~~\~~\::/~~~~~~~\~~\::/~~~~~~~~/__/:/~~~~~~~~~~\__\/
#  ~~~~~~~~~~~~~~~~~~~\__\/~~~~~~~~~\__\/~~~~~~~~~\__\/~~~~~~~~~~~~~~~~
#  ~~~~~~~~~~~~~~~~~~___~~~~~~~~~~~___~~~~~~~~~~~___~~~~~~~~~~~~~~~~~~~
#  ~~~~___~~~~~~~~~~/~~/\~~~~~~~~~/__/\~~~~~~~~~/~~/\~~~~~~~~~~~~~~~~~~
#  ~~~/~~/\~~~~~~~~/~~/::\~~~~~~~~\~~\:\~~~~~~~/~~/:/_~~~~~~~~~~~~~~~~~
#  ~~/~~/:/~~~~~~~/~~/:/\:\~~~~~~~~\~~\:\~~~~~/~~/:/~/\~~~~~~~~~~~~~~~~
#  ~/__/::\~~~~~~/~~/:/~~\:\~~~_____\__\:\~~~/~~/:/~/::\~~~~~~~~~~~~~~~
#  ~\__\/\:\__~~/__/:/~\__\:\~/__/::::::::\~/__/:/~/:/\:\~~~~~~~~~~~~~~
#  ~~~~\~~\:\/\~\~~\:\~/~~/:/~\~~\:\~~\~~\/~\~~\:\/:/~/:/~~~~~~~~~~~~~~
#  ~~~~~\__\::/~~\~~\:\~~/:/~~~\~~\:\~~~~~~~~\~~\::/~/:/~~~~~~~~~~~~~~~
#  ~~~~~/__/:/~~~~\~~\:\/:/~~~~~\~~\:\~~~~~~~~\__\/~/:/~~~~~~~~~~~~~~~~
#  ~~~~~\__\/~~~~~~\~~\::/~~~~~~~\~~\:\~~~~~~~~~/__/:/~~~~~~~~~~~~~~~~~
#  ~~~~~~~~~~~~~~~~~\__\/~~~~~~~~~\__\/~~~~~~~~~\__\/~~~~~~~~~~~~~~~~~~


#SPANISH VERSION


####  TODO
#### 1. add high scores
#### 2. Make it possible to die
####  3. enter turns
####  4. only ask to add questions at end of round
####   5. Ask for middle if there isn't one
####  6. Ask for appropriate end if there isn't one


##      external files required are trivia.json and masks.json
import time, random, json, pprint, os



#        load names
#        get name
##       if questions:
##          more questions?
##       else:
##          add questions
####     if story:
####        here are stories; new story?
####     else:
####        new story
#####    game()
######   ending()

def main():
#    load_stories()
    start()

def start():
    global status, masks, character, turncount, quotes, the_score, total_score, stories, level, average, difficulty, genre, narrative, asked_questions


        #initializing values

        #the values of the game are surprise, growth, collaboration, experimentation, learning, and thoughtfulness.
    turncount=0
    the_score=0
    total_score=0
    average=0
    status="living"
    asked_questions=[]
    get_difficulty()
    get_story()
    get_genre()
    load_trivia()

    start_menu()

# The simplest version of this game wouldn't have a list of players--the downloads of the file, with the saves, would be like a new player.
    #load_location()
    turn()
    exit()


def start_menu():
    ans=str(input("do you want to [l]oad a character or [c]reate a new one?"))
    if ans=="l":
        load_mask()
    elif ans=="c":
        new_mask()
    else:
        print("what was that?")
        start_menu()

def menu():
    ans=str(input("[p]lay another turn, or [s]ave and quit?"))
    if ans=="p":
        turn()
    elif ans=="s":
        add_question()
        save_mask()
        save_locations()
        exit()
    else:
        print("what was that?")
        start_menu()

#  ~~~~~~___~~~~~~~~~~___~~~~~~~~~~___~~~~~~~~~~~~~~~~~~~~~___~~~~~
#  ~~~~~/\~~\~~~~~~~~/\~~\~~~~~~~~/\~~\~~~~~~~~~___~~~~~~~/\~~\~~~~
#  ~~~~/::\~~\~~~~~~/::\~~\~~~~~~/::\~~\~~~~~~~/\~~\~~~~~/::\~~\~~~
#  ~~~/:/\:\~~\~~~~/:/\:\~~\~~~~/:/\~\~~\~~~~~~\:\~~\~~~/:/\:\~~\~~
#  ~~/::\~\:\__\~~/::\~\:\~~\~~_\:\~\~\~~\~~~~~/::\__\~/:/~~\:\~~\~
#  ~/:/\:\~\:|__|/:/\:\~\:\__\/\~\:\~\~\__\~__/:/\/__//:/__/~\:\__\
#  ~\:\~\:\/:/~~/\/__\:\/:/~~/\:\~\:\~\/__//\/:/~~/~~~\:\~~\~~\/__/
#  ~~\:\~\::/~~/~~~~~~\::/~~/~~\:\~\:\__\~~\::/__/~~~~~\:\~~\~~~~~~
#  ~~~\:\/:/~~/~~~~~~~/:/~~/~~~~\:\/:/~~/~~~\:\__\~~~~~~\:\~~\~~~~~
#  ~~~~\::/__/~~~~~~~/:/~~/~~~~~~\::/~~/~~~~~\/__/~~~~~~~\:\__\~~~~
#  ~~~~~~~~~~~~~~~~~~\/__/~~~~~~~~\/__/~~~~~~~~~~~~~~~~~~~\/__/~~~~
#  ~~~~~~___~~~~~~~~~~___~~~~~~~~~~___~~~~~~~~~~___~~~~~~~___~~~~~~
#  ~~~~~/\~~\~~~~~~~~/\__\~~~~~~~~/\__\~~~~~~~~/\~~\~~~~~/\~~\~~~~~
#  ~~~~/::\~~\~~~~~~/:/~~/~~~~~~~/::|~~|~~~~~~/::\~~\~~~~\:\~~\~~~~
#  ~~~/:/\:\~~\~~~~/:/~~/~~~~~~~/:|:|~~|~~~~~/:/\:\~~\~~~~\:\~~\~~~
#  ~~/::\~\:\~~\~~/:/~~/~~___~~/:/|:|~~|__~~/:/~~\:\~~\~~~/::\~~\~~
#  ~/:/\:\~\:\__\/:/__/~~/\__\/:/~|:|~/\__\/:/__/~\:\__\~/:/\:\__\~
#  ~\/__\:\~\/__/\:\~~\~/:/~~/\/__|:|/:/~~/\:\~~\~~\/__//:/~~\/__/~
#  ~~~~~~\:\__\~~~\:\~~/:/~~/~~~~~|:/:/~~/~~\:\~~\~~~~~/:/~~/~~~~~~
#  ~~~~~~~\/__/~~~~\:\/:/~~/~~~~~~|::/~~/~~~~\:\~~\~~~~\/__/~~~~~~~
#  ~~~~~~~~~~~~~~~~~\::/~~/~~~~~~~/:/~~/~~~~~~\:\__\~~~~~~~~~~~~~~~
#  ~~~~~~~~~~~~~~~~~~\/__/~~~~~~~~\/__/~~~~~~~~\/__/~~~~~~~~~~~~~~~
#  ~~~~~~~~~~~~~~~~~___~~~~~~~~~~___~~~~~~~~~~___~~~~~~~~~~~~~~~~~~
#  ~~~~~~___~~~~~~~/\~~\~~~~~~~~/\__\~~~~~~~~/\~~\~~~~~~~~~~~~~~~~~
#  ~~~~~/\~~\~~~~~/::\~~\~~~~~~/::|~~|~~~~~~/::\~~\~~~~~~~~~~~~~~~~
#  ~~~~~\:\~~\~~~/:/\:\~~\~~~~/:|:|~~|~~~~~/:/\~\~~\~~~~~~~~~~~~~~~
#  ~~~~~/::\__\~/:/~~\:\~~\~~/:/|:|~~|__~~_\:\~\~\~~\~~~~~~~~~~~~~~
#  ~~__/:/\/__//:/__/~\:\__\/:/~|:|~/\__\/\~\:\~\~\__\~~~~~~~~~~~~~
#  ~/\/:/~~/~~~\:\~~\~/:/~~/\/__|:|/:/~~/\:\~\:\~\/__/~~~~~~~~~~~~~
#  ~\::/__/~~~~~\:\~~/:/~~/~~~~~|:/:/~~/~~\:\~\:\__\~~~~~~~~~~~~~~~
#  ~~\:\__\~~~~~~\:\/:/~~/~~~~~~|::/~~/~~~~\:\/:/~~/~~~~~~~~~~~~~~~
#  ~~~\/__/~~~~~~~\::/~~/~~~~~~~/:/~~/~~~~~~\::/~~/~~~~~~~~~~~~~~~~
#  ~~~~~~~~~~~~~~~~\/__/~~~~~~~~\/__/~~~~~~~~\/__/~~~~~~~~~~~~~~~~~
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def turn():
    global masks, character, turncount, score, status, level, stories, genre, average, difficulty
    #print(" the turn turns")
    turncount+=1
    print (" ")
    print ("turn", turncount)
    #for i in character:
    #    print ("Your character's",i,"is",character[i])
    time.sleep(1)
    if turncount==1:
        try:
            print (stories["genres"][genre]["beginning"])
        except:
            print ("the beginning to the story is lost.")

    if turncount==3:
        try:
            print (stories["genres"][genre]["middle"])
        except:
            print ("the middle of the story is lost")
            add_middle()

    if turncount==6:
        result()
        add_question()
    turn_menu()

    #next step:
    #trivia()
    while status=="living":
        turn()

def result():
    global the_score, character, turncount, difficulty, total_score, question_score, status, average

    print ("you are playing at a difficulty of", difficulty, "so you needed an average score of", difficulty )
    #target=difficulty*(turncount-1)
    target=difficulty
    if average < target:
        lose()
    else:
        win()

def lose():
    global status, stories, genre
    print("you lose!!!")
    if "bad_end" in stories["genres"][genre]:
        print (stories["genres"][genre]["bad_end"])
    else:
        add_bad_end()
    status="dead"

def win():
    global status
    if "good_end" in stories["genres"][genre]:
        print (stories["genres"][genre]["good_end"])
    else:
        add_good_end()

    status="living"

def turn_menu():
    ans=str(input("Do you want to [a]nswer a trivia question, or [s]ave and quit?"))
    if ans=="a":
        trivia()

    elif ans=="s":
        save_mask()
        #save_locations()
        #if you update this, also update it in the main menu

def get_difficulty():
    global difficulty
    difficulty =int(input("At what difficulty would you like to play (1-6)?"))
    print ("difficulty is set at", difficulty)

def get_genre():
    global genre, stories
#this function should 1) create a list of possible genres (eventually, this list would probably be populated from a json file like other things, with permanence)
    if "genres" in stories:
        print ("genres detected. They are:")
        for i in stories["genres"]:
            print (i)
    #    print (stories["genres"].keys)
    else:
        stories["genres"]={}
        stories["genres"]["fantasy"]={}
        stories["genres"]["fantasy"]["beginning"]="The heroes made their way over the mountain pass, the wild landscape of good and evil spread out below them."



    #genre_list=["fantasy", "science fiction", "action"]
    #count=0
    #for i in stories["genres"]:

    #    print (stories["genres"][i])
    try:
        genre =input("What genre?")
        print ("you have selected", genre)
        if genre in stories["genres"]:
            print (stories["genres"][genre]["beginning"])
        else:
            add_genre()
    except:
        print ("I fail to understand.")
        get_genre()

    with open("stories.json","w") as outfile:
        json.dump(stories, outfile)

def add_genre():
    global genre, stories
    stories["genres"][genre]={}
    try:
        new_beginning = str(input("how does the story start?"))
        stories["genres"][genre]["beginning"]=new_beginning
        print (stories["genres"][genre]["beginning"])
    except:
        print ("failed to create new beginning")
        add_new_beg()

def add_question():
    global questions, character
    ans = str(input("do you want to add a question?"))
    if ans =="y":
        new_question=str(input("what is the question?"))
        new_answer=str(input("what is the answer?"))
        new_subject=str(input("what subject?"))
        n = len(questions)+1
        print ("the number of questions is", n)
        questions.update({n:{"q":new_question,"a":new_answer,"subject":new_subject}})
        character["xp"]+=6
        ans =str(input("enter another question y/n?"))
        if ans =="y":
            add_question()
        else:
            save_questions()
            pass

def add_new_beg():
    if "new_beg" in stories["genres"][genre]:
        print (stories["genres"][genre]["new_beg"])
    else:
        add_new_beg()

def add_middle():
    global stories, genre
    new_middle = str(input("what is the middle of the story?"))
    try:
        stories["genres"][genre]["middle"]=new_middle
        print (stories["genres"][genre]["middle"])
    except:
        print ("failed to create new middle")

def add_good_end():
    global stories, genre
    new_good_end = str(input("what is a good ending for the story?"))
    try:
        stories["genres"][genre]["middle"]=new_good_end
        print (stories["genres"][genre]["good_end"])
    except:
        print ("failed to create new good ending")

def add_bad_end():
    global stories, genre
    new_bad_end = str(input("what is a bad ending for the story?"))
    try:
        stories["genres"][genre]["bad_end"]=new_bad_end
        print (stories["genres"][genre]["bad_end"])
    except:
        print ("failed to create new bad ending")

def score():
    global character, turncount, total_score, question_score, average
    ans=int(input("enter your score (1-6)__"))
    total_score+=ans
    average= total_score/turncount
    question_score=ans
    print ("you scored", question_score)
    print ("your average score is now", average)
    character["xp"]+=ans
    print ("you now have", character["xp"], "xp")
    time.sleep(1)

def ask_trivia(subject):
    global questions, asked_questions
    count=0
    subject_list=[]
    question_list={}
    new_questions={}
    for i in questions:
        questions.update({i:questions[i]})
        count+=1
        #print (questions[i]["subject"])
        if questions[i]["subject"] not in subject_list:
            subject_list.append(questions[i]["subject"])

    print ("there are ", count, "questions.")
    print (subject_list)

    chosen_subject=str(input("what subject? or [a]ll)"))
    if (chosen_subject=="all") or (chosen_subject=="a"):
        for i in questions:
            if questions[i] not in asked_questions:
                question_list.update({i:questions[i]})
            else:
                pass
    else:
        for i in questions:
            if questions[i] not in asked_questions:
                if questions[i]["subject"]==chosen_subject:
                    question_list.update({i:questions[i]})
                else:
                    pass
            else:
                pass
    #I need a way to redirect when something unrecognized is entered.
    n = len(question_list)
            #print (questions[i]["q"])
            #input()
            #print (questions[i]["a"])
            #score()
    print ("there are", n, "questions in", chosen_subject)
    if n >1:
        roll=(random.randint(1,n))
    elif n==0:
        print ("there are no more questions in that subject.")
        #ask_trivia("all")
        trivia()
    else: roll=1
    print ("roll is", roll)
    time.sleep(1)
    new_list={}
    x=1
    for i in question_list:
        new_list[x]=question_list[i]
        x+=1
        #question_list["i"]=question_list[x]
    #print (new_list)
    print (new_list[roll]["q"])
    #print (question_list[roll]["q"])
    input("ready for the answer?")
    print (new_list[roll]["a"])
	#	global questions_list
    asked_questions.append(new_list[roll])
#    print (new_list[roll]["q"], "has been added to the list of asked questions.")


def reroll():
    global roll, character
    roll=random.randint(1,6)
    #for i in character:
    #    if character[i]=roll:
    #        reroll()


def new_mask():
    global mask, character, roll
    #import random
    taken_numbers=[]
    character = {}
    #character["a"]=random.randint(1,6)
    #character["s"]=random.randint(1,6)
    #character["h"]=random.randint(1,6)
    #character["d"]=random.randint(1,6)
    #character["r"]=random.randint(1,6)
    #character["m"]=random.randint(1,6)
    character["name"]="unknown"
    #character["location"]="inn"
#    for i in character:
#        while character[i] in taken_numbers:
#            print (character[i], "is in the list of taken numbers, which is ", taken_numbers)
            #time.sleep(1)
#            character[i]=random.randint(1,6)
#            print ("now the roll is", character[i])
#        else:
#            taken_numbers.append(character[i])
    for stat in character:
            print(stat)
	#character["s"]=random.randint(1,6)
#acter["m"]
	#new_roll(m)
    character["xp"]=0

    for i in character:
        print ("Your", i, "is", character[i])

	#turn()
	#print (stats["a"])
	#If you have started the game wth an even distribution then you can rest knowing that you are one of the universla archetypes, and that the game has been designed to have a strategy maximized for you, a gameplay glowing in the eigen-dark.
	#print

def trivia():
    #load file
    #get question
    #get answer
    #score
    #load_trivia()
    ask_trivia("all")
    time.sleep(.5)
    score()
    #add_question()
#  ~~~~~~___~~~___~~~~~~~~~~___~~~~~~~~~~___~~~~~~~~~~~~~~~~~~~~~~
#  ~~~~~/\__\~/\~~\~~~~~~~~/\~~\~~~~~~~~/\~~\~~~~~~~~~~~~~~~~~~~~~
#  ~~~~/:/~~//::\~~\~~~~~~/::\~~\~~~~~~/::\~~\~~~~~~~~~~~~~~~~~~~~
#  ~~~/:/~~//:/\:\~~\~~~~/:/\:\~~\~~~~/:/\:\~~\~~~~~~~~~~~~~~~~~~~
#  ~~/:/~~//:/~~\:\~~\~~/::\~\:\~~\~~/:/~~\:\__\~~~~~~~~~~~~~~~~~~
#  ~/:/__//:/__/~\:\__\/:/\:\~\:\__\/:/__/~\:|__|~~~~~~~~~~~~~~~~~
#  ~\:\~~\\:\~~\~/:/~~/\/__\:\/:/~~/\:\~~\~/:/~~/~~~~~~~~~~~~~~~~~
#  ~~\:\~~\\:\~~/:/~~/~~~~~~\::/~~/~~\:\~~/:/~~/~~~~~~~~~~~~~~~~~~
#  ~~~\:\~~\\:\/:/~~/~~~~~~~/:/~~/~~~~\:\/:/~~/~~~~~~~~~~~~~~~~~~~
#  ~~~~\:\__\\::/~~/~~~~~~~/:/~~/~~~~~~\::/__/~~~~~~~~~~~~~~~~~~~~
#  ~~~~~\/__/~\/__/~~~~~~~~\/__/~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  ~~~~~~___~~~~~~~~~~___~~~~~~~~~~___~~~~~~~~~~___~~~~~~~___~~~~~
#  ~~~~~/\~~\~~~~~~~~/\__\~~~~~~~~/\__\~~~~~~~~/\~~\~~~~~/\~~\~~~~
#  ~~~~/::\~~\~~~~~~/:/~~/~~~~~~~/::|~~|~~~~~~/::\~~\~~~~\:\~~\~~~
#  ~~~/:/\:\~~\~~~~/:/~~/~~~~~~~/:|:|~~|~~~~~/:/\:\~~\~~~~\:\~~\~~
#  ~~/::\~\:\~~\~~/:/~~/~~___~~/:/|:|~~|__~~/:/~~\:\~~\~~~/::\~~\~
#  ~/:/\:\~\:\__\/:/__/~~/\__\/:/~|:|~/\__\/:/__/~\:\__\~/:/\:\__\
#  ~\/__\:\~\/__/\:\~~\~/:/~~/\/__|:|/:/~~/\:\~~\~~\/__//:/~~\/__/
#  ~~~~~~\:\__\~~~\:\~~/:/~~/~~~~~|:/:/~~/~~\:\~~\~~~~~/:/~~/~~~~~
#  ~~~~~~~\/__/~~~~\:\/:/~~/~~~~~~|::/~~/~~~~\:\~~\~~~~\/__/~~~~~~
#  ~~~~~~~~~~~~~~~~~\::/~~/~~~~~~~/:/~~/~~~~~~\:\__\~~~~~~~~~~~~~~
#  ~~~~~~~~~~~~~~~~~~\/__/~~~~~~~~\/__/~~~~~~~~\/__/~~~~~~~~~~~~~~
#  ~~~~~~~~~~~~~~~~~___~~~~~~~~~~___~~~~~~~~~~___~~~~~~~~~~~~~~~~~
#  ~~~~~~___~~~~~~~/\~~\~~~~~~~~/\__\~~~~~~~~/\~~\~~~~~~~~~~~~~~~~
#  ~~~~~/\~~\~~~~~/::\~~\~~~~~~/::|~~|~~~~~~/::\~~\~~~~~~~~~~~~~~~
#  ~~~~~\:\~~\~~~/:/\:\~~\~~~~/:|:|~~|~~~~~/:/\~\~~\~~~~~~~~~~~~~~
#  ~~~~~/::\__\~/:/~~\:\~~\~~/:/|:|~~|__~~_\:\~\~\~~\~~~~~~~~~~~~~
#  ~~__/:/\/__//:/__/~\:\__\/:/~|:|~/\__\/\~\:\~\~\__\~~~~~~~~~~~~
#  ~/\/:/~~/~~~\:\~~\~/:/~~/\/__|:|/:/~~/\:\~\:\~\/__/~~~~~~~~~~~~
#  ~\::/__/~~~~~\:\~~/:/~~/~~~~~|:/:/~~/~~\:\~\:\__\~~~~~~~~~~~~~~
#  ~~\:\__\~~~~~~\:\/:/~~/~~~~~~|::/~~/~~~~\:\/:/~~/~~~~~~~~~~~~~~
#  ~~~\/__/~~~~~~~\::/~~/~~~~~~~/:/~~/~~~~~~\::/~~/~~~~~~~~~~~~~~~
#  ~~~~~~~~~~~~~~~~\/__/~~~~~~~~\/__/~~~~~~~~\/__/~~~~~~~~~~~~~~~~


def load_mask():
    global masks, character
    with open('masks.json', "r") as readfile:
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

def load_trivia():
    global questions
    with open("trivia.json", "r") as readfile:
        questions= json.load(readfile)
    print ("questions loaded!")
    time.sleep(.6)
    count=0
    for i in questions:
        count+=1
    print ("there are", count, "questions.")

def load_stories():
    global stories
    if os.path.isfile("stories.json"):
        with open('stories.json', "r") as readfile:
            stories = json.load(readfile)
        print ("The stories file exists")

        #    stories.append({"dragon":{"setup":"once there was a dragon.","good_end":"you steal it's treasure","bad_end":"it kills you."}})
    else:
        print ("no stories file detected")
        try:
            #stories = open("stories.json", "w+")
            stories={}
        #    stories={"dragon":"once there was a dragon."}
        #    stories.append(stories)
        #    print ("new stories file created.")

            with open("stories.json","w") as outfile:
                json.dump(stories, outfile)
            #stories.append({"dragon":{"setup":"once there was a dragon.","good_end":"you steal it's treasure","bad_end":"it kills you."}})
        except:
            print ("file could not be created.")

    #  ~~~~~~___~~~~~~~~~~___~~~~~~~~~~~~~~~~~~~~~~___~~~~~~~~~~~
    #  ~~~~~/\__\~~~~~~~~/\~~\~~~~~~~~~___~~~~~~~~/\__\~~~~~~~~~~
    #  ~~~~/:/~_/_~~~~~~/::\~~\~~~~~~~/\~~\~~~~~~/:/~_/_~~~~~~~~~
    #  ~~~/:/~/\~~\~~~~/:/\:\~~\~~~~~~\:\~~\~~~~/:/~/\__\~~~~~~~~
    #  ~~/:/~/::\~~\~~/:/~/::\~~\~~~~~~\:\~~\~~/:/~/:/~_/_~~~~~~~
    #  ~/:/_/:/\:\__\/:/_/:/\:\__\~___~~\:\__\/:/_/:/~/\__\~~~~~~
    #  ~\:\/:/~/:/~~/\:\/:/~~\/__//\~~\~|:|~~|\:\/:/~/:/~~/~~~~~~
    #  ~~\::/~/:/~~/~~\::/__/~~~~~\:\~~\|:|~~|~\::/_/:/~~/~~~~~~~
    #  ~~~\/_/:/~~/~~~~\:\~~\~~~~~~\:\__|:|__|~~\:\/:/~~/~~~~~~~~
    #  ~~~~~/:/~~/~~~~~~\:\__\~~~~~~\::::/__/~~~~\::/~~/~~~~~~~~~
    #  ~~~~~\/__/~~~~~~~~\/__/~~~~~~~~~~~~~~~~~~~~\/__/~~~~~~~~~~
    #  ~~~~~~___~~~~~~~___~~~~~~~~~~___~~~~~~~~~~___~~~~~~~~~~~~~
    #  ~~~~~/\__\~~~~~/\~~\~~~~~~~~/\~~\~~~~~~~~/\__\~~~~~~~~~~~~
    #  ~~~~/:/~_/_~~~~\:\~~\~~~~~~~\:\~~\~~~~~~/:/~~/~~~~~~~~~~~~
    #  ~~~/:/~/\__\~~~~\:\~~\~~~~~~~\:\~~\~~~~/:/~~/~~~~~~~~~~~~~
    #  ~~/:/~/:/~~/___~~\:\~~\~~_____\:\~~\~~/:/~~/~~___~~~~~~~~~
    #  ~/:/_/:/~~//\~~\~~\:\__\/::::::::\__\/:/__/~~/\__\~~~~~~~~
    #  ~\:\/:/~~/~\:\~~\~/:/~~/\:\~~\~~\/__/\:\~~\~/:/~~/~~~~~~~~
    #  ~~\::/__/~~~\:\~~/:/~~/~~\:\~~\~~~~~~~\:\~~/:/~~/~~~~~~~~~
    #  ~~~\:\~~\~~~~\:\/:/~~/~~~~\:\~~\~~~~~~~\:\/:/~~/~~~~~~~~~~
    #  ~~~~\:\__\~~~~\::/~~/~~~~~~\:\__\~~~~~~~\::/~~/~~~~~~~~~~~
    #  ~~~~~\/__/~~~~~\/__/~~~~~~~~\/__/~~~~~~~~\/__/~~~~~~~~~~~~
    #  ~~~~~~~~~~~~~~~~~~~~~~~~___~~~~~~~~~~___~~~~~~~~~~___~~~~~
    #  ~~~~~~~~~~~~~~~~~~~~~~~/\~~\~~~~~~~~/\~~\~~~~~~~~/\__\~~~~
    #  ~~~~~~___~~~___~~~~~~~/::\~~\~~~~~~~\:\~~\~~~~~~/:/~_/_~~~
    #  ~~~~~/\__\~/\__\~~~~~/:/\:\~~\~~~~~~~\:\~~\~~~~/:/~/\~~\~~
    #  ~~~~/:/~~//:/__/~~~~/:/~~\:\~~\~~_____\:\~~\~~/:/~/::\~~\~
    #  ~~~/:/__//::\~~\~~~/:/__/~\:\__\/::::::::\__\/:/_/:/\:\__\
    #  ~~/::\~~\\/\:\~~\__\:\~~\~/:/~~/\:\~~\~~\/__/\:\/:/~/:/~~/
    #  ~/:/\:\~~\~~\:\/\__\\:\~~/:/~~/~~\:\~~\~~~~~~~\::/~/:/~~/~
    #  ~\/__\:\~~\~~\::/~~/~\:\/:/~~/~~~~\:\~~\~~~~~~~\/_/:/~~/~~
    #  ~~~~~~\:\__\~/:/~~/~~~\::/~~/~~~~~~\:\__\~~~~~~~~/:/~~/~~~
    #  ~~~~~~~\/__/~\/__/~~~~~\/__/~~~~~~~~\/__/~~~~~~~~\/__/~~~~
    #  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def save_questions():
    global questions
    with open("trivia.json","w") as outfile:
        json.dump(questions, outfile)
        print ("questions saved!")

def save_mask():
    global character
    with open('masks.json', "r") as readfile:
        masks = json.load(readfile)
    #print ("okay, so if I print each thing in the character I get this:")
    #for i in character:
    #    print (i)

        if character["name"]=="unknown":
            print("This is your first time saving.")
            character["name"]=str(input("what is the name of this character?"))

        else:
            print ("Saving", character["name"])
        time.sleep(1)

    #    masks[name]=character
        #check to see if mask exists

            #masks[character["name"]]=character
        #else:
        #    print
    name=character["name"]
    #print ("If the masks loaded, there is this:", masks)
    #print ("here is the character:", character)
    readfile.close
    masks[name]=character
    print (masks[name])
    with open('masks.json', "w") as outfile:
        json.dump(masks, outfile)
        print("new mask should be saved!")
    time.sleep(1)
    exit()

#  ~~~~~~___~~~~~~~~~~___~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~___~~~~~
#  ~~~~~/\__\~~~~~~~~/\~~\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/\__\~~~~
#  ~~~~/:/~~/~~~~~~~/::\~~\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/:/~_/_~~~
#  ~~~/:/~~/~~~~~~~/:/\:\~~\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/:/~/\~~\~~
#  ~~/:/~~/~~___~~/:/~/::\~~\~~___~~~~~___~~___~~~~~___~~/:/~/::\~~\~
#  ~/:/__/~~/\__\/:/_/:/\:\__\/\~~\~~~/\__\/\~~\~~~/\__\/:/_/:/\:\__\
#  ~\:\~~\~/:/~~/\:\/:/~~\/__/\:\~~\~/:/~~/\:\~~\~/:/~~/\:\/:/~/:/~~/
#  ~~\:\~~/:/~~/~~\::/__/~~~~~~\:\~~/:/~~/~~\:\~~/:/~~/~~\::/~/:/~~/~
#  ~~~\:\/:/~~/~~~~\:\~~\~~~~~~~\:\/:/~~/~~~~\:\/:/~~/~~~~\/_/:/~~/~~
#  ~~~~\::/~~/~~~~~~\:\__\~~~~~~~\::/~~/~~~~~~\::/~~/~~~~~~~/:/~~/~~~
#  ~~~~~\/__/~~~~~~~~\/__/~~~~~~~~\/__/~~~~~~~~\/__/~~~~~~~~\/__/~~~~

main()
