import pygame
from pygame import *
from Resources.Image_size import image_proportion

class Image:
    def __init__(self):
        # image attributes:
        self.image_path = ""
        self.transparent = True

        # dimension attributes:
        self.keep_proportion = True
        self.scale = 1

        # header attributes:
        self.header_active = False
        self.header_text = ""
        self.header_align = "top"
        self.header_spacing = 0.01
        self.header_colour = (0, 0, 0)
        self.font = "arial"
        self.font_size = 20

        # private attributes:
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
    
    def _draw_header(self, surface, font):
        surface.blit(font.render(self.header_text, True, self.header_colour), (self._position[0], self._position[1]))
    
    def draw(self, surface, pos):
        image_to_draw = pygame.image.load(self.image_path)
        width = image_to_draw.get_width()
        height = image_to_draw.get_height()
        
        image_position = list(self._position)
        image_dimensions = list(self._dimensions)

        font = pygame.font.SysFont(self.font, self.font_size)
        spacing = self.header_spacing * self._dimensions[1]
        
        if self.header_active:
            if self.header_align == "top":
                image_position[1] += font.render("H", False, self.header_colour).get_height() + spacing
                image_dimensions[1] -= font.render("H", False, self.header_colour).get_height() + spacing
            elif self.header_align == "left":

                image_position[0] += (font.render(self.header_text, False, self.header_colour).get_width() + spacing)
                image_dimensions[0] -= (font.render(self.header_text, False, self.header_colour).get_width() + spacing)

        self._draw_header(surface, font)

        if self.keep_proportion:
            image_to_draw = image_proportion(width, height, image_dimensions, image_to_draw, self.scale)
        else:
            image_to_draw = pygame.transform.smoothscale(image_to_draw, (int(image_dimensions[0]), int(image_dimensions[1])))

        surface.blit(image_to_draw, (image_position[0], image_position[1]))