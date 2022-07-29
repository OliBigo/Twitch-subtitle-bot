from os import name
import win32api
import win32con
import time
import keyboard

# Unfortunately I had to use an auto clicker since good speech to text api's like Google's are quite expensive.
# Instead what I did is use the integrated speech to text button in Microsoft Word.
# The position values are all hard coded, so if you wish to make your own, you will need to find the values for yourself.
# For this to work you will also need to set you Word to automatically save as a .txt file and make Word the default app to open .txt files.


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
                click(500, 400)  # Click on the web browser
                keyboard.press_and_release("f5")  # Refresh the stream page
                refreshed = True
                time.sleep(0.3)
                # Double click on the .txt file on the desktop to open it in Word
                click(1110, 740)
                time.sleep(0.3)
                click(1110, 740)
                time.sleep(1.5)
                click(1275, 525)  # Focus on the Word window
                time.sleep(1)
                click(1325, 100)  # Start speech to text
            time.sleep(30)
            keyboard.press_and_release("ctrl+s")
            time.sleep(0.3)
            click(730, 495)  # Click on the pop up
            time.sleep(0.3)
            keyboard.press_and_release("ctrl+a")
            time.sleep(0.3)
            keyboard.press_and_release("backspace")
            time.sleep(0.3)
            click(1370, 200)  # Restart speech to text
        else:
            f.close()
            if (refreshed == True):
                click(1275, 525)  # Focus on the Word window
                time.sleep(0.3)
                keyboard.press_and_release("ctrl+a")
                time.sleep(0.3)
                keyboard.press_and_release("backspace")
                time.sleep(0.3)
                keyboard.press_and_release("ctrl+s")
                time.sleep(0.3)
                click(730, 495)  # Click on the pop up
                time.sleep(0.3)
                click(1500, 10)  # Close Word
            refreshed = False
            time.sleep(30)


if __name__ == '__main__':
    main()
