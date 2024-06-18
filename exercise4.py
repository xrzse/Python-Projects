import turtle

amt = int(input("How many squares?: "))
turtle.setup(500,500)
screen = turtle.Screen()
screen.title("Assignment 1")
jeff = turtle.Turtle()
jeff.speed(0)

def pretty_pattern(amt):
    for _ in range(amt):
        for x in range(4):
            jeff.forward(50)
            jeff.left(90)

        jeff.left(360/amt)
    
    turtle.done()

pretty_pattern(amt)


