from os import system
from hacklib import gen_string
from random import random
from time import sleep

clear = lambda: system('clear')

running = True

clear()

while (running):
    print(gen_string())
    sleep(random()/5)
