


"""
import pyfirmata
import time

breadboard = pyfirmata.Arduino('COM4')

while True:
    breadboard.digital[5].write(1)
    time.sleep(1)
    breadboard.digital[5].write(0)
    time.sleep(1)
"""



"""
from plyer import notification

notification.notify(
    title = "Jarvis",
    message = "Sono intelligentissimo",
    app_icon = None,
    timeout = 5,
)


data = {

    "Cartenon": {

    }

}

from pynput.keyboard import Key, Controller
import keyboard

from pynput import keyboard

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


keyboard = Controller()

time.sleep(2)
for i in range(10):
    keyboard.type("Hey\n")
"""