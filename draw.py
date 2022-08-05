import arcade
import random


class MyGame(arcade.Window):
    def __init__(self, screen_width, screen_height, screen_title):
        super().__init__(screen_width, screen_height, screen_title)
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.open_menu = False
        self.menu = Menu(screen_width, screen_height)
        self.menu.add_button(name='返回',
                             center=(200, 100),
                             width=200,
                             height=100)
        self.game = Game(screen_width, screen_height)

    def on_draw(self):
        arcade.start_render()
        self.game.draw()
        if self.open_menu:
            self.menu.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            self.open_menu = not self.open_menu
        if symbol == arcade.key.UP and not self.open_menu:
            self.game.update(status='up')
        if symbol == arcade.key.DOWN and not self.open_menu:
            self.game.update(status='down')
        if symbol == arcade.key.LEFT and not self.open_menu:
            self.game.update(status='left')
        if symbol == arcade.key.RIGHT and not self.open_menu:
            self.game.update(status='right')

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if self.open_menu:
            self.open_menu = self.menu.get_button('返回').on_pressed(x, y, self.open_menu)


class Menu:
    def __init__(self, screen_width, screen_height):
        self.scale = 0.5
        self.left = screen_width * self.scale * 0.5
        self.right = screen_width - self.left
        self.bottom = screen_height * self.scale * 0.5
        self.top = screen_height - self.bottom
        self.buttons = []
        self.buttons_dict = dict()

    def draw(self):
        arcade.draw_lrtb_rectangle_filled(left=self.left,
                                          right=self.right,
                                          top=self.top,
                                          bottom=self.bottom,
                                          color=arcade.color.YELLOW_ORANGE)
        for button in self.buttons:
            button.draw()

    def add_button(self, name, width, height, center):
        self.buttons_dict[name] = len(self.buttons)
        self.buttons.append(Button(name, width, height, center))

    def get_button(self, name):
        if self.buttons:
            return self.buttons[self.buttons_dict[name]]


class Button:
    def __init__(self, name, width, height, center):
        self.left = (center[0] - width * 0.5) * 0.5
        self.right = self.left + width
        self.bottom = (center[1] - height * 0.5) * 0.5
        self.top = height
        self.name = name

    def draw(self):
        arcade.draw_lrtb_rectangle_filled(left=self.left,
                                          right=self.right,
                                          top=self.top,
                                          bottom=self.bottom,
                                          color=arcade.color.BLUE)
        arcade.draw_text(text=self.name,
                         start_x=self.left,
                         start_y=self.bottom)

    def on_pressed(self, x, y, flag=True):
        if self.left <= x <= self.right and self.bottom <= y <= self.top:
            return not flag
        return flag


