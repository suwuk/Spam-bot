from typing import MutableMapping
import pyautogui
import time

massage = input("Masukan pesan : ")
ulang = int(input("Masukan Berapa kali : "))
time.sleep(5)
for i in range (ulang):
    pyautogui.typewrite(massage)
    pyautogui.press('enter')
    time.sleep(2)