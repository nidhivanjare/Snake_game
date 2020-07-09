import turtle
import time
import random

delay = 0.1

score = 0
high_score = 0


# set up th screen
win = turtle.Screen()
win.title("SNAKE GAME")
win.bgcolor("green")
win.setup(width=600, height=600)
win.tracer(0)

# snake

head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# food

food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(" SCORE : 0  HIGH SCORE : 0",align="center", font=("Courier",24,"normal"))


# fuctions

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# keyboard bindings

win.listen()
win.onkey(go_up, "w")
win.onkey(go_down, "s")
win.onkey(go_left, "a")
win.onkey(go_right, "d")

while True:
    win.update()
    # CHECk FOR COLLISION with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()

        score = 0
        delay = 0.1
        pen.clear()
        pen.write(" SCORE : {}  HIGH SCORE : {} ".format(score, high_score), align="center",font=("Courier", 24, "normal"))

    # CHECK FOR COLLISION with food
    if head.distance(food) < 20:
        # move food
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001

        #score
        score += 1

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(" SCORE : {}  HIGH SCORE : {} ".format(score, high_score) ,align="center", font=("Courier",24,"normal"))

        # move end segments
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # move segment 0 to head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # check for head and body collisions
    for segment in segments:
        if segment.distance(head) <20 :
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000,1000)

            segments.clear()

            score = 0

            delay = 0.1

            pen.clear()
            pen.write(" SCORE : {}  HIGH SCORE : {} ".format(score, high_score), align="center",font=("Courier", 24, "normal"))



    time.sleep(delay)

win.mainloop()
