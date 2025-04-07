import random
#for i in range(1,21,):
#    print ("i = ", i,"Hello"*i)

#print ("The end.")


need_nectar = 20000
has_nectar = 0
nectar_deposit = 0


for hour in range (7 *18):

    dropoff = random.randint(
        has_nectar // 4,
        3*has_nectar //4

    )

    pickups = random.randint(
        need_nectar // 4,
        3* need_nectar // 4
    )

    has_nectar = has_nectar + pickups
    need_nectar = need_nectar - pickups
    has_nectar = has_nectar - dropoff
    need_nectar = need_nectar + dropoff 
    nectar_deposit = nectar_deposit + dropoff
    print(str(has_nectar) + (" (has)"))
    print(str(need_nectar) + (" (needs)"))
honey = round(nectar_deposit // 90)
print ("The total honey produced was "+ str(honey)+(" grams of honey.") )
