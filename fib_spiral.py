import turtle
import math

x = turtle.Turtle()

def fib_plot(n):
    a = 0
    b = 1
    square_a = a
    square_b = b

    x.pencolor("blue")

    #draw first square
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)

    #proceeding in Fibonacci series
    temp = square_b
    square_b = square_b + square_a
    square_a = temp

    #draw the rest of the squares
    for i in range(1, n):
        x.backward(square_a * factor)
        x.right(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)

        #proceeding in Fibonacci series
        temp = square_b
        square_b = square_b + square_a
        square_a = temp

    #bring pen to starting point of spiral plot
    x.penup()
    x.setposition(factor, 0)
    x.seth(0)
    x.pendown()

    #set color of plotting pen
    x.pencolor("pink")

    #Fibonacci spiral plot
    x.left(90)
    for i in range(n):
        print(b)
        fdwd = math.pi * b * factor / 2
        fdwd /= 90
        for j in range(90):
            x.forward(fdwd)
            x.left(1)
        temp = a
        a = b
        b = temp + b

factor = 1
n = int(input("Enter number of iterations (n > 1): "))
if n > 0:
    print("Fibonacci series for ", n, " elements: ")
    x.speed(100)
    fib_plot(n)
    turtle.done()
else:
    print("Number of iterations must be > 0")
