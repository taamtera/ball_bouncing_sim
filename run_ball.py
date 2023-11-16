import turtle
import ball

num_balls = int(input("Number of balls to simulate: "))
turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()
canvas_width = turtle.screensize()[0]
canvas_height = turtle.screensize()[1]
ball_radius = 0.05 * canvas_width
turtle.colormode(255)
balls = []
for i in range(num_balls):
    balls.append(ball.Ball(canvas_width, canvas_height, ball_radius))
while (True):
    turtle.clear()
    for i in balls:
        i.draw_circle()
        i.move_circle(canvas_width, canvas_height)
    turtle.update()

# hold the window; close it by clicking the window close 'x' mark
turtle.done()
