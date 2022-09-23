from secrets import choice
from unicodedata import name

print("Are you lucky or unlucky?")
from random import randint
choice == randint(1,10)

if choice == 7:
    print("lucky")
else:
    print("unlucky")
