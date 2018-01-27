import pyautogui
while (True):
	pyautogui.click(x=1084, y=150, button='left')
	pyautogui.click(x=1084, y=150, button='left')
	pyautogui.PAUSE = 5
	pyautogui.click(x=803, y=295, button='left')
	pyautogui.PAUSE = 5
	for i in range(100):
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

