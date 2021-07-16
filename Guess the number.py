def matching(x):
    y = False
    while y == False:
        guess = input("What is your guess? (3 numbers) ")

        if x[0] == int(guess[0]) and x[1] == int(guess[1]) and x[2] == int(guess[2]):
            return True
        elif x[0] == int(guess[0]) or x[1] == int(guess[1]) or x[2] == int(guess[2]):
            print('Match You ve guessed a correct number in the correct position')
        elif x[0] == int(guess[1]) or x[0] == int(guess[2]):
            print('Close You ve guessed a correct number but in the wrong position')
        elif x[1] == int(guess[0]) or x[1] == int(guess[2]):
            print('Close You ve guessed a correct number but in the wrong position')
        elif x[2] == int(guess[0]) or x[2] == int(guess[1]):
            print('Close You ve guessed a correct number but in the wrong position')
        else:
            print('Nope You haven t guess any of the numbers correctly')



import random
digits = list(range(10))
random.shuffle(digits)
x = digits[:3]


if (matching(x) == True):
    print('Congratualtions!!!')
