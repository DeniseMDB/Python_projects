from  turtle import Turtle


class Ball():
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.shape("Circle")
        self.penup()
        self.width = 20
        self.height = 20
        x_pos = 0
        y_pos = 0

        
        