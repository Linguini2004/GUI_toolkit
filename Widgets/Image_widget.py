import pygame
from pygame import *

class Image:
    def __init__(self):
        self.image_path = ""
        self.padding = [0, 0, 0, 0]
        self.transparent = True
        self.header_active = False
        self.header_text = ""
        self.header_align = "top"

        self._act_padding = [0, 0, 0, 0]
        self._type = "image"
        self._dimensions = [0, 0]
        self._position = [0, 0]

    def assign_dimensions(self, dimensions):
        """The provided size_hint is only advisory as certain layouts may manipulate dimensions in different ways
        Therefore the dimensions are set by the layout object itself rather than the user or widget"""

        self._dimensions = dimensions

    def assign_position(self, position):
        """The provided pos_hint is only advisory as certain layouts may align and place widgets in different ways
        Therefore the position is set by the layout object itself rather than the user or widget"""

        self._position = position

    def draw(self, surface, pos):
        pass