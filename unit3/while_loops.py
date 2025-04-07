import random

#tails = 0
#heads = 0
#while tails < 10:
#    coin_flip = random.randint(1,2)
#    
#    if coin_flip == 2:
#        tails = tails + 1
#    else: heads = heads + 1
        
#print (heads)
sumsum = 0
N = 10

Timesrolled = 0
while Timesrolled < 5:
    Rolls = 0
    while Rolls < N:
        Dice_roll1 = random.randint(1,6)
        Dice_roll2 = random.randint(1,6)
        sum = Dice_roll1 + Dice_roll2
        sumsum = sum + sumsum
        Rolls = Rolls + 1
    sumsum = sumsum /N
    print (sumsum)
    Timesrolled = Timesrolled + 1