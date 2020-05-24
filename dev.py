import os, json, random, time, math

from poemify import *


## from poemify import poemify

##### there could be a significance to the comment hashes, where the length of them determines how many estimated turns until they are ready to be activated or incorporated into the functional parts of the program.
### or if not the actual module then the idea of poemification
###### the idea of the meme worked well, in that the random quote selection was actually useful and appropriate. It set a word count goal for the day of 1,600 words, and If that goal was met, then my character would gain the day's count as XP. Every time a comment, like a meme, is downvoted, another comment hash is added. They function like hit points, or damage markers, and if they go above six, the meme is deleted, or the character dies.
### where there is an axis of method implicit but not visible to the synchronic
### product or effect.

from error import *

# the error offers one gateway out, one node that isn't standard
### an internal library of mine
#### a system of indented significance, ranked positions horizontal.
##### limiting the number of comments per section or function to six.
##  To write I have to be able to inhabit one link at a time of a semiotic chain.

text = "All development files will have a text variable, by ideological default. The next step would be to make new texts a class of Text, with built in functions such as word count and poemify."
#  TEXT
##  This program should
###  create a record for every turn in a day (game).
###  give a point of experience to Tetao everytime it is run.
####  currently, I don't think this is happening. So sneaky, though (I'd forgotten about it.)
#####  the theif character. Who occasionally sneaks into mondays, the start of them, taking time that would otherwise have been spent differently.
######  game philosophpy: take whatever lines are above and below you seriously. Same at the level of sections, and programs.
# TODO

## set up hidden xp award.
### choose root story
##### move successful code into the writing_game file.
###### give memes functionality as a class, with voting.
# write file manifesto
#### write new story

total_turns = 0

##turns of the game, not deep turns

# START

####  You hold the shell in your hand. 'It is back to zero,' you say.
#####  'We must have died,' the other says, uncertainly.
main_file = "drift.txt"
###  'The more words we write,' you tell her, 'the more our abilities and memories will return. That, I think, has always been our quest. To remember.
# To hang experience
## on the lines of music out to dry.'

play_again = True

# you gain the will to survive, to play the game, to learn and grow and adapt and die.
## ecological fantasy. The overarching problems of climate intrude on lower levels of meaning. Science nerds geek out about a role playing game, while gamifying their serious research or mission.

def intro(main_file):
    ###  the two of you are standing by a mountain pool, watching fish. "Go ahead," Cora says, "call one of them."



    ###  Here, then, is the first chllenge. Before anything else, I have to get turn_stats to be a thing. In game-data/data.json, you can add to the dictionary. right now there are "avg_wpm" and "total_turns."

    #print(
