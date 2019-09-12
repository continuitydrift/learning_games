#file to start the game.

import os, json
from questions import *

def load_questions():
    global questions

    # check to see if the file exists. If so, load it.
    if os.path.isfile("questions.json"):
        with open('questions.json', "r") as readfile:
            questions = json.load(readfile)
        print ("The questions file exists")
    #If not, create it.
    else:
        print ("no questions file detected")
        try:
            questions={}
            with open("questions.json","w") as outfile:
                json.dump(questions, outfile)
        except:
            print ("file could not be created.")

    # check to see if there are questions (if dictionary is empty)
    if not questions:
        print ("There aren't any questions")
    try:
        #test create new question
        questions["In what era was the Cretaceous Period?"]={"a":"Mesozoic", "subject": "history"}
    #    print (questions["In what era was the Cretaceous Period?"])
    except:
        print ("Some problem was encountered creating a test question.")

def save_questions():
    with open("questions.json","w") as outfile:
        json.dump(questions, outfile)
        print ("questions saved!")


if __name__ == '__main__':
    load_questions()
    save_questions()

    add_question()
