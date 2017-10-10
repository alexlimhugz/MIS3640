import turtle

def drunkTurtle(n):
    for i in range(n):
        turtle.left(random.choice([0, 90, 180, 270]))
        turtle.forward(50)
    turtle.mainloop()