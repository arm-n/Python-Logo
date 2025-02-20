from turtle import Screen, Turtle

def curved_box(t, sides):
    """Draws a curved box for the snake logo."""
    for _ in range(sides):
        t.circle(90, extent=90)
        t.forward(120)
    t.circle(90, extent=90)

def snake(t, color):
    """Draws a snake-like curved shape."""
    t.backward(16)
    t.left(90)
    t.forward(16)
    t.right(90)

    t.fillcolor(color)
    t.pencolor("black")  # Outline color
    t.width(3)  # Outline thickness

    t.begin_fill()
    t.forward(64)
    curved_box(t, 2)
    t.forward(44)
    t.left(90)
    t.forward(152)
    t.right(90)
    t.forward(16)
    t.right(90)
    t.forward(204)
    curved_box(t, 1)
    t.forward(44)
    t.left(90)
    t.forward(60)
    t.circle(-90, extent=90)
    t.forward(64)
    t.end_fill()

    # Eye effect
    t.backward(86)
    t.left(90)
    t.forward(224)
    t.dot(48, 'white')  # Eye
    t.backward(224)
    t.right(90)
    t.forward(86)

def draw_background():
    """Creates a simple gradient-like background using multiple rectangles."""
    bg = Turtle()
    bg.hideturtle()
    screen.tracer(False)  # Disable updates for fast rendering
    bg.speed(0)

    colors = ["#1a1a1a", "#252525", "#303030", "#3a3a3a", "#444444"]
    y = 200

    for color in colors:
        bg.penup()
        bg.goto(-300, y)
        bg.pendown()
        bg.fillcolor(color)
        bg.begin_fill()
        for _ in range(2):
            bg.forward(600)
            bg.right(90)
            bg.forward(80)
            bg.right(90)
        bg.end_fill()
        y -= 80

    screen.tracer(True)  # Re-enable updates


# Screen setup
screen = Screen()
screen.bgcolor("#121212")  # Dark theme background
screen.setup(width=700, height=600)

# Draw background and logo
draw_background()
turtle = Turtle()
turtle.penup()
turtle.speed(3)
turtle.pensize(2)

# Draw two snake-like shapes
snake(turtle, '#3774A8')  # First shape
turtle.left(180)
snake(turtle, '#F6D646')  # Second shape


screen.exitonclick()
