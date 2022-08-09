import random
import arcade
from animate import AnimateList
from graphics import Text
from position import Position
from components import Number


class MyGame(arcade.Window):
    def __init__(self, screen_width, screen_height, screen_title):
        super().__init__(screen_width, screen_height, screen_title)
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.animate_list = AnimateList()
        self.open_menu = False
        self.game_loop = GameLoop(self.screen_width, self.screen_height, arcade.color.YELLOW_ORANGE, self.animate_list)

    def on_draw(self):
        arcade.start_render()
        if not self.animate_list.is_empty():
            self.animate_list.draw()
        else:
            if self.game_loop.get_should_add_number():
                self.game_loop.add_number()
        self.game_loop.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if not self.game_loop.is_game_over() and self.animate_list.is_empty():
            if symbol == arcade.key.UP:
                self.game_loop.update(status='up')
            if symbol == arcade.key.DOWN:
                self.game_loop.update(status='down')
            if symbol == arcade.key.LEFT:
                self.game_loop.update(status='left')
            if symbol == arcade.key.RIGHT:
                self.game_loop.update(status='right')


class GameLoop:
    def __init__(self, screen_width, screen_height, color, animate_list, num=4, half_width=40):
        self.num = num
        self.center_point_list = self._get_coordinate_list(screen_width, screen_height, num)
        self.animate_list = animate_list
        self.color = color
        self.half_width = half_width
        self.numbers_list = [[None] * num for _ in range(num)]
        self.should_add_number = False
        self.score = 0
        self.score_text = Text(position=Position([screen_width - 400, screen_width, 500, screen_height]),
                               text='Score: 0',
                               font_size=50)
        self.game_over = False
        self.game_over_text = Text(position=Position([screen_width - 300, screen_width, 400, screen_height]),
                                   text='Game Over',
                                   font_size=40)
        self.start()

    def _get_coordinate_list(self, screen_width, screen_height, num):
        return [[[100, 400], [200, 400], [300, 400], [400, 400]],
                [[100, 300], [200, 300], [300, 300], [400, 300]],
                [[100, 200], [200, 200], [300, 200], [400, 200]],
                [[100, 100], [200, 100], [300, 100], [400, 100]]]

    def _get_position(self, i, j):
        left = self.center_point_list[i][j][0] - 50
        right = left + 2 * self.half_width
        bottom = self.center_point_list[i][j][1] - 50
        top = bottom + 2 * self.half_width
        return [left, right, bottom, top]

    def start(self):
        i = random.randint(0, 3)
        j = random.randint(0, 3)
        self.numbers_list[i][j] = Number(Position(self._get_position(i, j)), self.color, '2')

    def update(self, status):
        count = 0

        if status == 'up':
            j = 0
            while j < self.num:
                i = 0
                while i < self.num - 1:
                    k = i + 1
                    while k < self.num:
                        if not self.numbers_list[i][j]:
                            if self.numbers_list[k][j]:
                                self.animate_list.add_animate(self.numbers_list[k][j],
                                                              Position(self._get_position(i, j)), k - i)
                                self.numbers_list[i][j], self.numbers_list[k][j] = self.numbers_list[k][j], None
                                count += 1
                                i -= 1
                                break
                            else:
                                k += 1
                        else:
                            if not self.numbers_list[k][j]:
                                k += 1
                            else:
                                num1 = int(self.numbers_list[i][j].get_text())
                                num2 = int(self.numbers_list[k][j].get_text())
                                if num1 == num2:
                                    self.score += num1 * 2
                                    self.numbers_list[i][j].set_text(str(num1 * 2))
                                    self.animate_list.add_animate(self.numbers_list[k][j],
                                                                  Position(self._get_position(i, j)), k - i)
                                    self.numbers_list[k][j] = None
                                    count += 1
                                    break
                                else:
                                    break
                    i += 1
                j += 1

        if status == 'down':
            j = self.num - 1
            while j >= 0:
                i = self.num - 1
                while i > 0:
                    k = i - 1
                    while k >= 0:
                        if not self.numbers_list[i][j]:
                            if self.numbers_list[k][j]:
                                self.animate_list.add_animate(self.numbers_list[k][j],
                                                              Position(self._get_position(i, j)), i - k)
                                self.numbers_list[i][j], self.numbers_list[k][j] = self.numbers_list[k][j], None
                                count += 1
                                i += 1
                                break
                            else:
                                k -= 1
                        else:
                            if not self.numbers_list[k][j]:
                                k -= 1
                            else:
                                num1 = int(self.numbers_list[i][j].get_text())
                                num2 = int(self.numbers_list[k][j].get_text())
                                if num1 == num2:
                                    self.score += num1 * 2
                                    self.numbers_list[i][j].set_text(str(num1 * 2))
                                    self.animate_list.add_animate(self.numbers_list[k][j],
                                                                  Position(self._get_position(i, j)), i - k)
                                    self.numbers_list[k][j] = None
                                    count += 1
                                    break
                                else:
                                    break
                    i -= 1
                j -= 1

        if status == 'left':
            i = 0
            while i < self.num:
                j = 0
                while j < self.num - 1:
                    k = j + 1
                    while k < self.num:
                        if not self.numbers_list[i][j]:
                            if self.numbers_list[i][k]:
                                self.animate_list.add_animate(self.numbers_list[i][k],
                                                              Position(self._get_position(i, j)), k - j)
                                self.numbers_list[i][j], self.numbers_list[i][k] = self.numbers_list[i][k], None
                                count += 1
                                j -= 1
                                break
                            else:
                                k += 1
                        else:
                            if not self.numbers_list[i][k]:
                                k += 1
                            else:
                                num1 = int(self.numbers_list[i][j].get_text())
                                num2 = int(self.numbers_list[i][k].get_text())
                                if num1 == num2:
                                    self.score += num1 * 2
                                    self.numbers_list[i][j].set_text(str(num1 * 2))
                                    self.animate_list.add_animate(self.numbers_list[i][k],
                                                                  Position(self._get_position(i, j)), k - j)
                                    self.numbers_list[i][k] = None
                                    count += 1
                                    break
                                else:
                                    break
                    j += 1
                i += 1

        if status == 'right':
            i = self.num - 1
            while i >= 0:
                j = self.num - 1
                while j > 0:
                    k = j - 1
                    while k >= 0:
                        if not self.numbers_list[i][j]:
                            if self.numbers_list[i][k]:
                                self.animate_list.add_animate(self.numbers_list[i][k],
                                                              Position(self._get_position(i, j)), j - k)
                                self.numbers_list[i][j], self.numbers_list[i][k] = self.numbers_list[i][k], None
                                count += 1
                                j += 1
                                break
                            else:
                                k -= 1
                        else:
                            if not self.numbers_list[i][k]:
                                k -= 1
                            else:
                                num1 = int(self.numbers_list[i][j].get_text())
                                num2 = int(self.numbers_list[i][k].get_text())
                                if num1 == num2:
                                    self.score += num1 * 2
                                    self.numbers_list[i][j].set_text(str(num1 * 2))
                                    self.animate_list.add_animate(self.numbers_list[i][k],
                                                                  Position(self._get_position(i, j)), j - k)
                                    self.numbers_list[i][k] = None
                                    count += 1
                                    break
                                else:
                                    break
                    j -= 1
                i -= 1

        if count == 0:
            return

        self.score_text.set_text('Score: ' + str(self.score))
        self.should_add_number = True

    def add_number(self):
        inds = []
        i = 0
        while i < self.num:
            j = 0
            while j < self.num:
                if not self.numbers_list[i][j]:
                    inds.append([i, j])
                j += 1
            i += 1

        ind = random.choice(inds)
        i, j = ind[0], ind[1]

        self.numbers_list[i][j] = Number(Position(self._get_position(i, j)), self.color, '2')
        self.should_add_number = False

        if len(inds) == 1:
            self._is_game_over()

    def get_should_add_number(self):
        return self.should_add_number

    def is_game_over(self):
        return self.game_over

    def _is_game_over(self):
        self.game_over = self._compare_text(0, 0)

    def _compare_text(self, i, j):
        if i >= self.num or j >= self.num:
            return True

        if j + 1 < self.num:
            if self.numbers_list[i][j].get_text() == self.numbers_list[i][j + 1].get_text():
                return False

        if i + 1 < self.num:
            if self.numbers_list[i][j].get_text() == self.numbers_list[i + 1][j].get_text():
                return False

        right = self._compare_text(i, j + 1)
        down = self._compare_text(i + 1, j)

        return right and down

    def draw(self):
        for nums in self.numbers_list:
            for num in nums:
                if num:
                    num.draw()

        self.score_text.draw()

        if self.game_over:
            self.game_over_text.draw()
