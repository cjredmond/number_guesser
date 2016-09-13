import random
answer = random.randint(1,100)
print(answer)
count = -1

while count < 5:
    count = count + 1
    print("You used %o of 5 guesses" % count)
    if count < 5:
        guess = int(input("What is your guess? (between 1 and 100)"))
    else:
        print("Sorry, you lose")
    if guess == answer:
        print("YOU WIN")
    elif guess < (answer + 3) and guess > (answer - 3):
        print("You are within 3 numbers of the answer")
    elif guess > answer:
        print("Too High")
    else:
        print("Too Low")

#function?
#return?
#count placeholder?
