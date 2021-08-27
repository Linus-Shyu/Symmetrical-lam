print("----------------------------------------------------------------")
print("X          X     XXXXX        X   X       X     X         X   X")
print("X          X     X   X        X   X          X            X   X")
print("X          X     X   X        X   X         X  X          X   X")
print("X X X X    X     X   X        XXXXX      X       X        XXXXX")
print("----------------------------------------------------------------")


import os, time

import pyautogui as pag

try:
    while True:
        print("按下Ctrl + C 结束程序")
        print("Mac用户请按下control+c")
        x, y = pag.position()
        posStr = "当前鼠标位置:" + str(x).rjust(4) + ',' + str(y).rjust(4)
        print(posStr)
        time.sleep(1)
        os.system('cls')
except KeyboardInterrupt:
    print('已退出')
