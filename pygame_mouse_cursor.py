import pygame
import pygame_cursor


class MouseCursor(pygame_cursor.Cursor):
    mouse = None
    past_click_state = None

    def __init__(self, radius):
        self.mouse = pygame.mouse
        self.mouse.set_visible(False)
        self.position = self.mouse.get_pos()
        self.past_click_state = self.mouse.get_pressed()
        super().__init__(self.position, radius)

    def update(self, surface):
        self.mouse = pygame.mouse
        self.past_click_state = self.mouse.get_pressed()
        self.position = self.mouse.get_pos()
        super().update(surface)

    def left_click(self):
        if self.mouse.get_pressed()[0] is True and self.past_click_state[0] is False:
            return True
        return False

    def right_click(self):
        if self.mouse.get_pressed()[2] is True and self.past_click_state[2] is False:
            return True
        return False

    def left_release(self):
        if self.mouse.get_pressed()[0] is False and self.past_click_state[0] is True:
            return True
        return False

    def right_release(self):
        if self.mouse.get_pressed()[2] is False and self.past_click_state[2] is True:
            return True
        return False

    def left_pressed(self):
        if self.mouse.get_pressed()[0] and left_click() is False:
            return True
        return False

    def right_pressed(self):
        if self.mouse.get_pressed()[2] and right_click() is False:
            return True
        return False

    def get_actions(self):
        actions_list = []

        if self.left_click():
            actions_list.append("click_1")
        if self.right_click():
            actions_list.append("click_3")
        if self.left_release():
            actions_list.append("release_1")
        if self.right_release():
            actions_list.append("release_3")
        if self.left_pressed():
            actions_list.append("hold_1")
        if self.right_pressed():
            actions_list.append("hold_3")

        return actions_list
