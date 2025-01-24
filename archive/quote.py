
# coding: utf-8

# # quote of the day

# In[1]:


import json
import random


# In[2]:


quote_list={}
with open("quotes.json", "r") as readfile:
    quotes = json.load(readfile)
    #for i in quotes:
     #   print (quotes[i]["quote"])
    roll=random.choice(list(quotes.keys()))
    print (quotes[roll]["quote"])


# In[3]:


def add_quote():
    global quotes
    choice = input("Do you want to add a quote? (y/n)")
    if choice == "y" or choice =="yes":
        print ("you said yes.")
        try:
            new_quote= str(input("Type the quote here:"))
            print ("The quote was", new_quote)
            total_quotes=len(quotes)
            print ("the number of quotes is", total_quotes)
            this_quote = total_quotes + 1
            print ("this quote will be", this_quote)
            #quotes[len(quotes)]["quote"]=new_quote
            #print
            #quotes[this_quote]:["quote"]= new_quote
            #print (quotes[this_quote])
            #print (quotes)
            new_author=str(input("Who was the author?"))
            new_title=str(input("What was the title of the book or poem?"))
            new_page=str(input("What page was this on?"))
            quotes.update({this_quote:{"title":new_title,"author":new_author,"page":new_page}})
            print (quotes)
            save_quotes()
        except:
            print ("something went wrong.")
    else:
        print ("you said no.")


# In[6]:


def save_quotes():
    global quotes
    with open("quotes.json", "w") as outfile:
        try:
            json.dump(quotes, outfile)
            print ("quotes saved!")
        except:
            print ("oh noes! malfunction!!")


# In[7]:


add_quote()
