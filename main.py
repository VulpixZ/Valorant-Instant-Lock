# pip install Pillow --upgrade
# pip install pyautogui --upgrade
# pip install opencv-python
#▒▒▒▒▒▒▒▒▒▒ 0%
#█▒▒▒▒▒▒▒▒▒ 10%
#██▒▒▒▒▒▒▒▒ 20%
#███▒▒▒▒▒▒▒ 30%
#████▒▒▒▒▒▒ 40%
#█████▒▒▒▒▒ 50%
#██████▒▒▒▒ 60%
#███████▒▒▒ 70%
#████████▒▒ 80%
#█████████▒ 90%
#██████████ 100%

import pyautogui as pag
from time import sleep as t

Agents = ["astra", "breach", "brimstone", "chamber", "cypher", "deadlock"
          "fade", "gekko", "harbor", "iso", "jett", "kayo", "killjoy",
          "neon", "omen", "phoenix", "raze", "reyna", "sage",
          "skye", "sova", "viper", "yoru"]

#---agents input
agents = pag.prompt(text="available agents : \n"
                         "astra\n"
                         "breach , brimstone\n"
                         "chamber, cypher\n"
                         "deadlock(WIP)\n"
                         "fade\n"
                         "gekko\n"
                         "harbor\n"
                         "iso\n"
                         "jett\n"
                         "kayo , killjoy\n"
                         "neon\n"
                         "omen\n"
                         "phoenix\n"
                         "raze , reyna\n"
                         "sage , skye , sova\n"
                         "viper\n"
                         "yoru",title="select your agent : ")

print("---:REBOOT SYSTEM:---")
print("---:.PLEASE WAIT.:---")
print("▒▒▒▒▒▒▒▒▒▒ 0%")
t(0.1)
print("█▒▒▒▒▒▒▒▒▒ 10%")
t(0.1)
print("██▒▒▒▒▒▒▒▒ 20%")
t(0.1)
print("███▒▒▒▒▒▒▒ 30%")
t(0.1)
print("████▒▒▒▒▒▒ 40%")
t(0.1)
print("█████▒▒▒▒▒ 50%")
t(0.1)
print("██████▒▒▒▒ 60%")
t(0.1)
print("███████▒▒▒ 70%")
t(0.1)
print("████████▒▒ 80%")
t(0.1)
print("█████████▒ 90%")
t(0.1)
print("██████████ 100%")
print("---:!SYSTEM READY!:---")
print("---:!!!STAND BY!!!:---")

if agents in Agents:
    for i in range(99999):
        if pag.locateOnScreen(agents + ".png", confidence = 0.8):
            print("-:.Instant locking.:-")
            # locate agents pic
            x = pag.locateCenterOnScreen(agents + ".png", confidence = 0.8)[0]
            y = pag.locateCenterOnScreen(agents + ".png", confidence = 0.8)[1]
            # locate lock in button
            xx = pag.locateCenterOnScreen("lock.png", confidence = 0.8)[0]
            yy = pag.locateCenterOnScreen("lock.png", confidence=0.8)[1]
            # go to agents pic
            pag.moveTo(x,y)
            pag.tripleClick(x,y)
            # go to lock in button
            pag.moveTo(xx,yy)
            pag.tripleClick(xx,yy)
            #Result
            print("-:.Operation Completed.:-")
            print(agents + " image cords : X : " + str(x) + " Y : " + str(y))
            print("lock button cords : X : " + str(xx) + " Y : " + str(yy))
            break
        else: print("Error 404 :" ,agents, "image not found.")
else:
    print("Error 303 : Agent :" ,agents, "is not available.")
