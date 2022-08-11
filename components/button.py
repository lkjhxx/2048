from position import Position
from graphics import Rectangle, Text


class Button:
    def __init__(self, position: Position, color, text):
        self.shape = Rectangle(position, color)
        self.text = Text(position, text)

    def set_position(self, position: Position):
        self.shape.set_position(position.get_position())
        self.text.set_position(position.get_position())

    def get_position(self):
        return self.shape.get_position()

    def draw(self):
        self.shape.draw()
        self.text.draw()

    def is_in_area(self, x, y):
        pos = self.shape.get_position()
        if pos[0] <= x <= pos[1] and pos[2] <= y <= pos[3]:
            return True
        else:
            return False
