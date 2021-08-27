print("----------------------------------------------------------------")
print("X          X     XXXXX        X   X       X     X         X   X")
print("X          X     X   X        X   X          X            X   X")
print("X          X     X   X        X   X         X  X          X   X")
print("X X X X    X     X   X        XXXXX      X       X        XXXXX")
print("----------------------------------------------------------------")
import pyautogui
import time
counts=3
while counts>0:
    pyautogui.click(x=1250, y=1012)
    time.sleep(5)
    pyautogui.click(x=766,y=461)
    time.sleep(3)
    pyautogui.click(x=838,y=352)
    time.sleep(2)
    pyautogui.click(x=1181,y=539)
    break
    