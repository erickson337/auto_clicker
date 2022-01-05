import pyautogui
import keyboard

running = True
click = False

try:
    while running:

        if keyboard.is_pressed('s'):
            running = False
        
        x, y = pyautogui.position()
        if click:
            pyautogui.click(x, y)
        
        
        if keyboard.is_pressed('p'):
            click = False
        
        if keyboard.is_pressed('c'):
            click = True

except KeyboardInterrupt:
    print('\n')