import random

secret_number = random.randint(1,100)
while True:
    User_Attempt = int(input("Adivine el numero del 1 al 100:"))
    if User_Attempt < secret_number:
        print("El numero es muy bajo")
    elif User_Attempt > secret_number : 
        print("El numero es muy alto")
    else:
        print("Es corecto")
        break