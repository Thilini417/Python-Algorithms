import random

chance = 0

random_integer = random.randint(0, 10)

while chance <= 2:
    n = int(input("Guess the number between 1 to 10:"))
    
    if (n < 0 or n > 10):
        print("number out of range")
        chance+=1
        
    else:
         # Generate a random integer between 0 and 10 (inclusive)
        if (n == random_integer):
            print("You Win")
            break
            
        elif (n > random_integer):
            print("number guessed is greater than the lucky number")
            chance +=1
            
        elif (n < random_integer):
            print("number guessed is less than the lucky number")
            chance+=1

print("Lucky number was:",random_integer)