import random

N = input("How many flips would you like? : ")
N = int(N)


numheads = 0

#roll = random.randint(1,6)
#print(roll)

for _ in range(N):
    flip_int = random.randint(1,100)
    if flip_int <= 30:
        numheads = numheads + 1

print (numheads / N * N)


 






