'''A classe comida deve ser capaz de fazer a cobra
detectar toda vez que a cobra tocar na comida e após
isso, gerar outra comida em um local aleatório'''
from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-280,280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)













'''L21 -> Vai para outro local após a colisão'''



''' L6-> A classe Food está herdando métodos e atributos da superclasse
Turtle'''

'''L12 -> Formato da comida 10x10'''

'''L14 -> Cria o objeto food rapidamente e o leva para outra posição'''

'''L18 -> Por meio da biblioteca random,fazendo a comida aparecer em um local aleatório da tela'''