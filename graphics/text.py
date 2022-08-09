import arcade
from position import Position


class Text(Position):
    def __init__(self, position: Position, text: str, font_size=60):
        super().__init__(position.get_position())
        self.text = text
        self.font_size = font_size

    def set_text(self, text: str):
        self.text = text

    def get_text(self) -> str:
        return self.text

    def set_font_size(self, font_size):
        self.font_size = font_size

    def draw(self):
        arcade.draw_text(text=self.text,
                         start_x=self.left,
                         start_y=self.bottom,
                         font_size=self.font_size)

