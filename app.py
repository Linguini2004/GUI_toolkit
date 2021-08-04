# The purpose of this program is to act as a foundation for the application
# This involves drawing everything to the screen and housing the event loop
# It does not house any classes and does not handle the logic behind objects (which are to be dealt with by the object's methods)
import pygame
from pygame.locals import *

# noinspection PyAttributeOutsideInit
class App:
    def __init__(self):
        self._running = False
        self.screen_width = 400
        self.screen_height = 600

        self._screen = pygame.display.set_mode((self.screen_width, self.screen_height))

    def build(self):
        return None

    def run(self):
        pygame.init()
        self._running = True
        layout = self.build()

        while self._running:
            layout.draw_background(self._screen)
            widgets = layout.provide_widgets()

            for widget in widgets:
                widget.draw(self._screen, pygame.mouse.get_pos())

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    for widget in widgets:
                        if widget._type == "button":
                            if widget.mouse_click(pygame.mouse.get_pos()):
                                widget.action()


