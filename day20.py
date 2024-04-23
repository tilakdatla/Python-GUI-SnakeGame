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




# from turtle import Turtle,Screen
# import random
# import time
#
# screen=Screen()
# screen.bgcolor("black")
# screen.setup(600,600)
# screen.title("My snake game")
# screen.tracer(0)
#
# #step 3-turning
#
# up=90
# left=180
# right=0
# down=270
#
# def Left():
#     if segment[0].heading() != right:
#      segment[0].setheading(left)
#
# def Right():
#    if segment[0].heading() != left:
#     segment[0].setheading(right)
#
# def Up():
#    if segment[0].heading()!=down:
#     segment[0].setheading(up)
#
# def Down():
#     if segment[0].heading() != up:
#      segment[0].setheading(down)
#
# screen.listen()
#
# screen.onkey(key="Left",fun=Left)
# screen.onkey(key="Right",fun=Right)
# screen.onkey(key="Up",fun=Up)
# screen.onkey(key="Down",fun=Down)
#
# #step -1 creating a snake
#
# start=[0,-20,-40]
# segment=[]
# for i in range(0,3):
#     new=Turtle("square")
#     new.color("white")
#     new.penup()
#     new.goto(x=start[i],y=0)
#     segment.append(new)
# screen.update()
#
# #step -5 collision with food
#
# class Food(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.shape("circle")
#         self.color("blue")
#         self.penup()
#         self.shapesize(0.5,0.5)
#         self.speed(40)
#         self.refresh()
#
#     def refresh(self):
#         ramdom_x=random.randint(-280,280)
#         random_y=random.randint(-280,280)
#         self.goto(ramdom_x,random_y)
#
# food=Food()
#
# #step -6
#
# class score(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.score=0
#         self.color("white")
#         self.penup()
#         self.hideturtle()
#         self.goto(0,265)
#         self.update()
#
#     def update(self):
#         self.write(f"Score {self.score}" ,align="center",font=("Arial",24,"normal"))
#
#     def game_over(self):
#         self.goto(0,0)
#         self.write(f"GAME OVER!", align="center", font=("Arial", 24, "normal"))
#
#     def increase(self):
#         self.score+=1
#         self.clear()
#         self.update()
#
# score=score()
# #step 2-moving the snake
#
# moving=True
# while moving:
#     screen.update()
#     time.sleep(0.1)
#     for seg_num in range(len(segment)-1,0,-1):
#        new_x=segment[seg_num-1].xcor()
#        new_y=segment[seg_num-1].ycor()
#        segment[seg_num].goto(new_x,new_y)
#     segment[0].forward(20)
#
#     #step -5 collision with food
#     if segment[0].distance(food)<15:
#         food.refresh()
#         score.increase()
#         #increasing length of snake
#         new = Turtle("square")
#         new.color("white")
#         new.penup()
#         new.goto(segment[-1].pos())
#         segment.append(new)
#
#     #step 7 collision with wall
#     if segment[0].xcor()>293 or segment[0].xcor()<-293 or segment[0].ycor()>293 or segment[0].ycor()<-293:
#         score.game_over()
#         moving=False
#
#     #step -8 collision with body
#     for seg in segment:
#         if seg==segment[0]:
#             pass
#         elif segment[0].distance(seg)<10:
#             moving=False
#             score.game_over()






































screen.exitonclick()














