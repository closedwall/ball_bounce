import turtle
import random

#screen 
wn = turtle.Screen()
wn.bgcolor("blue")
wn.setup(width=600, height=500)
wn.tracer(0)

wn.title("Ball Bounce")

#lines
lines = []
line_pos=[-100,-50,0,50,100,150,200,250]
for val in line_pos:
    line = turtle.Turtle()
    line.shape("square")
    if val==250:
        line.shapesize(stretch_wid=wn.window_height(),stretch_len=.3)
        # line.shapesize(30,.3)
        line.color("green")
    else:
        line.shapesize(stretch_wid=wn.window_height(),stretch_len=.1)
        # line.shapesize(30,.1)
        line.color("white")
    line.penup()
    line.goto(x=val, y=0)
    lines.append(line)

#balls
ball_direction = [-2.0,  -1.9, -1.8, -1.7, -1.6, -1.5, -1.4, -1.3, -1.2, -1.1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2]
ball_pos=[-75,-25, 25, 75,125, 175, 225]
balls=[]

for pos in ball_pos:
    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(pos,0)
    ball.dy = random.choice(ball_direction)
    balls.append(ball)

#pen for won message
pen = turtle.Turtle()
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0,0)

#pen for showing level
pen_level = turtle.Turtle()
pen_level.color("white")
pen_level.penup()
pen_level.hideturtle()
pen_level.goto(-220,200)

#for for showing the number of level
pen_level_number = turtle.Turtle()
pen_level_number.color("white")
pen_level_number.penup()
pen_level_number.hideturtle()
pen_level_number.goto(-160, 200)


#turtle for the game
user = turtle.Turtle()
user.shape("turtle")
user.color("red")
user.penup()
user.goto(-125,0)

#controlling user(player turtle)
def user_up():
    y = user.ycor()
    y = y+50
    if y> wn.window_height()//2:
        y=wn.window_height()//2-10
    user.sety(y)
def user_down():
    y = user.ycor()
    y=y-50
    if y< -wn.window_height()//2:
        y = -wn.window_height()//2+10
    user.sety(y)
def user_right():
    user.setx(user.xcor()+50)
def user_left():
    x = user.xcor()
    x=x-50
    if x<-125:
        x=-125
    user.setx(x)

# function to bounce ball
def bounce_ball(current_ball):
    if current_ball.ycor() > 240:
        current_ball.sety(240)
        current_ball.dy *= -1
    if current_ball.ycor() < -240:
        current_ball.sety(-240)
        current_ball.dy *= -1

# function for intersacting balls
def ball_intersaction(left_x, right_x, current_ball):
    if (user.xcor() > left_x and user.xcor() < right_x) and (current_ball.ycor() < user.ycor() +10 and current_ball.ycor()> user.ycor()-10):
        user.goto(-125,0)

def movement(level):
    for ball in balls:
        ball.sety(ball.ycor() + ball.dy*level)

    # instructing all balls to bounce
    for ball in balls:
        bounce_ball(ball)

    # user(player turtle) and ball interaction
    pos = 0
    for val in line_pos[:-1]:
        ball_intersaction(val,val+50,balls[pos])
        pos+=1

def main(level):
    pen_level.write("Level:", align="center", font=("Courier", 24, "normal"))
    pen_level_number.write(level, align="center", font=("Courier", 24, "normal"))


    while True:
        if user.xcor() < 250:
            wn.update()
            movement(level)
        else:
            wn.bgcolor("white")
            pen.write("ohoooo, You win!", align="center", font=40)


level = int(turtle.textinput("Input", "Choose you level"))

#controls of player
wn.listen()
wn.onkey(user_up,"Up")
wn.onkey(user_down,"Down")
wn.onkey(user_right,"Right")
wn.onkey(user_left,"Left")



main(level)

