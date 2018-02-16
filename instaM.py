import pyautogui
l = ["followforfollow"]
for i in range(1):
	pyautogui.click(x=727, y=132, button='left')
	pyautogui.click(x=727, y=132, button='left')
	pyautogui.PAUSE = 5
	pyautogui.typewrite(l[i]+'\n\n')
	pyautogui.typewrite('\n\n')
	pyautogui.PAUSE = 5
	while(True):
		pyautogui.click(x=399, y=453, button='left')
		pyautogui.PAUSE = 3
		pyautogui.moveTo(450,450)
		pyautogui.click(x=399, y=453, button='left')
		pyautogui.PAUSE = 0.1
		pyautogui.click(x=399, y=453, button='left')
		pyautogui.PAUSE = 0.1
		pyautogui.click(x=399, y=453, button='left')
		pyautogui.PAUSE = 0.1
		pyautogui.click(x=399, y=453, button='left')
		pyautogui.hotkey('esc')
		pyautogui.PAUSE = 10
		pyautogui.scroll(-7)
		pyautogui.PAUSE = 3