#        "Scape and Camilla have left the crime-drenched racing planet of their birth, the brutal bio-reactors of Arma.")

    print ("The main file for today, the on which the final word count will be based, is ", main_file)

    # next_step = "'I can do any file,' I was thinking. 'Whichever one Atom opens up to. Starting at 7:40 am. Really, though, the record that needs to be broken is words per day. Wpd.'"

    words = ["These types of lists can be saved from the fire at the end of files, moved sideways into other realms.","Each file has a place, a character, and story. An about section, a footer, and index /menu.", "In a way, writing in python allows a meta level, where I can express ideas via demonstration.", "I think I see how it works. If you go for a while without saving, it is possible to cheat on a word count, but you run the danger of losing the new information from the file. Do you, though? Atom does a good job with auto-saving, but apparently not to the file itself."]

    # "There is a path here," the fox says. "You can follow it." He has an attack strength of 6, a speed of 5, defense of 4, health of 2, range of 1, and magic of 3. It has 6 experience points, so is level 1.

    #    print ("After the battle with the death worshippers, Tetao and Salena stayed up late in the common room of the Inn of Last Night's Moon, dancing. They were in a small town called Telos, that happened to lay upon a powerful convergence of ley lines. Both Tetao and Selena drew, as the night went on, from the magical channels, but in different ways: Tetao to tell stories, and Salena to capture audiences with her singing.")

    # "This is the best of the worlds," Thetao sang, not mocking her style but showing a playful awareness of it. His own voice was strong, but nowhere near as trained as hers. His own receptacle for the most effortful and honest communications went towards telepathy. A violin and mandolin and cello were playing. "That is the best possible combination of three instruments," he said, then caught himself. "Not including voice."

    # Salena smiled, nodding at the correction. "Wouldn't a better world be one not only where are dimension was utopian, but all adjacent worlds as well? Then we would not be in such constant danger."

    # They looked around, both aware that many of the aspects of the inn were taken from other places, the basic codes the same.

    # "The coded contents of the file will come and go," Thetao said, "but the meta-story, the one in the comments, will persist, and the Inhabitant can keep making it better."

    # "We can write a thousand words," the healer answered.

    # "Easily," he agreed. "Which will imbue the earth-staff with enough power to defeat the monsters at the gate."

    #

    memes = {
        "memes are stored in a dictionary, defined as a fitness value that affects their likelihood of repreduction.": 6,
        "The variables operate at a level of pseudo-code, where they can make suggestions about their own methods.": 5,
        "At the beginning of every turn, a meme or quote or trivia question is shown as a loading screen, and once the game is ready, there is the question 'was that meme/image/entry useful?', the answer to which will cause the fitness value of the corresponding fragment to incease or decrease.'": 5,
        "Today, my word count goal is 1,600. If I reach it, I get that many experience points.": 2,
        "From this file, this collection of associated syntax (that of it that passes the gates) will glob onto the drift, attracting more like-minded proto-memes.": 2,
        "The charmed castle for today, though, is obviously Ishtar, and the dark forest in general. I'm trying to develop a new way of talking about he larger ideas and design strategies of the game.": 0,
        "The lists and verbiage accumulated with astonishing speed, and unrealistic expectations as for future use.": 3,
        "'How far can we go, today?' the ranger asked, touching one by one the tools of their survival, including water, rations, weapons, and extra layers against the cold. She didn't answer, her thoughts going from the question he had asked to something else, and he didn't press her, nor did he answer his own question. After a while she reached out and touched his hand.": 1, }

    class meme:

        ##  as far as I know, this class is never called, and is still
        ##  unfunctional pseudo-code

        def __init__(self, text, fitness):
            self.fitness = fitness
            self.text = text

            # self.description = description

            def vote(fitness):
                fitness += 1

            print("your fitness is now", fitness)

    # a_meme=meme("I am a sphere, and reflect all images in the universe simply by existing.", 6)

    meme_choice = random.choice(list(memes.keys()))
    print("Your meme is \n \n \n", meme_choice, "\n\n\n")
    input()


# print (a_meme.fitness)

# what are the conventions around class names? ClassNames?


def load_data():
    global data
    # data file exists

    if os.path.isfile("game-data/data.JSON"):

        #        print ("'It's here!' Scape called up to Kate. 'The box did't lie to us this time!")

        # if data size is > 0

        if os.path.getsize("game-data/data.JSON") > 0:
            #    print ("data bigger than zero.")
            with open("game-data/data.JSON", "r") as rf:
                data = json.load(rf)
        #                print ("upon loading the data/opening the box, you see the following values:")

        #                for i in data:
        #                    print (i, "is", data[i])

        # if is empty
        else:
            data = {"avg_wpm": 10}
            save_data()
            load_data()


    # if doesn't exist
    else:
        print("data file not found. attempting to create.")

        data = open("game-data/data.JSON", "w")
        #   os.mknod("game-data/data.JSON")
        data = {"avg_wpm": 9.5}
        save_data()
        load_data()

        print("failed to create file data.")

        print(
            "Next time you run the file you should see this. \nRotate 25 minutes of actual writing with 25 minutes of coding or planning. \n make the timer more interesting.")

    if "total_games" in data:

        total_games = data["total_games"]
        # print ("So far, you have played", total_games, "games")
        # input()
        total_games += 1
        print("This is now game", total_games)
        # save data
        data["total_games"] = total_games
        save_data()
    else:
        print("total games not detected.")
        try:
            data["total_games"] = 0
        except:
            print("couldn't set games turns to zero.")
        try:
            total_games = 0
            data["total_games"] = 0
            save_data()
            print("This is your first turn")
        except:
            print("couldn't set total turns to data")
            load_messages()
            give_message()

    ### NEW: I want to create a dictionary entry called total_words, and another called total_minutes. This should save when the data is dumped when the game closes.

    if "deep_words" in data:

        deep_words = data["deep_words"]
        print("Since writing this program, you have used it to write", deep_words, "words.")

        #        total_turns += 1
        #        print ("Your total turns are now" ,total_turns)
        # save data
        data["deep_words"] = deep_words
        try:
            with open("game-data/data.JSON", "w+") as wf:
                json.dump(data, wf)
        except:
            print("data with updated turn count didn't save.")
    else:
        print("deep words not detected.")
        try:
            data["deep_words"] = 0
        except:
            print("couldn't set deep words to zero.")
        try:
            deep_words = 0
            data["deep_words"] = 0
            print("You are wordless")
        except:
            print("couldn't set deep words to data")
            load_messages()
            give_message()
        save_data()

    if "deep_minutes" in data:

        deep_minutes = data["deep_minutes"]

        print("You have played the writing game for a total of", deep_minutes, "minutes.")
        #        deep_turns += 1
        #        print ("Your deep turns are now" ,deep_turns)
        # save data
        data["deep_minutes"] = deep_minutes
        try:
            with open("game-data/data.JSON", "w+") as wf:
                json.dump(data, wf)
        except:
            print("data with updated minute count didn't save.")
    else:
        print("deep minutes not detected.")
        try:
            data["deep_minutes"] = 0
        except:
            print("couldn't set deep minutes to zero.")
        try:
            deep_minutes = 0
            data["deep_minutes"] = 0
            print("You are wordless")
            save_data()
        except:
            print("couldn't set deep minutes to data")
            load_messages()
            give_message()

    ## NEW
    #### Attempt to check and see if data["games"] exists, and create if not.
    try:
        pass

    # "Okay," Cora said, "We're close to getting a working record system."
    except:
        pass
    try:
        if "games" in data:
            print("there are games records in data.")
            for i in data["games"]:
                print(i)
        else:
            data["games"] = {}
            data["games"]["turn_1"] = {}
    except:
        print("Scape and Cora get thrown out of the airlock.")
        load_messages()
        give_message()


