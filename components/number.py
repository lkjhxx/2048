from position import Position
from graphics import Rectangle
from graphics import Text


class Number:
    def __init__(self, position: Position, color, text: str):
        self.shape = Rectangle(position, color)
        self.number = Text(position, text)

    def set_position(self, position: Position):
        self.shape.set_position(position.get_position())
        self.number.set_position(position.get_position())

    def get_position(self):
        return self.shape.get_position()

    def set_text(self, text):
        self.number.set_text(text)
        self.number.set_font_size(60 if len(text) == 1 else int(60 / len(text) * 1.5))

    def get_text(self):
        return self.number.get_text()

    def draw(self):
        self.shape.draw()
        self.number.draw()
