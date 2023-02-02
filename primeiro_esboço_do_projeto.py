from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height = 600)
screen.bgcolor("black")
screen.title("Meu Snake Game")
screen.tracer(0)

starting_positions = [(0,0), (-20,0), (20,0)]

segmentos = []

for position in starting_positions:
    novo_segmento = Turtle("square")
    novo_segmento.color("white")
    novo_segmento.penup()
    novo_segmento.goto(position)
    segmentos.append(novo_segmento)

game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.1)

    #movimento da cobra
    for seg_num in range(len(segmentos)-1,0,-1):
        novo_x = segmentos[seg_num - 1].xcor()
        novo_y = segmentos[seg_num - 1].ycor()
        segmentos[seg_num].goto(novo_x, novo_y)
    segmentos[0].forward(20)
    segmentos[0].left(90)














screen.exitonclick()

