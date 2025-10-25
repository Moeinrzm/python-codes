import gtts
import os

text=input("enter text your text:")

speech=gtts.gTTS(text=text,lang='en',slow=False)
speech.save("voice.mp3")
os.system("voice.mp3")