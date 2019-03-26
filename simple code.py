import random
ad_1 = str(input("What is your name:?\t"))
ad_2 =str(input("What is your surname:? \t"))
print("Welcome %s %s in the game, which is baesd on guessing a number, which was randomized by generator. \n lET STARTS!!"%(ad_1,ad_2))

los= random.randint(1,100)
count = 0
strike = None



while (strike != los):
    count+=1
    strike = int(input("Guess a numer %s, it's your  %d attempt: \t"%(ad_1,count)))
    if  (strike > los ):
        print("The number which you enter is to big, try again!\n")
    elif (strike < los):
        print("The number which you enter is to small, try again!!\n")
    else:
        print("Excellent %s, you managed to guess the number for %d times!!!"%(ad_1,count))
