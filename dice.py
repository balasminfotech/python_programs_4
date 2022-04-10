import random

print(random.randint(1,9))
def diceRoll():
    num= random.randint(1,9)
    return num
print("Welcome to dice roll app!!!!")
while 1:
    choice=input("Enter your choice  by typing (y/n):  ")
    print(choice)
    if 'y' in choice.lower():
        dicenumber=diceRoll()
        print("Dice number is : ",dicenumber)
    elif 'n' in choice.lower():
        print("exiting from Dice")
        break
    else:
        print("Pleas enter a valid choice")