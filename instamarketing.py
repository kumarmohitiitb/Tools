import pyautogui
while (True):
	l = ["tinder","happn","badoo","trulymadly","twoo"]
	for i in range(5):
		pyautogui.click(x=710, y=131, button='left')
		pyautogui.click(x=710, y=131, button='left')
		pyautogui.PAUSE = 5
		pyautogui.typewrite(l[i]+'\n\n')
		pyautogui.typewrite('\n\n')
		pyautogui.PAUSE = 5
		pyautogui.click(x=680 , y=300 , button='left')
		pyautogui.PAUSE = 5
		for i in range(60):
			pyautogui.click(x=890 , y=240 , button='left')
			pyautogui.scroll(-2)
			pyautogui.PAUSE = 1
		j=1
		while (j<450):
			pyautogui.moveTo(300,400)
			pyautogui.PAUSE = 1
			pyautogui.moveTo(600,600)
			j += 1
	
