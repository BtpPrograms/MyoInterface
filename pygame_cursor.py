import pygame

class Cursor:
    position = None
    radius = None

    def __init__(self, position, radius):
        self.saved_position = ()
        self.position = position
        self.radius = radius

    def update(self, surface):
        self.clamp_pos(surface)

    def draw(self, surface):
        pygame.draw.circle(surface, (130, 130, 130), self.position, self.radius, 0)

    def set_pos(self, x, y):
        self.position = (x, y)

    def get_pos(self):
        return self.position

    def save_pos(self):
        self.saved_position = self.position

    def set_x(self, x):
        self.position = (x, self.position[1])

    def get_x(self):
        return self.position[0]

    def set_y(self, y):
        self.position = (self.position[0], y)

    def get_y(self):
        return self.position[1]

    def get_drag_offset(self, object_x, object_y):
        x = self.position[0] - object_x
        y = self.position[1] - object_y
        return (x, y)

    def get_actions(self):
        raise NotImplementedError("get_action must be implemented")

    def clamp_pos(self, surface):
        if self.get_x() < 0:
            self.set_x(0)
        elif self.get_x() > surface.get_width():
            self.set_x(surface.get_width())

        if self.get_y() < 0:
            self.set_y(0)
        elif self.get_y() > surface.get_height():
            self.set_y(surface.get_height())
