from pico2d import get_canvas_width, load_image


class Ball:
    SPEED = 10

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.image = load_image('ball21x21.png')

    def update(self):
        self.x += self.direction * Ball.SPEED

    def draw(self):
        self.image.draw(self.x, self.y)

    def is_out_of_bounds(self):
        return self.x < 0 or self.x > get_canvas_width()
