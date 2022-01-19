from pygame import mixer
import time

mixer.init() #Initialzing pyamge mixer
mixer.music.load('giornos-theme-kaiya-remix.mp3') #Loading Music File

#Timer based
mixer.music.play() #Playing Music with Pygame
time.sleep(5)
print("________________________________________________________________________________________ |")                    
print("| From: Jabbari: Welcome to my adventure. This game is base off of Jabbari Jumps.       |")
print("| I need you to help me slove these problems. With each proeblem solved you wil.        |")
print("|get one letter Once you get all Letters you will you will see what my favorite food is.|")
print("|______________________________________________________________________________________ |")
print()

print("What 2 numbers add up to his favorite number. Jabbari's favorite  number is 5.")
number1 = int(input("Please enter a number: "))
number2 = int(input("Please enter a number: "))
print (number1)
print (number2)
result = number2 + number1
print(result)
while True:
    if result > 5: 
        print("Your answer is too high try again") 
        number3 = int(input("Please enter a number: "))
        number4 = int(input("Please enter a number: "))
        print (number3)
        print (number4)
        result = number3 + number4
        print(result)
    elif result == 5:
        print("You got the correct answer great job! The first letter in this code is C. Now that you have gotten the first letter it is time to move onto the second challange")  
        break
    else:
        print("Your answer is too low try again")
        number3 = int(input("Please enter a number: "))
        number4 = int(input("Please enter a number: "))
        print (number3)
        print (number4)
        result = number3 + number4
        print(result)
print("Jabbari visits a farm. He has to count how many legs 2 cows have and 3 chickens. ")
number1 = int(input("Please enter a number: "))
print (number1)
result = number1
print(result)
while True:
    if result > 14: 
        print("Your answer is too high try again") 
        number1 = int(input("Please enter a number: "))
        print (number1)
        result = 0  + number1
        print(result)
    elif result == 14:
        print("______________________________________________________________________________|")                    
        print("| From: Jabbari: You got the correct answer great Job! The second letter  in  |")
        print("| this code is a h. Time to move onto the third challange.                    |")
        print("|____________________________________________________________________________ |")
        break
    else:
        print("Your answer is too low try again")
        number1 = int(input("Please enter a number: "))
        print(number1)
        result =  0 + number1
        print(result)
print("______________________________________________________________________________|")                    
print("| From: Jabbari: Thanks for helping! Now can yout tell me which animals has more |")
print("|  legs 3 chickens or 2 Cows.                                                |")
print("|                                                                             |")
print("|____________________________________________________________________________ |")
print()
print("A): 3 Chickens ")
print("B): 2 Cows")
print()
while True:
    Answer = input("Input your answer here: ")
    if Answer in ('B', '2 Cows','c'): 
       print('Great Job! The third word in the code is e. Time to move onwards. ')
       break
    else:
        print("Oops Try Again?")
        Answer =  int(input("Input answer here"))
        continue
import random

number = random.randint(1,100)
guess = int(input("Guess the marbles from 1 to 100: "))

while guess != number:
    if guess > number:
        print ("Incorrect.  Your guess is too high.")
    else:
        print ("Incorrect.  Your guess is too low.")
    guess = int(input("Guess the marbles from  1 to 100: "))

    print("__________________________________________________________________________|")                    
print("|   From: Jabbari:  Great Job! You guessed the correct amount of marbles. The |")
print("| next letter in the code is e. Get ready for the next level where you will   |")
print("| guess the amount of corn on the table  Goof Luck! :)                        |")
print("|____________________________________________________________________________ |")
import random

number = random.randint(1,100)
guess = int(input("Guess the corn from 1 to 100: "))

while guess != number:
    if guess > number:
        print ("Incorrect.  Your guess is too high.")
    else:
        print ("Incorrect.  Your guess is too low.")
    guess = int(input("Guess the corn from  1 to 100: "))
  
print("__________________________________________________________________________   |")                    
print("|   From: Jabbari: Good Job the next letter is s. Anyways I need you to help |")
print("|  escape this corn maze.  I'm realy scared down here and you're the only   |")
print("|   one that can help me,|will you do it?                                    |")
print("|____________________________________________________________________________|")
print ("Help Jabbari by reading the sign and input it into the text box.")              
print("__________________________________________________________________________|")                    
print("|    |            ________              _________            _______      |")          
print("|    |            |                     |                       |         |")     
print("|    |            |                     |                       |         |")
print("|    |            |                     |                       |         |")
print("|    |            |                     |                       |         |")
print("|    |            |_______              |________               |         |")
print("|    |            |                     |                       |         |")
print("|    |            |                     |                       |         |")
print("|    |            |                     |                       |         |")
print("|    |______      |__________           |                       |         |")
print("|_________________________________________________________________________|")
while True:
    command = input("Type a direction to move. \nValid directions are left, right, Up and Down. ")
    if "left" in command.lower():
        print ("You have the correct one. Time to Move onto the next one.")
        break
    elif "Right" in command.lower():
        print ("You have moved right. Incorrect")

    elif "Up" in command.lower():
        print ("You have moved up. Incorrect")

    elif "Down" in command.lower():
        print ("You have moved down. Incorrect")

    else:
        print ("I don't recognize that direction.")
print("__________________________________________________________________________|")                    
print("|   From: Jabbari:  Great Job! You did it. The final letter is e. What word   |")
print("|    does that make?                                                           |")
print("|                                                                             |")
print("__________________________________________________________________________   |")     
while True:
    command = input("Type the food. \nValid Foods are bacon,salad,and cheese. ")
    if "cheese" in command.lower():
        print ("You have won the game.")
        validInput = True
        break
    elif "bacon" in command.lower():
        print ("Incorrect try again.")
        validInput = True
        continue
    elif "salad" in command.lower():
        print ("Incorrect try again.")
        validInput = True
        continue
print("_____________________________________________________________________________ |")                    
print("|   From: Jabbari:  Great Job! You did it. You completed all the challanges   |")
print("|    and figuered out what my favorite food was. I know it may have seemed    |")
print("|      challenging but thanks for playing and helping me with my adventure.   |")   
print("| Enter Y to stop music                                                        |")                               
print("|_____________________________________________________________________________ |")   
mixer.music.stop()
mixer.music.play()
answer = input("Enter y ")
while 'y' not in answer:
    print ("Sorry, incorrect")
    answer = input('Enter y to stop ')
mixer.music.stop()


    