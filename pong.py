import turtle
#create screen
sc= turtle.Screen()
sc.title("PONG GAME")
sc.bgcolor("green")
sc.setup(width=900, height=500)
#left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("white")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400 ,0)
#right paddle
right_pad=turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("white")
right_pad.shapesize(stretch_wid= 6, stretch_len= 2)
right_pad.penup()
right_pad.goto(400,0)
#ball of circle shape
hit_ball=turtle.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color("black")
hit_ball.penup()
hit_ball.goto(0,0)
hit_ball.dx=5
hit_ball.dy=-5
#score initialization
left_player=0
right_player=0
#display the score
sketch=turtle.Turtle()
sketch.speed(0)
sketch.color("black")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("left_player:0  right_player:0", align="center", font=("courier", 24, "normal"))
#to move paddle vertically
def paddleaup():
    y= left_pad.ycor()
    y +=20
    left_pad.sety(y)
def paddleadown():
    y=left_pad.ycor()
    y -=20
    left_pad.sety(y)
def paddlebup():
    y=right_pad.ycor()
    y +=20
    right_pad.sety(y)
def paddlebdown():
    y=right_pad.ycor()
    y -=20
    right_pad.sety(y)
#kerboard bindings
sc.listen()
sc.onkeypress(paddleaup,"x")
sc.onkeypress(paddleadown,"e")
sc.onkeypress(paddlebup,"up")
sc.onkeypress(paddlebdown,"down")
while True:
    sc.update()
    hit_ball.setx(hit_ball.xcor()+hit_ball.dx)
    hit_ball.sety(hit_ball.ycor()+hit_ball.dy)
    #checking borders
    if hit_ball.ycor()>280:
        hit_ball.sety(280)
        hit_ball.dy *=-1
    if hit_ball.ycor()< -280:
        hit_ball.sety(-280)
        hit_ball.dy *=-1
    if hit_ball.xcor()>500:
        hit_ball.goto(0,0)
        hit_ball.dy *=-1
        left_player +=1
        sketch.clear()
        sketch.write("left_player:{}  right_player:{}".format(left_player, right_player),align="center",font=("courier",24,"normal"))
    if hit_ball.xcor() < - 500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        right_player += 1
        sketch.clear()
        sketch.write("left_player:{}  right_player:{}".format(left_player, right_player), align="center", font=("courier", 24, "normal"))
        #paddle ball collision
        if (hit_ball.xcor() > 360 and hit_ball.xcor() < 370) and (hit_ball.ycor() < right_pad.ycor() + 40 and hit_ball.ycor() > right_pad.ycor()-40):
            hit_ball.setx(360)
            hit_ball.dx*=+1
        if (hit_ball.xcor() < -360 and hit_ball.xcor() > -370) and (hit_ball.ycor() < left_pad.ycor() + 40 and hit_ball.ycor() > left_pad.ycor() - 40):
            hit_ball.setx(-360)
            hit_ball.dx *= -1








