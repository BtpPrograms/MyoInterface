import pygame

class Window:
    header = None
    inner_window = None
    whole_window = None
    top_margin = None
    left_margin = None
    right_margin = None
    bottom_margin = None

    header_height = 64
    margin_width = 64

    window_name = None
    font = None

    image = None

    def __init__(self, window_name, window_rect):
        self.whole_window = pygame.Rect(window_rect)
        self.update()

        self.window_name = window_name

    def update(self):
        corner_x, corner_y = self.whole_window.topleft
        width = self.whole_window.width
        height = self.whole_window.height

        self.header = pygame.Rect(corner_x + self.margin_width, corner_y + self.margin_width, width - (self.margin_width * 2), self.header_height)
        self.inner_window = pygame.Rect(corner_x + self.margin_width, corner_y + self.margin_width + self.header_height, width - (self.margin_width * 2), height - (self.margin_width * 2) - self.header_height)

        self.top_margin = pygame.Rect(corner_x, corner_y, width, self.margin_width)
        self.left_margin = pygame.Rect(corner_x, corner_y, self.margin_width, height)
        self.right_margin = pygame.Rect(corner_x + width - self.margin_width, corner_y, self.margin_width, height)
        self.bottom_margin = pygame.Rect(corner_x, corner_y + height - self.margin_width, width, self.margin_width)

        self.whole_window = self.header.unionall([self.inner_window, self.top_margin, self.left_margin, self.right_margin, self.bottom_margin])

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.header, 0)
        pygame.draw.rect(surface, (255, 0, 0), self.inner_window, 0)

        pygame.draw.rect(surface, (0, 0, 255), self.left_margin, 0)
        pygame.draw.rect(surface, (0, 0, 255), self.right_margin, 0)
        pygame.draw.rect(surface, (0, 255, 0), self.top_margin, 0)
        pygame.draw.rect(surface, (0, 255, 0), self.bottom_margin, 0)

    def resize(self, topleft, bottomright):
        if (bottomright[0] - topleft[0]) > 300:
            self.whole_window.width = bottomright[0] - topleft[0]
        if (bottomright[1] - topleft[1]) > 300:
            self.whole_window.height = bottomright[1] - topleft[1]
        self.whole_window.topleft = topleft


    def move(self, x, y):
        self.whole_window.topleft = (x, y)

    def get_position(self):
        return self.whole_window.topleft

    def get_x(self):
        return self.whole_window.topleft[0]

    def get_y(self):
        return self.whole_window.topleft[1]

    def get_intersect(self, x, y, radius):
        cursor = pygame.Rect((x - radius, y - radius, radius * 2, radius * 2))
        if cursor.colliderect(self.whole_window):
            if cursor.colliderect(self.top_margin):
                if cursor.colliderect(self.left_margin):
                    return ("topleft")
                elif cursor.colliderect(self.right_margin):
                    return ("topright")
                else:
                    return ("top")

            elif cursor.colliderect(self.left_margin):
                if cursor.colliderect(self.bottom_margin):
                    return("bottomleft")
                else:
                    return ("left")

            elif cursor.colliderect(self.right_margin):
                if cursor.colliderect(self.bottom_margin):
                    return("bottomright")
                else:
                    return ("right")

            elif cursor.colliderect(self.bottom_margin):
                return ("bottom")

            elif cursor.colliderect(self.header):
                return ("header")

            elif cursor.colliderect(self.inner_window):
                return ("inner_window")

            else:
                return (None)


