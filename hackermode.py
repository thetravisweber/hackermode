from pynput import keyboard
from os import system
from hacklib import gen_string

clear = lambda: system('clear')

running = True

while (running):
    with keyboard.Events() as events:
        # Block for as much as possible
        event = events.get(1e6)
        print(gen_string())
        if event.key == keyboard.KeyCode.from_char('q'):
            running = False


clear()
input("Hack Complete")
