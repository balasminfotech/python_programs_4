import random

def guessNumber():
    num= random.randint(1,9)
    return num

print("Welcome to Number guessing  app!!!!")
chances=0

while 1:
    choice=input("Enter your choice  by typing (y/n):  ")
    if 'y' in choice.lower():
        print("Generating random number between 0 to 10")
        numb=guessNumber()

        while 1:
            chances+=1
            user_numer=int(input("Enter the number you think it is :  "))

            if user_numer>9 or user_numer < 0:
                print("Invalid number, please try again")
            else:
                if user_numer == numb:
                    print("Conguratulation !!! You got the number in {0} chances\n".format(chances))
                    chances = 0
                    break
                elif user_numer>numb :
                    print("You have entered a higher number")
                elif user_numer<numb:
                    print("You have entered a lower number")
    elif 'n' in choice.lower():
        print("exiting from Dice")
        break
    else:
        print("Pleas enter a valid choice")