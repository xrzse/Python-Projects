def game_of_chance():
    
    from random import random
    from time import time
    dice = (1, 2, 3, 4, 5, 6) # Each outcome of roll
    spin = (1, 2, 3, 4, 5, 6, 7, 8) # Each outcome of spin
    import random
    dicex = str(random.choice(dice)) # Random outcome from all the outcomes(dice)
    spinx = str(random.choice(spin)) # Random outcome from all the outcomes(spinner)

    dicy = float(dicex)
    spiy = float(spinx)

    def bye2():       
        print("Thank you for playing!") 
        time.sleep(2)                     
        play_again = input("\nDo you wish to play 'Game of Chance' again? ").lower()
        if play_again == "yes" or play_again == "ya" or play_again == "sure" or play_again == "yea":
            game_of_chance()
        else:
            print("Closing Game...")
            time.sleep(3)
            import sys
            sys.exit("Goodbye")

    def simulate():
        z2 = float(10000)
        t = []
        while len(t) < z2:
            import random
            dicex = str(random.choice(dice)) # Random outcome from all the outcomes(dice)
            spinx = str(random.choice(spin)) # Random outcome from all the outcomes(spinner)

            dicy = int(dicex)
            spiy = int(spinx)
            x = dicy + spiy

            if dicy == 6 and spiy == 6:
                x1 = 50
                t.append(int(x1)) 
            elif x == 1 or x == 3 or x == 5 or x == 7 or x == 9 or x == 11 or x == 13:
                x2 = x * 2
                t.append(int(x2)) 
            elif dicy == spiy:
                x3 = 0
                t.append(int(x3))
            else:
                x4 = x / 2
                t.append(int(x4))
                    
        else:
            print("\nThe Results Are In!")
            time.sleep(1)
            ask = input("Do you wish to see all of 10,000 outcomes?: ")
            if ask == "yes" or ask == "ya" or ask == "sure" or ask == "yea":
                time.sleep(1)
                print(t)
                x21 = sum(t)
                avg = x21 / z2
                time.sleep(1)
                print ("\nAnd the expected value from 10,000 simulations is: " + str(avg))
                sim2 = input("Do you wish to simulate again?: ")
                if sim2 =="yes" or sim2 == "ya" or sim2 == "sure" or sim2 == "yea":
                    simulate()
                elif sim2 == 'no':
                    bye2()
            else:
                x21 = sum(t)
                avg = x21 / z2
                time.sleep(1)
                print ("\nVery well, the expected value from 10,000 simulations is: " + str(avg))
                time.sleep(1)
                sim3 = input("Do you wish to simulate again?: ")
                if sim3 =="yes" or sim3 == "ya" or sim3 == "sure" or sim3 == "yea":
                    simulate()
                elif sim3 == 'no':
                    bye2()

    def bye():   
        import time                          
        print("Closing Game...")
        time.sleep(2)
        print("Goodbye")
        time.sleep(3)

    def start():
        print("Alrighty then, lets roll the dice!")
        time.sleep(1)
        print("Rolling...")
        time.sleep(2)
        import random
        print("The number you have rolled is: " + dicex)
        time.sleep(1)
        print("Now lets spin the spinner!")
        time.sleep(2)
        print("Spinning...")
        time.sleep(1)
        print("The number you have spun is: " + spinx)
        time.sleep(1)
        sum = dicy + spiy
        if dicy == 6 and spiy == 6: #Lottery
                print("\nCongratulations! \nYou rolled a 6 and spun a 6!\nYou have won the lottery of $50!!!")
                time.sleep(2)
                def lottery1():
                    lottery = input("\nAccept your lottery of $50 by typing 'Accept': " ).lower()
                    if lottery == "accept":
                        bye2()
                    else:
                        lottery1()
                lottery1()

        elif sum == 1 or sum == 3 or sum == 5 or sum == 7 or sum == 9 or sum == 11 or sum == 13: #Odd
            sum2 = sum * 2
            print("The sum of the two is " + str(sum) +"...")
            time.sleep(1.5)
            print("\nThe sum is odd!\n\nCongratulations your winnings have doubled and are now: " + str(sum2))
            time.sleep(1.5)
            def odd1():
                odd = input("\nAccept your cash winnings of $" + str(sum2) + " by typing 'Accept': " ).lower()
                if odd == "accept":
                    bye2()
                else:
                    odd1()
            odd1()

        elif dicy == 1 and spiy == 1: #Doubles
            print("\nUnfortunate!\nYou got doubles!\nBetter luck next time!")
            time.sleep(2)
            bye2()
        elif dicy == 2 and spiy == 2:
            print("\nUnfortunate!\nYou got doubles!\nBetter luck next time!")
            time.sleep(2)
            bye2()
        elif dicy == 3 and spiy == 3:
            print("\nUnfortunate!\nYou got doubles!\nBetter luck next time!")
            time.sleep(2)
            bye2()
        elif dicy == 4 and spiy == 4:
            print("\nUnfortunate!\nYou got doubles!\nBetter luck next time!")
            time.sleep(2)
            bye2()
        elif dicy == 5 and spiy == 5:
            print("\nUnfortunate!\nYou got doubles!\nBetter luck next time!")
            time.sleep(2)
            bye2()
        else:
            sum3 = sum / 2
            print("The sum of the two is " + str(sum) +"...")
            time.sleep(1.5)
            print("\nThe sum is even!\n\nYour winnings have halfed and are now " + str(sum3))
            time.sleep(1.5)
            def even1():
                even = input("\nAccept your cash winnings of $" + str(sum3) + " by typing 'Accept': " ).lower()
                if even == "accept":
                    bye2()
                else:
                    even1()
            even1()            

    def rules1():
        rules = input("\nDo you wish to know the rules of the game? ").lower()
        if rules == "yes" or rules == "yea" or rules == "yep":
            time.sleep(1)
            print("\nYou will roll the dice and spin the spinner")
            time.sleep(3)
            print("The sum will be taken of both outcomes")
            time.sleep(3)
            print("If the sum is even you get half of the sum, if the sum is odd you get double the sum")
            time.sleep(4)
            print("If you roll doubles then you get nothing")
            time.sleep(3)
            print("However...")
            time.sleep(2)
            print("If you roll a 6 and spin a 6 then you win the lottery of $50!!")
            time.sleep(2)
            def rdy():
                game1 = input("Are you ready to start?: ").lower()
                if game1 == "yes" or game1 == "ya" or game1 == "start" or game1 == "yea":
                    start()
                else:
                    rdy()
            rdy()

        elif rules == "no" or rules == "nope" or rules == "na":
            start()
        else:
            rules1()

    def paywall():
        pay = input("The fee of this game is $13.25, type '13.25' to pay or type 'goodbye' to leave game: ").lower()
        if pay == "13.25":
            time.sleep(1)
            rules1()
        elif pay == "goodbye":
            bye()
        elif float(pay) > 13.25:
            time.sleep(0.5)
            print("Please pay the correct amount of 9.35, not higher because I do not have change.")
            time.sleep(0.5)
            paywall()
        elif float(pay) < 13.25:
            x = 13.25 - float(pay)
            time.sleep(0.5)
            print("That is not enough please pay " + str(x) + " more.")
            time.sleep(0.5)
            paywall()
        else:
            paywall()

    # The code below is the introduction piece
    Welcome = input("Welcome to the Game of Chance, type 'Start' to begin or type 'Simulate' to simulate 10,000 plays!: ").lower()
    if Welcome == "start":
        print("Loading...")
        import time
        time.sleep(2)
        paywall()
    elif Welcome == "simulate":
        print("Loading...")
        import time
        time.sleep(2)
        simulate()
    else:
        def Welcome1():
            wlcm = input("Welcome to the Game of Chance, type 'Start' to begin or type 'Simulate' to simulate 10,000 plays!: ").lower()
            if wlcm == "start":
                print("Loading...")
                import time
                time.sleep(2)
                paywall()
            elif wlcm == "simulate":
                simulate()
            else:
                Welcome1()
        Welcome1()

game_of_chance()