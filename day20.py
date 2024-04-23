from turtle import Turtle,Screen
from day21 import Food,score_board
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

up=90
left=180
right=0
down=270
game_is_on=True

starting_pos=[(0,0),(-20,0),(-40,0)]
segment=[]
for pos in starting_pos:
    new=Turtle(shape="square")
    new.color("white")
    new.penup()
    new.goto(pos)
    segment.append(new)
screen.update()

food=Food()
score=score_board()

def Left():
    if segment[0].heading() != right:
     segment[0].setheading(left)

def Right():
   if segment[0].heading() != left:
    segment[0].setheading(right)

def Up():
   if segment[0].heading()!=down:
    segment[0].setheading(up)

def Down():
    if segment[0].heading() != up:
     segment[0].setheading(down)

screen.listen()

screen.onkey(key="Left",fun=Left)
screen.onkey(key="Right",fun=Right)
screen.onkey(key="Up",fun=Up)
screen.onkey(key="Down",fun=Down)

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segment)-1,0,-1):
         new_x=segment[seg_num-1].xcor()
         new_y=segment[seg_num-1].ycor()
         segment[seg_num].goto(new_x,new_y)
    segment[0].forward(20)

    if segment[0].distance(food) < 15:
        food.refresh()
        score.increase()
        #adding or increasing length of snake
        new = Turtle(shape="square")
        new.color("white")
        new.penup()
        new.goto(segment[-1].pos())
        segment.append(new)

    #detect collision with wall
    if segment[0].xcor()>290 or  segment[0].xcor()<-290 or  segment[0].ycor()>290 or  segment[0].ycor()<-290:
        game_is_on=False
        score.game_over()

    #detect collision with tail

    for seg in segment:
       if seg==segment[0]:
        pass
       elif segment[0].distance(seg)<10:
           game_is_on=False
           score.game_over()


screen.exitonclick()

