import turtle


def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_snowflake(order, size=600):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, 180)
    t.pendown()

    for _ in range(3):
        koch_snowflake(t, order, size)
        t.right(120)

    window.mainloop()

recursion_level = int(input("Enter the level of recursion: "))

draw_koch_snowflake(recursion_level)
