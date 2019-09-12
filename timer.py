import time, os, pygame, random
# todo
## more sounds to start/end
### find sounds
### edit sounds
### import sounds
### randomized sounds
##  create learning-games repository
##  add images
##  add quotes

#from playsound import playsound
pygame.mixer.init()


pygame.mixer.music.load("sounds/start-end.mp3")

#end_time = vlc.MediaPlayer("file:///start_end.mp3")
#end_time.play()
def set_time():
    global target
    try:
        target = int(input("how many minutes?"))
        pygame.mixer.music.play()
    except:
        print ("Something went wrong. Was that an integer?")

def run_clock():
    global target, seconds, minutes

    while seconds<60:
        time.sleep(1)
        try:
            os.system("cls")
        except:
            os.system("clear")
        seconds+=1
        display(minutes, seconds)
    minutes+=1
    seconds=0
    while minutes < target:
        run_clock()
#    playsound.playsound("start_end.mp3")

def display(minutes, seconds):
    print ("You have been working for", minutes, "minutes and", seconds, "seconds. \n")
    remaining = target - minutes
    print ("\n", remaining, "minutes left until target of ", target)
def end():
    pygame.mixer.music.play()
    #uses file loaded at beginning
    end_messages=["You have reached the end.", "Kudos.", "Well played."]
    end_message=random.choice(end_messages)
    print (end_message)
seconds=0
minutes=0
#playsound.playsound("start_end.mp3")
set_time()
run_clock()
end()
