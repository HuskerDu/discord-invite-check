from random import randint
from random import choice


def create():
    b = 'http://discord.gg/'
    for i in range(7):
        a = [randint(48, 57), randint(65, 90), randint(97, 122)]
        b += chr(choice(a))  # generating possible invite link
    return b
