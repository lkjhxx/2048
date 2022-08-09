class Position:
    def __init__(self, sides: list):
        self.left = sides[0]
        self.right = sides[1]
        self.bottom = sides[2]
        self.top = sides[3]

    def set_position(self, sides: list):
        self.left = sides[0]
        self.right = sides[1]
        self.bottom = sides[2]
        self.top = sides[3]

    def get_position(self):
        return [self.left, self.right, self.bottom, self.top]
