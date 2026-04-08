import time
import keyboard
import pyautogui



TARGET_COLOR = (59, 56, 63)

lines = [
    (722, 539),
    (876, 544),
    (1028, 540),
    (1190, 536)
]

while True:
   if keyboard.is_pressed('q'):
      print("Macro runs...")
      break
   else:
      time.sleep(0.1)
go = True
while go:
    for x, y in lines:
        pixel = pyautogui.pixel(x, y)


        if pixel == TARGET_COLOR:
            pyautogui.click(x, y)


    time.sleep(0.001)


    if keyboard.is_pressed('q'):
        go = False