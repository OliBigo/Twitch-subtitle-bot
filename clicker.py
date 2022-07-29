from os import name
import win32api
import win32con
import time
import keyboard


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def main():
    refreshed = False
    while(True):
        f = open("status.txt", "r")
        if (f.read() == "true"):
            f.close()
            if (refreshed == False):
                click(500, 400)
                keyboard.press_and_release("f5")
                refreshed = True
                time.sleep(0.3)
                click(1110, 740)
                time.sleep(0.3)
                click(1110, 740)
                time.sleep(1.5)
                click(1275, 525)
                time.sleep(1)
                click(1325, 100)
                time.sleep(0.3)
                click(1110, 740)
            time.sleep(30)
            click(930, 23)
            time.sleep(0.3)
            click(730, 495)
            time.sleep(0.3)
            click(1110, 400)
            time.sleep(0.3)
            keyboard.press_and_release("ctrl+a")
            time.sleep(0.3)
            keyboard.press_and_release("backspace")
            time.sleep(0.3)
            click(1110, 740)
        else:
            f.close()
            if (refreshed == True):
                click(1110, 400)
                time.sleep(0.3)
                keyboard.press_and_release("ctrl+a")
                time.sleep(0.3)
                keyboard.press_and_release("backspace")
                time.sleep(0.3)
                click(930, 23)
                time.sleep(0.3)
                click(730, 495)
                time.sleep(0.3)
                click(1500, 10)
            refreshed = False
            time.sleep(30)


if __name__ == '__main__':
    main()
