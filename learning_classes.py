import turtle


def draw_square(some_turtle):
    for i in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    # Create the turtle dan
    dan = turtle.Turtle()
    dan.shape("turtle")
    dan.color("yellow")
    dan.speed(10)
    for i in range(1, 36):
        draw_square(dan)
        dan.right(10)

    # songyi = turtle.Turtle()
    # songyi.shape("arrow")
    # songyi.color("blue")
    # songyi.circle(100)
    # window.exitonclick()


draw_art()
