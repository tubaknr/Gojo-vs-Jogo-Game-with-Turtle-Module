import turtle
import random
import time
turtle.register_shape("okul2.gif")

wn = turtle.Screen()
wn.title("Gojolu Yılan Oyunu")
wn.setup(700,600)
wn.tracer(0)
wn.bgcolor("green")
turtle.register_shape("gojo_kucuk_jpg.gif")
turtle.register_shape("jogo.gif")

#Yılan
yilan = turtle.Turtle()
yilan.shape("gojo_kucuk_jpg.gif")
yilan.color("black")
yilan.speed(0)
yilan.penup()
yilan.goto(0,0)
yilan.direction = "stop"
yilan_speed = 0.2

#Yem
yem = turtle.Turtle()
yem.shape("jogo.gif")
yem.color("orange")
yem.speed(0)
yem.penup()
yem.goto(100,150)

gojo = 0
#Skor tablosu
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-250,270)
pen.write(f"GOJO : 0 ",align="center", font=("Courier",14,"normal"))

def move_yilan():
    if yilan.direction=="up":
        yilan.sety(yilan.ycor()+yilan_speed)
    if yilan.direction=="down":
        yilan.sety(yilan.ycor()-yilan_speed)
    if yilan.direction=="right":
        yilan.setx(yilan.xcor()+yilan_speed)
    if yilan.direction=="left":
        yilan.setx(yilan.xcor()-yilan_speed)


def go_up():
    if yilan.direction!="down":
        yilan.direction="up"

def go_down():
    if yilan.direction!="up":
        yilan.direction="down"

def go_right():
    if yilan.direction!="left":
        yilan.direction="right"

def go_left():
    if yilan.direction!="right":
        yilan.direction="left"


wn.listen()

wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# kuyruk_eklentileri = []

while True:
    wn.update()
    move_yilan()
    if yilan.xcor()>330 or yilan.xcor()<-330 or yilan.ycor()>280 or yilan.ycor()<-280:
        time.sleep(0.5)
        yilan.setpos(0,0)
        yilan.direction *= -1
        pen.clear()
        gojo -= 10
        pen.write(f"GOJO : {gojo} ", align="center", font=("Courier", 14, "normal"))

    if yilan.distance(yem)<40:
        yem.hideturtle()
        yem.setpos(random.randint(-310,310),random.randint(-250,250))
        yem.showturtle()
        pen.clear()
        gojo += 10
        pen.write(f"GOJO : {gojo} ", align="center", font=("Courier", 14, "normal"))

        if gojo==100:
            print("You win!")
            pen.clear()
            pen.setpos(-200,270)
            pen.write(f"GOJO : {gojo} YOU WIN!!!", align="center", font=("Courier", 14, "normal"))
            time.sleep(1)
            break

        if gojo==-100:
            print("Game Over!")
            pen.clear()
            pen.setpos(-200, 270)
            pen.write(f"GOJO : {gojo} GAME OVER!!!", align="center", font=("Courier", 14, "normal"))
            time.sleep(1)
            break



wn.mainloop()





