from gtts import gTTS
import os

myText= "Welcome back admin, How may i assist you today?"

language = 'en'

output = gTTS(text=myText, lang=language, slow=False)

output.save("output.mp3")

os.system("start output.mp3")