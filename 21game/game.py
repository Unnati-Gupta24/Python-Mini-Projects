import random

print("welcome to 21 game let's play your chance first")

count = 21
c = 0

while count>0:
    you = int(input("choose count: "))
    count = count-you
    if count<=3:
        c = c+1
        print("you won")
        break
    computer = random.randrange(3)
    print("comp choose "+str(computer))
    count = count-computer

if c==0:
    print("you loose")
