from gtts import gTTS
import os

myText = "You don’t start out writing good stuff. You start out writing crap and thinking it’s good stuff, and then gradually you get better at it.That’s why I say one of the most valuable traits is persistence & Welcome to the Hell darling "
language = 'en'

myobj = gTTS(text=myText, lang=language, slow=False)
myobj.save("welcome.mp3")
os.system("mpg321 welcome.mp3")
