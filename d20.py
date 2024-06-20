import random

def roll():
    number = random.randint(1,20)
    print("Dice roll =", number)
    return number

roll()
