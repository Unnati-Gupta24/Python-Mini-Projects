import random

someWords = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(' ')
word = random.choice(someWords)

print(someWords)

guess = len(word)+1

while guess!=0:
    var1 = input("choose a word: ")
    if var1==word:
        print("Congo you won")
        break
    guess = guess-1

if guess==0:
    print("better luck next time")
