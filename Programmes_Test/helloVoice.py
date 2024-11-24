import pyttsx3
engine = pyttsx3.init()
name=input("what's your name?")
engine.say(f" Hello {name}")
engine.runAndWait()