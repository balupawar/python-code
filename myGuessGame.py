i = 5
n = 6
for attempt in range(n):
    guess = int(input("enter a guess number:\n"))

    if guess == i:
        print("Your choose number is correct")
        print("you WON")
        break

    elif guess < i:
         print("your entered number is lesser")

    elif guess > i:
         print("your Entered nubmer is Greater")

    elif attempt != n:
        print("your life 0")
        print("try again")
        break
        exit()
    else:
        print("try again")
#this programme is currectly run and zero error and its absulutly i am created
#BALU PAWAR
