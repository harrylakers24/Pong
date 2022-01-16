from time import sleep
import turtle

playerAScore = 0
playerBScore = 0

# window setup
win = turtle.Screen()
win.title("first")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# creating left paddle
leftPaddle = turtle.Turtle()
leftPaddle.speed(0)
leftPaddle.shape("square")
leftPaddle.color("green")
leftPaddle.shapesize(stretch_wid=4, stretch_len=1)
leftPaddle.penup()
leftPaddle.goto(-350, 0)

# creating right paddle
rightPaddle = turtle.Turtle()
rightPaddle.speed(0)
rightPaddle.shape("square")
rightPaddle.color("red")
rightPaddle.shapesize(stretch_wid=4, stretch_len=1)
rightPaddle.penup()
rightPaddle.goto(350, 0)

# creating ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ballX = 1
ballY = 1


# move leftPaddle Down
def moveLeftDown():
    y_coor = leftPaddle.ycor()
    if y_coor >= -280:
        y_coor = y_coor - 20
    leftPaddle.sety(y_coor)


# move leftPaddle Up
def moveLeftUp():
    y_coor = leftPaddle.ycor()
    if y_coor <= 280:
        y_coor = y_coor + 20
    leftPaddle.sety(y_coor)


# move leftPaddle Down
def moveRightDown():
    y_coor = rightPaddle.ycor()
    if y_coor >= -280:
        y_coor = y_coor - 20
    rightPaddle.sety(y_coor)


# move leftPaddle Up
def moveRightUp():
    y_coor = rightPaddle.ycor()
    if y_coor <= 280:
        y_coor = y_coor + 20
    rightPaddle.sety(y_coor)


# Keyboard Binding
win.listen()
win.onkeypress(moveLeftUp, "w")
win.onkeypress(moveLeftDown, "s")
win.onkeypress(moveRightUp, "Up")
win.onkeypress(moveRightDown, "Down")

# scoreboard
sb = turtle.Turtle()
# animation speed
sb.speed(0)
sb.color("red")
sb.penup()
sb.hideturtle()
sb.goto(0, 260)
sb.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

# Game Loop

gameRun = True;


def collision(a, b):
    return abs(a.xcor() - b.xcor()) < 23 and abs(a.ycor() - b.ycor()) < 23


while gameRun:
    sleep(0.01)
    win.update()

    # ball movement
    ball.setx(ball.xcor() + ballX)
    ball.sety(ball.ycor() + ballY)

    if collision(ball, leftPaddle):
        ball.setx(-326)
        ballX = -(ballX - 0.5)

    if collision(ball, rightPaddle):
        ball.setx(326)
        ballX = -(ballX + 0.5)

    if ball.ycor() > 299:
        ballY = -ballY

    if ball.ycor() < -299:
        ballY = -ballY

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ballX = 2
        ballX = -1 * ballX
        playerAScore += 1
        sb.clear()
        sb.write("Player A: {} Player B: {}".format(playerAScore, playerBScore), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ballX = 2
        playerBScore += 1
        sb.clear()
        sb.write("Player A: {} Player B: {}".format(playerAScore, playerBScore), align="center", font=("Courier", 24, "normal"))
