import pygame
import pygame_window
import pygame_mouse_cursor
import pygame_myo_cursor
import threading

pygame.init()

resolution = (pygame.display.Info().current_w, pygame.display.Info().current_h)
screen = pygame.display.set_mode(resolution)

rect = pygame.Rect(60, 60, 300, 364)
font = pygame.font.Font(None, 36)

center_rect = pygame.Rect(screen.get_width() / 2, screen.get_height() / 2, 8, 8)

window = pygame_window.Window("Test", rect)

clock = pygame.time.Clock()
current_ms = 0
tickrate = 50

# mouse = pygame_mouse_cursor.MouseCursor(5)

myo = pygame_myo_cursor.MyoCursor(5)

offset = (0, 0)
header_clicked = False
bottom_right_clicked = False

white = (255, 255, 255)
black = (0, 0, 0)
x = 100
y = 100
while True:
    clock.tick()
    current_ms = current_ms + clock.get_time()

    # Run Myo, must be run constantly to prevent disconnect
    myo.run()

    if(current_ms >= tickrate):
        # Drawing
        screen.fill(black)
        window.draw(screen)
        # mouse.draw(screen)
        myo.draw(screen)
        pygame.draw.rect(screen, white, center_rect)
        pygame.display.update()

        # Updating
        window.update()
        # mouse.update()
        myo.update(screen)
        actions = myo.get_actions()
        print(actions)
        if "myo_set_reference" in actions:
            myo.set_reference()
        elif "myo_calibrate" in actions:
            myo.calibrate()
            myo.set_reference()

        pygame.event.get()

        # Printing
        print(window.get_intersect(myo.get_pos()[0], myo.get_pos()[1],  5))
        # print (myo.get_actions())
        # print (myo.get_pos())

        if "click_1" in actions:
            if window.get_intersect(myo.get_pos()[0], myo.get_pos()[1], 5) == "header":
                offset = myo.get_drag_offset(window.get_x(), window.get_y())
                header_clicked = True

            if window.get_intersect(myo.get_pos()[0], myo.get_pos()[1], 5) == "bottomright":
                print("BOTTOM RIGHT CLICKED")
                bottom_right_clicked = True

        if "hold_1" in actions:
            if header_clicked:
                window.move(myo.get_pos()[0] - offset[0], myo.get_pos()[1] - offset[1])

            if bottom_right_clicked:
                window.resize(window.get_position(), myo.get_pos())

        if "release_1" in actions:
            header_clicked = False
            bottom_right_clicked = False

        # Reset tick timer
        current_ms = 0