# And now to save.
def save_data():
    global data
    with open("game-data/data.JSON", "w") as wf:
        json.dump(data, wf)


def save_masks():
    global data
    with open("game-data/masks.JSON", "w") as wf:
        json.dump(masks, wf)


# with open("game-data/data.JSON", "r") as rf:
#    data=json.load(rf)
#    try:
#        for i in data:
#            print (i)
# print (data["hooks"])
#    except:
#        print ("couldn't print data from file.")


def turn(text_file):
    # Once this is working, I'll move it to development for the next stage.
    global play_again, data, total_turns, sum_total_minutes, sum_total_words, sum_scores, average_score
    print("play again is set to ", play_again)

    # all data should be loaded.

    class turnStats:
        def __init__(self, words, minutes, wmp, score):
            self.words = words
            self.minutes = minutes
            self.wmp = wmp
            self.score = score

    turn_stats = turnStats(0, 0, 0, 0)

    # load_data()

    ####  NEW

    words = []
    try:
        high_score = data["high_score"]
        print("The high score is", high_score)
    except:
        print("high score not available")

    total_turns += 1
    # get turn name
    try:
        total_games = data["total_games"]
        game_name = "game_" + str(total_games)
        print("game name set to", game_name)
        try:
            if game_name in data["games"]:
                print("that game name is in the data.")
            else:
                print("That game name is not listed. creating now.")

                ###  Scape gets up early and goes out on the balcony with a cup of tea to watch the sun rise over the tracks. Today, he thinks, will be one for the record books.

                data["games"][game_name] = {}
        except:
            print("something went wrong with reading or creating the game data.")

    except:
        print("problem with game name")
    try:
        turn_name = "turn_" + str(total_turns)

        print("the turn name is", turn_name)

        data["games"][game_name][turn_name] = {}

    ## This might be the point at which victory is awarded.

    ###
    except:
        print("couldn't make name, or couldn't create data.")
        load_messages()
        give_message()
    print("It is now turn", total_turns, "\n")
    keys = [0, 1, 2, 3, 4, 5, 6, 7]
    key_field = []
    for i in keys:

        # print (lines.index(i))
        magnifier = keys.index(i)
        # print ("will be used to generate copies. Populations multiplied by magnifier in the new list.")
        count = 0
        # oh, or the first one isn't even shown. I kind of like that.
        while count < magnifier:
            key_field.append(i)
            count += 1
    key = random.choice(key_field)

    #    data["genres"]=[]

    genres = data["genres"]
    save_data()

    genre = genres[key]
    print("This story is", genre)
    hooks = []
    hooks = data["hooks"]
    hook = hooks[key]
    #    data["openers"]=[]

    openers = data["openers"]

    opener = openers[key]
    # good_ending="the health of the ecosystem improves, and the territory of the tribes expands."
    #    data["good_endings"]=[]

    good_endings = data["good_endings"]
    good_ending = good_endings[key]

    ##bad_endings not complete, nor called.
    # data["bad_endings"]=[]

    bad_endings = data["bad_endings"]
    bad_ending = bad_endings[key]
    # you should write something to check and make sure data exists.
    twists = data["twists"]
    twist = random.choice(twists)
    print(twist)
    # twist=random.choice(twists)
    # print (twist)
    save_data()

    # high_score=0

    with open(text_file, "r") as rf:
        word_count = 0
        for word in rf.read().split():
            word_count += 1

    print("That file has", word_count, "words.\n", opener)
    time_goal = int(input("how many minutes do you want to work?"))
    word_goal = int(input("how many words can you write?"))
    start_time = time.time()
    print(hook)
    turns.append(total_turns)
    words.append(word_count)
    # plot(turns, words)
    str(input("press enter when done"))

    #####   RESULTS

    total_time = time.time() - start_time
    print("Your total time was ", total_time)
    # working_text = open("pseudo_text.txt", "r+")
    new_word_count = 0
    with open(text_file, "r") as rf:

        for word in rf.read().split():
            new_word_count += 1
    print(text_file, "now has", new_word_count, "words.")
    # new_word_count+=1
    word_difference = new_word_count - word_count
    total_minutes = math.ceil(total_time / 60)
    sum_total_minutes += total_minutes
    sum_total_words += word_difference

    print("You wrote ", word_difference, "new words in", total_minutes, "minutes")
    wpm = math.ceil(word_difference / total_minutes)
    # print ("the high score is", high_score)
    print("You wrote", wpm, "words per minute.")

    ####data to plot
    turns.append(total_turns)
    words.append(new_word_count)
    # plot(turns, words)
    # the plot thickens

    ## Going to try to save turn data
    try:
        print("game name is", game_name)
        print("the turn name is", turn_name)
    except:
        print("couldn't print relevant vars")
    #    data["games"][game_name]={}

    ## The empty dictionary now only gets created if there is no turn_name.
    try:

        data["games"][game_name][turn_name] = {}

        ## you need to change these numbers to variables data[game][turn]
        data["games"][game_name][turn_name]["words"] = word_difference
        print("we saved your words in the data for this turn.")
        ## next save minutes
        data["games"][game_name][turn_name]["minutes"] = total_minutes
        ## save wpm
        data["games"][game_name][turn_name]["wpm"] = wpm
        save_data()
        print("If you have gotten to this point in the file, there should now be data saved for", game_name, "turn",
              turn_name)
    except:
        print("Scape, without a car to drive, falls into a deep depression. Couldn't save data.")
        load_messages()
        give_message()

    if total_minutes > time_goal:
        time_diff = total_minutes - time_goal
        print("You exceed your time goal by", time_diff, "minutes!")
        roll = random.randint(1, 6)
        score = wpm + roll
        print("Now your score is", score)

    ###  The demon door swings closed, and you and your brave companions collapse into exhaustion. Your numbers have been reduced.
    else:
        print("You did not meet your time goal! Score lowered by 1d6.")
        roll = random.randint(1, 6)
        score = wpm - roll
        print("which makes your score", score)

    if word_difference > word_goal:
        over_goal = word_difference - word_goal
        print("You exceeded your word goal by", over_goal, "words!")
        #	stats["xp"]+=1
        roll = random.randint(1, 6)
        score = score + roll
    else:
        print("You did not meet your word goal! Subracting 1d6 from score.")
        # print (sent_list)
        # for i in range(roll):
        roll = random.randint(1, 6)
        score = score - roll
    # I like that I keep these dice lying around.
    print("Your final score for this turn is", score)
    data["games"][game_name][turn_name]["score"] = score

    if score > high_score:

        high_score = score
        print(high_score, "is the new high score!")
        data["high_score"] = high_score
        save_data()

        print(good_ending)
    else:
        print(bad_ending)

    print("the total words you have written are", sum_total_words)

    # add to deep words
    try:
        data["deep_words"] += word_difference
        print("deep word count is", data["deep_words"])
        save_data()
    except:
        print("deep words are lost.")
        load_messages()
        get_message()
    print("in all you have written for", total_minutes, "minutes")
    # add to deep minutes
    try:
        data["deep_minutes"] += total_minutes
        print("deep time count is", data["deep_minutes"], "minutes")
        save_data()
    except:
        print("deep time is lost.")
        load_messages()
        get_message()

    sum_scores += score
    # wait, score should reset to zero after this.
    # else:
    #    sum_scores=score

    average_score = sum_scores / total_turns
    # right?
    print("In", total_turns, "turns, your average score has been", average_score)
    ans = str(input("play again?"))

    ## a seed-bearing epilogue. The gnoll wandered through the grass, knowing he could catch up to the rest of the party later.

    if ans == "y":
        play_again = True
    else:

        play_again = False
    # quit()


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
##############################version 2.0#########

