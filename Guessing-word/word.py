import random

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

print("welcome to word guessing game")
print(words)

var1 = random.choice(words)

guess = int(input("enter the number of guesses: "))

while guess!=0:
    word = input("choose the word: ")
    if word==var1:
        print("Congo you won")
        break
    guess = guess-1

if guess==0:
    print("better luck next time")
