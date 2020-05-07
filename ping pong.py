import turtle

# Screen
mac = turtle.Screen()
mac.title("ping pong")
mac.bgcolor("black")
mac.setup(width = 800 , height = 600)
mac.tracer()

# Score count
scr_a = 0
scr_b = 0

# Bat A
bat_a = turtle.Turtle()
bat_a.speed(0)
bat_a.shape("square")
bat_a.color("white")
bat_a.shapesize(stretch_wid = 5 , stretch_len = 1)
bat_a.penup()
bat_a.goto(-350,0)

# Bat B
bat_b = turtle.Turtle()
bat_b.speed(0)
bat_b.shape("square")
bat_b.color("white")
bat_b.shapesize(stretch_wid = 5 , stretch_len = 1)
bat_b.penup()
bat_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 4
ball.dy = 4

# Score
score =turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,250)
score.write("Player A : 0 | Player B : 0", align="center" , font=("Courier" , 24, "normal"))

# Funcions

# Bat A
def bat_a_up():
    y = bat_a.ycor()
    y += 20
    bat_a.sety(y)

def bat_a_dn():
    y = bat_a.ycor()
    y -= 20
    bat_a.sety(y)

# Bat B
def bat_b_up():
    y = bat_b.ycor()
    y += 20
    bat_b.sety(y)

def bat_b_dn():
    y = bat_b.ycor()
    y -= 20
    bat_b.sety(y)    

# Keyboard
mac.listen()

# Bat A
mac.onkeypress(bat_a_up, "w")
mac.onkeypress(bat_a_dn, "s")

# Bat B
mac.onkeypress(bat_b_up, "Up")
mac.onkeypress(bat_b_dn, "Down")



# Game loop
while True :
    mac.update()

    # Ball movement 
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border check Y
    if ball.ycor() > 290 :
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() < -290 :
        ball.sety(-290)
        ball.dy *= -1   
    
    # Border check X
    if ball.xcor() > 390 :
        ball.goto(0,0)
        ball.dx *= -1 
        scr_a += 1 
        score.clear()
        score.write("Player A : {} | Player B : {}".format(scr_a,scr_b), align="center" , font=("Courier" , 24, "normal"))  
     
    elif ball.xcor() < -390 :
        ball.goto(0,0)
        ball.dx *= -1
        scr_b += 1 
        score.clear()
        score.write("Player A : {} | Player B : {}".format(scr_a,scr_b), align="center" , font=("Courier" , 24, "normal"))  
    
    # Collision
     
    # Bat B
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < bat_b.ycor() + 40 and ball.ycor() > bat_b.ycor() - 40) :
        ball.setx(340)
        ball.dx *= -1

    # Bat A
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < bat_a.ycor() + 40 and ball.ycor() >  bat_a.ycor() - 40) :
        ball.setx(-340)
        ball.dx *= -1


