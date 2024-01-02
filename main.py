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

Agents = ["astra", "breach", "brimstone", "chamber", "cypher", "deadlock",
          "fade", "gekko", "harbor", "iso", "jett", "kayo", "killjoy",
          "neon", "omen", "phoenix", "raze", "reyna", "sage",
          "skye", "sova", "viper", "yoru"]


def select_mode():
    mode = pag.prompt(text="1 : Auto Lock\n2: Check list", title="Select mode")
    return mode


def auto_lock():
    agents = pag.prompt(text="Available agents:\n" + "\n".join(Agents), title="Select your agent:")

    print("---:REBOOT SYSTEM:---")
    print("---:.PLEASE WAIT.:---")
    for i in range(11):
        progress = i * 10
        print(f"\r{'█' * i}{'▒' * (10 - i)} {progress}% ", end="")
        t(0.1)
    print("\n---:!SYSTEM READY!:---")
    print("---:!!!STAND BY!!!:---")

    if agents.lower() in [agent.lower() for agent in Agents]:
        for _ in range(99999):
            if pag.locateOnScreen(agents.lower() + ".png", confidence=0.8):
                print("-:.Instant locking.:-")
                x, y = pag.locateCenterOnScreen(agents.lower() + ".png", confidence=0.8)
                xx, yy = pag.locateCenterOnScreen("lock.png", confidence=0.8)
                pag.moveTo(x, y)
                pag.tripleClick(x, y)
                pag.moveTo(xx, yy)
                pag.tripleClick(xx, yy)
                print("-:.Operation Completed.:-")
                print(f"{agents} image cords : X : {x} Y : {y}")
                print(f"Lock button cords : X : {xx} Y : {yy}")
                break
            else:
                print(f"Error 404: {agents} image not found.")
    else:
        print(f"Error 303: Agent '{agents}' is not available.")


def main():
    mode = select_mode()
    if mode == "1":
        auto_lock()
    elif mode == "2":
        check = pag.prompt(text="Check agents available", title="Checking agents...")
        if check.lower() in [agent.lower() for agent in Agents]:
            print(f"{check} is available :D")
            lock = pag.prompt(text=f"{check} is available :D\nWould you like to lock?\ny/n",
                              title="Agent Available!")
            if lock.lower() == "y":
                auto_lock()
            else:
                print("Nope")
                main()
        else:
            print(f"{check} : is not currently available :(")
            main()


if __name__ == "__main__":
    main()
