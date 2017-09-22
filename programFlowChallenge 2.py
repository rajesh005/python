import random
answer = random.randint(1,10)



print("guess the number b/w 1 to 10")
guess=0
while (guess!=answer):
    guess=int(input())
    if(guess ==0):
        break
    elif(guess > answer):
            print("please guess something lower" )
    elif(guess < answer):
            print("Please guess something higher")

    else:
        print("Wow. you guessed it")

if guess == 0:
    print("Better luck next time")


