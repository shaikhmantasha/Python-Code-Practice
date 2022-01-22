#-----------------------------------------------PROJECT------------------------------------------------------------------------------------
import random

randNumber = random.randint(1 , 100)
# print(randNumber)
userGuess = None
guesses = 0

while (userGuess != randNumber):    # jab tak user aur randnumber equal nahi hotey tab tk loop chalega
    userGuess = int(input("Enter your Guess : "))  
    guesses += 1         #jaise jaise guess karte jaogey waise waise guess ka count badhte jayega  
    if (userGuess == randNumber):
        print("You Guessed it Right!")
    else:
        if (userGuess > randNumber):
            print("you've guessed it wrong! enter a smaller number")
        else:
            print("you've guessed it wrong! enter a larger number")

print(f"you guessed the number in {guesses} guesses")

#if you want your highscore to be shown somehwhere you  can make a .txt file

# with open(highscore.txt , "r") as f:
#     hiscore = int(f.read)
# with open (hiscore.txt , "w") as f:
#     f.write(guesses)