import time
import keyboard
import pyautogui
import win32api
import win32con

time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#Color of center: (255, 219, 195)

while keyboard.is_pressed('q') == False:

    pic = pyautogui.screenshot(region=(1200,130,10,12))

    width, height = pic.size
#RBG : 75, 219, 106 , X:  772 Y:  356
    for x in range(0,10,5):
        for y in range(0,12,5):

            r,g,b = pic.getpixel((x,y))

            if b == 106:
                click(x+1200,y+130)
                click(x+1200,y+130)
                click(x+1200,y+130)
                click(x+1200,y+130)
                click(x+1200,y+130)
                break
