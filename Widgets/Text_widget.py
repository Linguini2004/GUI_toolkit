# This is one of the widgets
# This widget simply blits text onto the screen
import pygame
from Resources.Wrap_text import static_wrap_text as wrap_text
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

        # dimension attributes:
        self.pos_hint = [0, 0]
        self.size_hint = [1, 1]
        self.compressible = True

        # private attributes:
        self._type = "text"
        self._dimensions = [0, 0]
        self. _position = [0, 0]
        self._text_loaded = False
        self._loaded_text = None

    def assign_dimensions(self, dimensions):
        """The provided size_hint is only advisory as certain layouts may manipulate dimensions in different ways
        Therefore the dimensions are set by the layout object itself rather than the user or widget"""

        self._dimensions = dimensions

    def assign_position(self, position, *kargs):
        """The provided pos_hint is only advisory as certain layouts may align and place widgets in different ways
        Therefore the position is set by the layout object itself rather than the user or widget"""

        self._position = position

    def draw(self, surface, *kargs):
        if not self._text_loaded:
            text = self.text
            color = self.text_colour
            rect = [self._position[0], self._position[1], self._dimensions[0], self._dimensions[1]]
            font = pygame.font.SysFont(self.font, self.font_size)
            align = self.align

            text_dict = wrap_text(text, color, rect, font, align)
            self._loaded_text = text_dict
            self._text_loaded = True

        text_dict = self._loaded_text
        for word, pos in text_dict.items():
            surface.blit(word, pos)

