from  turtle import Turtle


# La clase Ball representa un objeto blanco con forma de círculo que puede moverse en las direcciones
# x e y.
class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.move_speed = 0.1
        self.width = 20
        self.height = 20
        self.x_move = 10
        self.y_move = 10
    
    

    def move(self):
        """
        La función mueve un objeto a una nueva posición
        según su posición actual y sus valores de
        movimiento.
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """
        La función cambia la dirección del movimiento y multiplicándolo por -1.
        """
        self.y_move *= -1

    def bounce_x(self):
        """
        La función cambia la dirección del movimiento a
        lo largo del eje x y reduce la velocidad en un
        10%.
        """
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """
        La función restablece la posición de un objeto a las coordenadas (0,0)
        y establece la velocidad de movimiento en 0,1,
        luego llama al método rebote_x().
        """
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()