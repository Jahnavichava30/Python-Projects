from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):  # This is the initializer method
        super().__init__()  # This calls the initializer of the parent class (Turtle)
        self.shape("turtle")  # Set the shape of the player as a turtle
        self.penup()  # Prevent the player from drawing when it moves
        self.go_to_start_position()  # Start the player at the bottom of the screen
        self.setheading(90)  # Make the player face upward

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start_position(self):
        self.goto(STARTING_POSITION)

    def is_it_finish(self):
        if self.ycor() > 280:
            return True
        else:
            return False



