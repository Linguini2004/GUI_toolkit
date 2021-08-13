# This is one of the widgets
# This widget simply blits text onto the screen
import pygame
from Resources.Wrap_text import wrap_text
from pygame import *

class Text:
    def __init__(self):
        # text attributes:
        self.text_colour = (255, 255, 255)
        self.text = ""
        self.font = "arial"
        self.font_size = 20
        self.align = 0
        # align must be 0, 1, 2 or 3

        # private attributes:
        self._type = "text"
        self._dimensions = [0, 0]
        self. _position = [0, 0]

    def assign_dimensions(self, dimensions):
        """The provided size_hint is only advisory as certain layouts may manipulate dimensions in different ways
        Therefore the dimensions are set by the layout object itself rather than the user or widget"""

        self._dimensions = dimensions

    def assign_position(self, position):
        """The provided pos_hint is only advisory as certain layouts may align and place widgets in different ways
        Therefore the position is set by the layout object itself rather than the user or widget"""

        self._position = position

    def draw(self, surface, pos):
        text = self.text
        color = self.text_colour
        rect = [self._position[0], self._position[1], self._dimensions[0], self._position[1]]
        font = pygame.font.SysFont(self.font, self.font_size)
        align = self.align

        wrap_text(surface, text, color, rect, font, align)

