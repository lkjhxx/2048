from position import Position

SPEED_SCALE = 2


class AnimateList:
    def __init__(self):
        self.animate_list = []

    def add_animate(self, obj, destination, continue_time):
        self.animate_list.append(Animate(obj, destination, continue_time))

    def draw(self):
        for i in range(len(self.animate_list)):
            flag = self.animate_list[i].update()
            self.animate_list[i].draw()
            if flag:
                self.animate_list[i] = None

        while None in self.animate_list:
            self.animate_list.remove(None)

    def is_empty(self):
        return True if self.animate_list == [] else False


class Animate:
    def __init__(self, obj, destination: Position, continue_time):
        self.obj = obj
        self.position = self.obj.get_position()
        self.destination = destination.get_position()
        self.continue_time = continue_time
        self.speed = [0, 0]
        self.is_done = False
        self._get_speed_x_and_y()

    def _get_speed_x_and_y(self):
        self.speed[0] = (self.destination[0] - self.position[0]) / self.continue_time / SPEED_SCALE
        self.speed[1] = (self.destination[2] - self.position[2]) / self.continue_time / SPEED_SCALE

    def update(self):
        if self.is_done:
            return True

        if abs(self.speed[0]) < abs(self.destination[0] - self.position[0]):
            self.position[0] += self.speed[0]
        else:
            self.position[0] = self.destination[0]

        if abs(self.speed[0]) < abs(self.destination[1] - self.position[1]):
            self.position[1] += self.speed[0]
        else:
            self.position[1] = self.destination[1]

        if abs(self.speed[1]) < abs(self.destination[2] - self.position[2]):
            self.position[2] += self.speed[1]
        else:
            self.position[2] = self.destination[2]

        if abs(self.speed[1]) < abs(self.destination[3] - self.position[3]):
            self.position[3] += self.speed[1]
        else:
            self.position[3] = self.destination[3]

        if self.position == self.destination:
            self.is_done = True

        self.obj.set_position(Position(self.position))

        return False

    def draw(self):
        self.obj.draw()
