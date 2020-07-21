import os
import sys
import time
import win32gui
import win32con
import win32api
import win32process
import subprocess as subp

import timeit

try:
	import pyautogui
except :
	os.system('pip install pyautogui')


def startDeamon():
	# Returns an instance of subprocess api
	global Started
	instance=subp.Popen(['xmrig.exe'],stdout=subp.PIPE,shell=False)
	Started=True

	print('Deamon Started')
	return instance





Started=False
timer=0

while True:

	time.sleep(0.75)
	TaskManActive=pyautogui.getWindowsWithTitle('task')

	if Started==True  and TaskManActive :
		print('TM open = Killing')
		instance.kill();
		Started=False
		timer-=10 #penalty


	else: 
		if Started:
			timer+=1
			if timer % 10 ==0:
				print('Duration:','{:.3f}'.format(timer/3600),'h')

		if Started==False and not TaskManActive :
			instance=startDeamon()
			Started==True































# # XMRIG_ID=get_program_id_using_name()

# while True:
# 	#Fuzzy search all Titles
# 	# windowNames=pyautogui.getWindowsWithTitle('xmrig') 

# 	# get id of searched title by using internal method _hwnd 
# 	# ID=windowNames[0]._hWnd


# 	if pyautogui.getWindowsWithTitle('task'):
# 		print ('taskOba open ,PID :',XMRIG_ID)
# 		pauseMiner(XMRIG_ID)
# 	else:
# 		playMiner(XMRIG_ID)
# 	time.sleep(1)