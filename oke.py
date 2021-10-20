from typing import MutableMapping
import pyautogui
import time

massage = ['Adam','Benzol','Copper','Idun','Mamang','Otoy','Bimo','Tepen','Rahul']
time.sleep(5)
for i in range (len(massage)):
    pyautogui.typewrite(massage[i])
    pyautogui.press('enter')
    time.sleep(2)
  



