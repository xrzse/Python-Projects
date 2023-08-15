current_time = input("What time is it? (eg., 8:25 PM): ").lower()
future_time = input("What is your target time? (eg., 7:23 AM): ").lower()

def calc(current_hour, current_minute, current_period, future_hour, future_minute, future_period):
    if current_period == future_period and future_hour == 12 and current_hour != 12:
        hours_left = 24 - current_hour
    elif current_period == future_period and current_hour == 12 and future_hour != 12:
        hours_left = future_hour
    elif current_period == future_period and future_hour > current_hour:
        hours_left = future_hour - current_hour
    elif current_period == future_period and current_hour > future_hour:
        hours_left = future_hour + 24 - current_hour
    elif current_period != future_period:
        hours_left = 12 - current_hour + future_hour
    elif current_hour == future_hour and current_period == future_period:
        hours_left = 0
        
    if future_minute >= current_minute:
        minutes_left = future_minute - current_minute
    elif future_minute < current_minute:
        hours_left -= 1
        minutes_left = 60 - current_minute + future_minute
    
    print(str(hours_left) + " hours and " + str(minutes_left) + " minutes left")

# Defining current time variables
splittime = current_time.split(":")
current_hour = int(splittime[0])
current_minute, current_period = splittime[1].split()
current_minute = int(current_minute)

# Defining future time variables
splittime_future = future_time.split(":")
future_hour = int(splittime_future[0])
future_minute, future_period = splittime_future[1].split()
future_minute = int(future_minute)
        
calc(current_hour, current_minute, current_period, future_hour, future_minute, future_period)