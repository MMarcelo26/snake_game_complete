from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#TELA
screen = Screen()
screen.setup(width=600, height = 600)
screen.bgcolor("black")
screen.title("Meu Snake Game")
screen.tracer(0)

#CRIANDO OS OBJETOS
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



#COBRA
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    #delay por 0,1s e refresh a tela
    snake.move()


    #Detectar colisão com a comida
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.aumentar_score()


    #Detectando colisão com as paredes
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()


    #Detectar colisão com o rabo
    for segment in snake.segmentos[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


    '''for segment in snake.segmentos:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()'''











screen.exitonclick()

