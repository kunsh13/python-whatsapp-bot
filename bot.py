pip install pyautogui



import pyautogui as pg
import time
time.sleep(10)

txt = open('animals.txt','r')
for i in txt:
    pg.write(a+' '+i)
    pg.press('Enter')
    
