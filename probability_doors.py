#!/usr/bin/env python

from random import randint

#
# You have 3 doors, one of them with a prize
# you choose one of then but then someone says 
# the door (that you didn't choose") that doesn't
# have the prize. And asks if you want to rechoose.
#
# Q: What is the chance of getting the prize if you
# rechoose?
#
# A: 2/3
#

def main():
    correct = 0
    total = 10000000
    for x in range(total):
        if chooseDoor():
            correct += 1
    print(correct/total)

def chooseDoor():
    doors = [0 for x in range(3)]
    correct_door = randint(0, 2)
    doors[correct_door] = 1
    doors[randint(0, 2)] -= 1
    return bool(doors[correct_door])

if __name__ == '__main__':
    main()
