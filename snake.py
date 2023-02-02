from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20,0), (20,0)] #constante
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segmentos = []
        self.create_snake()
        self.head = self.segmentos[0]

    def create_snake(self):

        for position in STARTING_POSITIONS:
            self.aumentar_segmento(position)

    def move(self):

        for seg_num in range(len(self.segmentos) - 1, 0, -1):
            novo_x = self.segmentos[seg_num - 1].xcor()
            novo_y = self.segmentos[seg_num - 1].ycor()
            self.segmentos[seg_num].goto(novo_x, novo_y)
        self.head.forward(MOVE_DISTANCE)


    def aumentar_segmento(self, position):

        novo_segmento = Turtle("square")
        novo_segmento.color("white")
        novo_segmento.penup()
        novo_segmento.goto(position)
        self.segmentos.append(novo_segmento)

    def extend(self):
        self.aumentar_segmento(self.segmentos[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)