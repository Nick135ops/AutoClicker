import mouse
import keyboard
# WARNING: THIS CLICKER MAY AFFECT YOUR PERFORMANCE ITS BETTER TO TERMINATE ONCE YOU ARE DONE
# TO TERMINATE THIS PROGRAM CLICK 'q' ON YOUR KEYBOARD
hotkey = 'q'
while 1:
    if keyboard.is_pressed(hotkey=hotkey):
        print('Program terminated with the hotkey {}'.format(hotkey))
        break
    else:
        mouse.click()