# roll = random.randint(1,6)


# I'm not sure if now_variable is a good convention--a little too close to "new_variable"

# persistence, the gamification of work and learning.

def save_data():
    global data
    #    for i in data:
    #        print ("saving", data[i], "as", i )
    # for x in data[i]:
    #    print ("saving", x)

    with open("game-data/data.JSON", "w") as wf:
        json.dump(data, wf)


def start():
    global average_score, sum_scores, sum_total_words, sum_total_minutes, turns, xp
    print("within the start function, setting average_score, and other variables as globals.")
    average_score = 0
    sum_scores = 0
    sum_total_words = 0
    sum_total_minutes = 0
    turns = []
    xp = 0


def give_xp(new_xp):
    # How would you add something to the beginning or end of a list in python?

    global masks
    if os.path.isfile("game-data/masks.JSON"):
        #        print ("'It's here!' Scape called up to Kate. 'The box did't lie to us this time!")

        # if data size is > 0

        if os.path.getsize("game-data/masks.JSON") > 0:
            #    print ("data bigger than zero.")
            with open("game-data/masks.JSON", "r") as rf:
                masks = json.load(rf)
        #                print ("upon loading the data/opening the box, you see the following values:")

        #                for i in data:
        #                    print (i, "is", data[i])

        # if is empty
        else:
            masks = {"thetao": {"xp": 12}}
            save_data()
            load_data()


    # if doesn't exist
    else:
        print("masks file not found. attempting to create.")

        masks = open("game-data/masks.JSON", "w")
        #   os.mknod("game-data/data.JSON")
        masks = {}
        save_data()
        load_data()

        print("failed to create masks file.")

        print(
            "Next time you run the file you should see this. \nRotate 25 minutes of actual writing with 25 minutes of coding or planning. \n make the timer more interesting.")

    try:
        if "thetao" in masks:
            if "xp" in masks["thetao"]:
                xp = masks["thetao"]["xp"]
                xp += new_xp
                masks["thetao"]["xp"] = xp
                save_masks()
            else:
                masks["thetao"]["xp"] = 12
        else:
            masks["thetao"] = {}
            masks["thetao"]["xp"] = 12
            save_masks()
    except:
        print("we couldn't award thetao xp")


