#questions
import json
from start import *
try:
    load_questions()
except:
    print("couldn't run load_questions from start.py")

def add_question():
    global questions, character

    with open('questions.json', "r") as readfile:
        questions = json.load(readfile)
        #print ("annoyingly, I had to load questions from this program.")
    
        for i in questions:
            print (i)
        try:
            print (questions)
        except:
            print ("questions not loaded")
    ans = str(input("do you want to add a question?"))
    if ans =="y":
        new_question=str(input("what is the question?"))
        new_answer=str(input("what is the answer?"))
        new_subject=str(input("what subject?"))
        n = len(questions)+1
        print ("the number of questions is", n)
        try:
            questions.update({new_question:{"a":new_answer,"subject":new_subject}})
        #character["xp"]+=6
        except:
            print ("somtehing went wrong")
        ans =str(input("enter another question y/n?"))
        if ans =="y":
            add_question()
        else:
            from start import save_questions
            pass
    save_questions()

if __name__ == '__main__':
    add_question()
