def calc_daily_pay(hours,rank,rate):
    if hours > 7 and rank == "permanent":
        hoursextra = hours - 7
        dayspay = (7*rate) + (hoursextra*(rate*2))
        print(dayspay)
        return dayspay

    elif hours > 8 and rank != "permanent":
        hoursextra = hours - 7
        dayspay = (7*rate) + (hoursextra*(rate*1.5))
        print(dayspay)
        return dayspay
    
    else:
        dayspay = hours*rate
        print(dayspay)
        return dayspay
    
calc_daily_pay(9,"permanent",20)
    

