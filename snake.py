from turtle import Turtle
POS = [(0, 0), (-20, 0), (-40, 0)]
DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.seg = []
        self.createSnake()
        self.head = self.seg[0]

    def add_seg(self, position):
        t = Turtle()
        t.shape("square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.seg.append(t)
    def createSnake(self):
        for position in POS:
            self.add_seg(position)

    def move(self):
        for i in range(len(self.seg) - 1, 0, -1):
            self.seg[i].goto(self.seg[i - 1].xcor(), self.seg[i - 1].ycor())
        self.head.forward(DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def increase_size(self):
        self.add_seg(self.seg[-1].position())

