import turtle
import time
import random

delay = 0.1 

#setup screen
wm = turtle.Screen()
wm.title("SNAKE BY XERNOM-GT")
wm.bgcolor("grey")
wm.setup(width= 600, height = 600)
wm.tracer(0)


#program game
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('black')
head.penup()
head.goto(0,0)
head.direction = 'stop'

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto (0,100)

segments = []

#function
def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)
    
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
    
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)
    
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)
    
#funtioon
def go_up():
    head.direction = "up"
    
def go_down():
    head.direction = "down"
    
def go_right():
    head.direction = "right"
    
def go_left():
    head.direction = "left"
    
#keybind
wm.listen()
wm.onkeypress(go_up, "w")
wm.onkeypress(go_down, "s")
wm.onkeypress(go_right, "d")
wm.onkeypress(go_left, "a")

#main game loop
while True:
    wm.update()
    if head.distance(food) < 20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x , y)
        
        #add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('blue')
        new_segment.penup()
        segments.append(new_segment)

    #move the end segment
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()


    move()
    time.sleep(delay)


