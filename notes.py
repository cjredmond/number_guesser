import random

print(random.randint(1,20))

connors_age = int(input("How old are you?"))
shanes_age = 10

# Boolean

print(connors_age < shanes_age)

if connors_age > shanes_age:
    print('Connor is older than Shane')
elif connors_age == shanes_age:
    print('Same age')
else:
    print('Connor is not older than Shane')
