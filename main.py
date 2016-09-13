import random
answer = random.randint(1,100)


count = -1

while count < 5:
    count = count + 1
    
    print("You used %o of 5 guesses" % count)
    if count < 5:
        guess = int(input("What is your guess? (between 1 and 100)    "))
    else:
        print("Sorry, you lose, the answer was %s" % answer)
    if guess == answer:
        print("YOU WIN, the answer was:  %s  " % answer)
        break
    elif guess > answer:
        print("Too High")
        if guess < (answer + 3):
            print("You are within 3 numbers of the answer")
    else:
        print("Too Low")
        if guess > (answer - 3):
            print("You are within 3 numbers of the answer")


#function?
#return?
#count placeholder?
