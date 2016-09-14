import random
answer = int(input("Pick a number between 1 and 100:    "))
while answer >= 101:
    print("You need to chose a number between 1 and 100")
    answer = int(input("Pick a number between 1 and 100:    "))

print("You chose a valid number")
count = -1
min_guess = 1
max_guess = 100

while count < 7:

    comp_guess = int((min_guess + max_guess) / 2)
    print(comp_guess)


    if comp_guess == answer:
        print("Computer Wins!")
        break
    elif comp_guess < answer:
        print("Too Low")
        min_guess = (comp_guess + 1)
        count = count + 1
    else:
        print(comp_guess)
        print("Too High")
        max_guess = (comp_guess -1)
        count = count + 1
