#Text to Talk

import sys

try:
	import pyttsx3
except ImportError:
	print('The pyttsx3 module needs to be installed to run this.')
	print('For Linux')
	print('pip3 install pyttsx3')
	sys.exit()
tts = pyttsx3.init()

def raz():
	tts.say("i am razzie")
	tts.runAndWait()

def Y_N():
	tts.say("yes or no")
	tts.runAndWait()

def login(textA):
	tts.say(f"please enter {textA}")
	tts.runAndWait()

def pwrd():
	tts.say("do you wish to shut down")
	tts.runAndWait()

def gameA(textB):
	tts.say(f"do you want to play {textB}")
	tts.runAndWait()

def gameB(textC):
	tts.say(f"or {textC}")
	tts.runAndWait()

def chooseA(textD):
	tts.say(f"Would you like to {textD}")
	tts.runAndWait()

def chooseB(textf):
	tts.say(f'{textf}')
	tts.runAndWait