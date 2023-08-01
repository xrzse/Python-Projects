size = input("Enter the file size remaining to be downloaded in GB: ")
speed = input("How many MB/s are you averaging?: ")

sizeMB = int(size) * 1000 #Converts GB to MB
timesec = sizeMB/int(speed) #Calculates how many seconds it will take
timemin = timesec/60 #Calculates how many minutes
timehour = timemin/60 #Calculates how many hours

print("It will take "+str(timesec)+ " seconds, " +str(timemin)+ " minutes, "+ str(timehour) +" hours to download.")

