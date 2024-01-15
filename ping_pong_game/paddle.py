from turtle import Turtle

# La clase Paddle crea un objeto tortuga de forma cuadrada con un color blanco y establece su tamaño,
# posición y estado de penup.
class Paddle(Turtle):
    def __init__(self, position) -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        """
        La función "go_up" mueve un objeto hacia arriba 28 unidades.
        """
        new_y = self.ycor() + 28
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """
        La función mueve un objeto hacia abajo 28 unidades.
        """
        new_y = self.ycor() - 28
        self.goto(self.xcor(), new_y)
