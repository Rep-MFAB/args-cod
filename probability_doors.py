from random import randint

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
