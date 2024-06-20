import turtle

window = turtle.Screen()
window.screensize(800, 600)
turtle.speed('fastest')
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.left(90)

turtle_angle = 30

def branch(size, level):
  if level <= 0:
    return
  turtle.colormode(255)

  turtle.pencolor(0, 255 // level, 0)
  turtle.forward(size)
  turtle.right(turtle_angle)

  branch(0.8 * size, level - 1)
  turtle.pencolor(0, 255 // level, 0)
  turtle.pencolor(0, 255 // level, 0)
  turtle.left(2 * turtle_angle)

  branch(0.8 * size, level - 1)
  turtle.pencolor(0, 255 // level, 0)
  turtle.right(turtle_angle)

  turtle.forward(-size)

branch(80,8)

turtle.mainloop()
