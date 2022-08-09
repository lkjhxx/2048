import arcade
from position import Position


class Rectangle(Position):
    def __init__(self, position: Position, color):
        super().__init__(position.get_position())
        self.color = color

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def draw(self):
        arcade.draw_lrtb_rectangle_filled(left=self.left,
                                          right=self.right,
                                          bottom=self.bottom,
                                          top=self.top,
                                          color=self.color)
