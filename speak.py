import pyttsx3
friend = pyttsx3.init()

active = True

print("Press Z to end the Loop")

while active :
    speech = input("Type Something : ")
    if(speech == 'Z') :
        active = False
        friend.say('Good Bye')
        friend.runAndWait()
    else :
        friend.say(speech)
        friend.runAndWait()

print("Thank You")