load_data()
intro(main_file)
give_xp(6)
start()

text_file = str(input("what scroll do you want to open? "))

while play_again:
    # text_file="drift.txt"
    turn(text_file)
save_data()

try:
    # EXIT

    ## This will be moved to a file in dropbox, where I need to start putting all of there ragged journal entries. When it is difficult to write, to choose one of the fictions to pursue, or projects to commit to, there always needs to be the comfortable conventions and associations of trying, in time-honored tradition, of saying something true about the present.

    ## These files are safe, or at least as much as can reasonably be expected, hidden as they are in an impressive amount of verbiage. I was going through old files, not for the first time, coming across something occcasionally of neglected value. Thinking, not for the last time, that I need a better system for organizing files, preventing the accumulation of trash and duplication.

    # The one main project that I wanted to work on was the firestore database for the improv games. I have too many cloned copies of the repository, none of them working.

    save_data()
# import poemify.py

except:
    #    input("couldn't save data.")
    load_messages()
    give_message()

#  https://www.mandolincafe.com/tab/jerusalem.txt
#
#    C Part
#     Am                                  C
#   |-0---5---5-----3-|-5---7---8-------|---3-----3-------|-3-8-5-3---------|
#   |-7---------------|-------------5-6-|-7-----7-------7-|---------7-5-3-5-|
#   |-----------------|-----------------|-----------------|-----------------|
#   |-----------------|-----------------|-----------------|-----------------|
#     |   |   |.   .|   |   |   |   |_|   |_|_|_| |_|_|_|   |_|_|_| |_|_|_|
#     (slide up)
#     3   2   2     1   2   3   4   1 2   3 1   3 1     3   1 4 2 1 3 2 1 2
#     <--suggested fingering-->
#
