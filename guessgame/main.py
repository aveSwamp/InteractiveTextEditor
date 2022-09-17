import random

attempts = 0
guessed_number = random.randint(1,1000)

users_variant = -100

while(guessed_number != users_variant):
    print("Please enter your variant: ", end = '')
    users_variant = int(input())
    if guessed_number < users_variant:
        print("Guessed number is less than yours variant")
    else:
        print("Guessed number is more than yours variant")
    attempts += 1
print("Well done!")
print("Attempts: {0}".format(attempts))