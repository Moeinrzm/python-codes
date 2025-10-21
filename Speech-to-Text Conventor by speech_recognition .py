import speech_recognition

def speech_to_text():
    microphone=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        microphone.adjust_for_ambient_noise(source)
        print("I'm trying to hear you:")
        audio=microphone.listen(source)
        try:
            print("Recognizing:")
            phrase=microphone.recognize_google(audio,language="en")
            print(f"you said:{phrase}")
        except speech_recognition.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except speech_recognition.RequestError:
            print("Check your internet connection.")            
                     


