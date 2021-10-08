import random
randomNum = random.randint(1,9)
chances = 5

while (chances > 0):
    chances = chances-1
    guess = int(input("Enter Yor Guess : "))
    if (guess == randomNum):
        print ('Congrats you won!!')
        break
    elif (guess > randomNum):
        print ('Think of smaller number')
    else : 
        print ('Think of greater number')