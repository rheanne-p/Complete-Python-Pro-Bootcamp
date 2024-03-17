from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments_list = []
        self.create_body(3)
        self.head = self.segments_list[0]

    def create_body(self, num_segments):
        x_value = 0
        for num in range(0, num_segments + 1):
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.setx(x_value)
            self.segments_list.append(new_segment)
            x_value -= 20

    def move(self):
        for segment in range(len(self.segments_list) - 1, 0, -1):
            earlier_position = self.segments_list[segment - 1].position()
            current_segment = self.segments_list[segment]
            current_segment.goto(earlier_position)
        self.head.forward(MOVE_DISTANCE)

    def add_tail(self):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(self.segments_list[-1].pos())
        self.segments_list.append(new_segment)

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