import time

password = int(input("Enter your 4 digit numeric password: "))
start = 0
for x in range(9999):
    start = start + 1
    print("Attempt: " + str(start))
    if start == password:
        print("The password is " + str(start))
        time.sleep(10)

