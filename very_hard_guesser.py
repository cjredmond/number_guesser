import random
answer = int(input("Pick a number between 1 and 100:    "))
while answer >= 101:
    print("You need to chose a number between 1 and 100")
    answer = int(input("Pick a number between 1 and 100:    "))

print("good number")
count = -1
win = False
while count < 7:
    count = count + 1
    comp_guess = random.randint(1,100)
    print(comp_guess)
    if comp_guess == answer:
        print("Computer Wins!")
    elif comp_guess < answer:
        print("Too Low")
    else:
        print("Too High")
