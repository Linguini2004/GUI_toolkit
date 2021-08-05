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
        self.title = "GUI"

        self._screen = pygame.display.set_mode((self.screen_width, self.screen_height))

    def build(self):
        return None

    def _get_widgets(self, main_layout):
        widgets = []
        if type(main_layout) == list:
            for layout in main_layout:
                widgets += layout.provide_widgets()

        elif type(main_layout) == dict:
            for layout in main_layout:
                widgets += layout.provide_widgets()

        else:
            widgets = main_layout.provide_widgets()

        return widgets

    def _draw_backgrounds(self, main_layout):
        if type(main_layout) == list:
            for layout in main_layout:
                layout.draw_background(self._screen)

        elif type(main_layout) == dict:
            for layout in main_layout:
                layout.draw_background(self._screen)

        else:
            main_layout.draw_background(self._screen)

    def _assign_layout_params(self, main_layout):
        if type(main_layout) == list:
            layout_width = self.screen_width
            layout_height = self.screen_height / len(main_layout)
            for i, layout in enumerate(main_layout):
                layout.draw_background(self._screen)
                layout.assign_dimensions((layout_width, layout_height))
                layout.assign_position((0, i * layout_height))

        elif type(main_layout) == dict:
            layout_width = self.screen_width
            layout_heights = []
            for size in main_layout.values():
                layout_heights.append(size * self.screen_height)

            for i, (layout, size) in enumerate(main_layout.items()):
                layout.draw_background(self._screen)
                layout.assign_dimensions((layout_width, layout_heights[i]))
                layout.assign_position((0, sum(layout_heights[:i])))
        else:
            main_layout.assign_dimensions((self.screen_width, self.screen_height))
            main_layout.assign_position((0, 0))

    def run(self):
        pygame.init()
        pygame.display.set_caption(self.title)
        self._running = True
        main_layout = self.build()
        widgets = self._get_widgets(main_layout)
        self._assign_layout_params(main_layout)

        while self._running:
            self._draw_backgrounds(main_layout)

            for widget in widgets:
                widget.draw(self._screen, pygame.mouse.get_pos())

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    for widget in widgets:
                        if widget._type in ["button", "text_input"]:
                            if widget.mouse_click(pygame.mouse.get_pos()):
                                try:
                                    widget.action()
                                except AttributeError:
                                    pass
                if event.type == KEYDOWN:
                    for widget in widgets:
                        if widget._type == "text_input":
                            widget._update(event)
