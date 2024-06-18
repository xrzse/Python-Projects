l = [1,2,3,4,5,"Hello World"]
z = 0
try:
    print(l[203])
except ValueError:
    print("No")
except TypeError:
    print("Nopt2")
except IndexError:
    print("Nopt3")


while True:
    intz = input("Gimme a int: ")
    try:
        int(intz)
        print("Thanks")
        break
    except ValueError:
        continue
        