class Game:
    def __init__(self, screen_width, screen_height, num=4):
        self.num = num
        self.coordinate_list = self.get_coordinate_list(screen_width, screen_height, num)
        self.rect_side = 80
        self.numbers_list = [[None] * num for _ in range(num)]
        self.start()

    def get_coordinate_list(self, screen_width, screen_height, num):
        return [[[100, 400], [200, 400], [300, 400], [400, 400]],
                [[100, 300], [200, 300], [300, 300], [400, 300]],
                [[100, 200], [200, 200], [300, 200], [400, 200]],
                [[100, 100], [200, 100], [300, 100], [400, 100]]]

    def start(self):
        i = random.randint(0, 3)
        j = random.randint(0, 3)
        self.numbers_list[i][j] = Number(2, self.coordinate_list[i][j], self.rect_side)

    def update(self, status):
        count = 0
        if status == 'up':
            for j in range(self.num):
                for i in range(self.num - 1):
                    k = i + 1
                    while k < self.num:
                        if not self.numbers_list[i][j]:
                            if self.numbers_list[k][j]:
                                self.numbers_list[i][j], self.numbers_list[k][j] = self.numbers_list[k][j], None
                                self.numbers_list[i][j].set_new_center(self.coordinate_list[i][j])
                                count += 1
                                break
                            else:
                                k += 1
                        else:
                            if not self.numbers_list[k][j]:
                                k += 1
                            else:
                                if self.numbers_list[i][j].val == self.numbers_list[k][j].val:
                                    self.numbers_list[i][j].val *= 2
                                    self.numbers_list[k][j] = None
                                    count += 1
                                    break
                                else:
                                    break
        if status == 'down':
            for j in range(self.num - 1, -1, -1):
                for i in range(self.num - 1, 0, -1):
                    k = i - 1
                    while k >= 0:
                        if not self.numbers_list[i][j]:
                            if self.numbers_list[k][j]:
                                self.numbers_list[i][j], self.numbers_list[k][j] = self.numbers_list[k][j], None
                                self.numbers_list[i][j].set_new_center(self.coordinate_list[i][j])
                                count += 1
                                break
                            else:
                                k -= 1
                        else:
                            if not self.numbers_list[k][j]:
                                k -= 1
                            else:
                                if self.numbers_list[i][j].val == self.numbers_list[k][j].val:
                                    self.numbers_list[i][j].val *= 2
                                    self.numbers_list[k][j] = None
                                    count += 1
                                    break
                                else:
                                    break
        if status == 'left':
            for i in range(self.num):
                for j in range(self.num - 1):
                    k = j + 1
                    while k < self.num:
                        if not self.numbers_list[i][j]:
                            if self.numbers_list[i][k]:
                                self.numbers_list[i][j], self.numbers_list[i][k] = self.numbers_list[i][k], None
                                self.numbers_list[i][j].set_new_center(self.coordinate_list[i][j])
                                count += 1
                                break
                            else:
                                k += 1
                        else:
                            if not self.numbers_list[i][k]:
                                k += 1
                            else:
                                if self.numbers_list[i][j].val == self.numbers_list[i][k].val:
                                    self.numbers_list[i][j].val *= 2
                                    self.numbers_list[i][k] = None
                                    count += 1
                                    break
                                else:
                                    break
        if status == 'right':
            for i in range(self.num - 1, -1, -1):
                for j in range(self.num - 1, 0, -1):
                    k = j - 1
                    while k >= 0:
                        if not self.numbers_list[i][j]:
                            if self.numbers_list[i][k]:
                                self.numbers_list[i][j], self.numbers_list[i][k] = self.numbers_list[i][k], None
                                self.numbers_list[i][j].set_new_center(self.coordinate_list[i][j])
                                count += 1
                                break
                            else:
                                k -= 1
                        else:
                            if not self.numbers_list[i][k]:
                                k -= 1
                            else:
                                if self.numbers_list[i][j].val == self.numbers_list[i][k].val:
                                    self.numbers_list[i][j].val *= 2
                                    self.numbers_list[i][k] = None
                                    count += 1
                                    break
                                else:
                                    break

        if count == 0:
            return

        inds = []
        i = 0
        while i < self.num:
            j = 0
            while j < self.num:
                if not self.numbers_list[i][j]:
                    inds.append([i, j])
                j += 1
            i += 1

        print(len(inds))

        ind = random.choice(inds)
        i, j = ind[0], ind[1]

        self.numbers_list[i][j] = Number(2, self.coordinate_list[i][j], self.rect_side)

    def draw(self):
        for nums in self.numbers_list:
            for num in nums:
                if num:
                    num.draw()


class Number:
    def __init__(self, val, center, side_length):
        self.val = val
        self.left = center[0] - side_length * 0.5
        self.right = self.left + side_length
        self.bottom = center[1] - side_length * 0.5
        self.top = self.bottom + side_length
        self.side_length = side_length
        self.current_left = self.left
        self.current_right = self.right
        self.current_bottom = self.bottom
        self.current_top = self.top

    def draw(self):
        self.current_left = self.move(self.current_left, self.left)
        self.current_right = self.move(self.current_right, self.right)
        self.current_bottom = self.move(self.current_bottom, self.bottom)
        self.current_top = self.move(self.current_top, self.top)

        arcade.draw_lrtb_rectangle_filled(left=self.current_left,
                                          right=self.current_right,
                                          top=self.current_top,
                                          bottom=self.current_bottom,
                                          color=arcade.color.AIR_FORCE_BLUE)
        arcade.draw_text(text=str(self.val),
                         start_x=self.left,
                         start_y=self.bottom)

    def set_new_center(self, center):
        self.left = center[0] - self.side_length * 0.5
        self.right = self.left + self.side_length
        self.bottom = center[1] - self.side_length * 0.5
        self.top = self.bottom + self.side_length

    def move(self, cur, pos):
        if cur < pos:
            return cur + 10
        elif cur > pos:
            return cur - 10
        else:
            return pos
