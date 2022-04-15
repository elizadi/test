import random

def tails_hands():
    return(round(random.random()))

throw = input('enter the number of throw: ')
throw = int(throw)

count = 0
while count < throw:
    print(tails_hands())
    count += 1