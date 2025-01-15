# You find yourself in a hexagonal library. You select some books at random.

import random, json, os, time
# check to see if quotes.json exits.

def main():
    global quotes
#    print ("hello")
    do_quotes_exist()
    load_quotes()
    save_quotes()
    quote()
    add_quote()

def do_quotes_exist():
    global quotes
    try:
        if os.path.isfile("quotes.json"):
            #print ("\n", "quotes exist", "\n")
            #time.sleep(.6)
            pass

            if os.path.getsize("quotes.json") > 0:
                #print ("\n", "and are greater than zero.", "\n")
                pass
                #time.sleep(1.2)
#                load_quotes()
            else:
                quotes = {"The primary record of prehistoric man during the long span of mid-Pleistocene time is provided by stone artifacts.": {"text":"Environment and Archaeology", "author-last": "Butzer", "author-first": "Karl", "year":"1971", "page":"436"}}
#                save_quotes()
        else:
            print ("\n\n\n", "quotes do not yet exist", "\n")
            quotes = {}
#            save_quotes()
    except:
        print ("You die. Try starting the quest again.")
        time.sleep(.6)

def save_quotes():
    global quotes
    try:
        with open("quotes.json", "w") as wf:
            json.dump(quotes, wf)
    except:
        print ("You die more. Try starting the quest again.")
        time.sleep(1.6)

def load_quotes():
    global quotes
    with open("quotes.json","r") as rf:
        quotes = json.load(rf)

def load_data():
    global data
    with open("data.json", "r") as rf:
        data = json.load(rf)
# quick test
    try:
        for i in data:
            print (data[i])
    except:
        error_message()

def quote():

    #I need to fix this, and add randomness to the selection.
    global quotes
    quote = random.choice(list(quotes.keys()))
 #   for i in quote:
  #      print (i)
    text = quotes[quote]["text"]
    author_first = quotes[quote]["author-first"]
    author_last = quotes[quote]["author-last"]
    year = quotes[quote]["year"]
    print ("\n\n", quote, "\n\n", "-", author_first, author_last, ",", text, ",", year)
    time.sleep(.6)


def add_quote():
    global quotes
    answer = str(input("do you want to add a quote? [y]/[n]?"))
    if answer == "yes" or answer == "y":

        # get the quote from the user
        new_quote = input(str("\nEnter the new quote:\n"))
        time.sleep(1)
        print ("you entered", new_quote)
        new_text = input(str("\nWhat text is that from?\n"))
        time.sleep(1)
        print ("you entered", new_text)
        new_author_last = input(str("\nWhat is the author's last name?\n"))
        time.sleep(1)
        print ("you entered", new_author_last)
        new_author_first = input(str("\nFirst Name? [enter for none]\n"))
        time.sleep(1)
        print ("you entered", new_author_first)
        new_year = input("\nWhat year was it wrtitten?\n")
        time.sleep(1)
        print ("you entered", new_year)
        new_page = input("\nWhat is the page number?\n")
        time.sleep(1)
        print ("you entered", new_page)
        try:
            quotes[new_quote]= {"text":new_text, "author-last": new_author_last,"author-first": new_author_first, "year": new_year,"page": new_page}
            for i in quotes[new_quote]:
                print (quotes[new_quote][i])
            save_quotes()
        except:
            error_message()
#        print ("adding quote...")
        time.sleep(1)
    else:
        print ("maybe next time")
        time.sleep(1)

def error_message():
    global data
    # As a literate programmer, I'm trying to create a meta/mini-game, where whenever my code breaks, a error_message function is triggered, that makes fun of me and my laughable skills.
    try:
        load_data()
    except:
        print ("You are a complete loser who knows nothing about computers and can't play the mandolin.")

main()
