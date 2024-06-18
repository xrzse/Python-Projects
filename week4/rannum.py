import random
while True:
    rannum = input("Do u want a randon number: ").lower()
    if rannum in ["yes", "y"]:
        print(random.choice(range(1,101)))
        continue
    elif rannum in ["no", "n"]:
        break
    else:
        continue



