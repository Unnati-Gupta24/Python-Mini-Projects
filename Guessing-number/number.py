import random

var1 = random.randrange(10)

guess = int(input("enter number of guesses : "))

var2 = 0

while guess>0:
    var2 = int(input("input your guess: "))
    if var2 == var1:
        print("Congratulations you won")
        break
    guess = guess-1

print("the chosen number was: "+str(var1))

if guess==0:
    print("better luck next time")
