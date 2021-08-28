import pygame
from pygame import *
import time
from Resources.Image_size import image_proportion

class Image:
    def __init__(self):
        # image attributes:
        self.image_path = ""
        self.transparent = True

        # dimension attributes:
        self.keep_proportion = True
        self.scale = 1
        self.size_hint = [1, 1]
        self.pos_hint = [0, 0]
        self.compressible = True

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
        self._loaded = False
        self._image_to_draw = None
        self._dimensions = [0, 0]
        self._position = [0, 0]
        self._loaded_header = None
        self._loaded_image = None
        self._loaded_dim = [0, 0]
        self._loaded_pos = [0, 0]
        self._rect_loaded = False

    def assign_dimensions(self, dimensions):
        """The provided size_hint is only advisory as certain layouts may manipulate dimensions in different ways
        Therefore the dimensions are set by the layout object itself rather than the user or widget"""

        self._dimensions = dimensions

    def assign_position(self, position, *kargs):
        """The provided pos_hint is only advisory as certain layouts may align and place widgets in different ways
        Therefore the position is set by the layout object itself rather than the user or widget"""

        self._position = position
    
    def _draw_header(self, surface, font):
        surface.blit(font.render(self.header_text, True, self.header_colour), (self._position[0], self._position[1]))
    
    def draw(self, surface, *kargs):
        if not self._loaded:
            self._image_to_draw = pygame.image.load(self.image_path)
            self._loaded = True

        image_to_draw = self._image_to_draw

        width = image_to_draw.get_width()
        height = image_to_draw.get_height()
        
        image_position = list(self._position)
        image_dimensions = list(self._dimensions)

        font = pygame.font.SysFont(self.font, self.font_size)
        spacing = self.header_spacing * self._dimensions[1]
        
        if self.header_active:
            if not self._rect_loaded:
                if self.header_align == "top":
                    image_position[1] += font.render("H", False, self.header_colour).get_height() + spacing
                    self._loaded_pos = image_position
                    image_dimensions[1] -= font.render("H", False, self.header_colour).get_height() + spacing
                    self._loaded_dim = image_dimensions
                elif self.header_align == "left":
                    image_position[0] += (font.render(self.header_text, False, self.header_colour).get_width() + spacing)
                    self._loaded_pos = image_position
                    image_dimensions[0] -= (font.render(self.header_text, False, self.header_colour).get_width() + spacing)
                    self._loaded_dim = image_dimensions
                self._rect_loaded = True
        else:
            self._loaded_dim = image_dimensions
            self._loaded_pos = image_position

        self._draw_header(surface, font)

        if self._loaded_image is None:
            if self.keep_proportion:
                self._loaded_image = image_proportion(width, height, self._loaded_dim, image_to_draw, self.scale)
            else:
                self._loaded_image = pygame.transform.smoothscale(image_to_draw, (int(self._loaded_dim[0]), int(self._loaded_dim[1])))

        surface.blit(self._loaded_image, (self._loaded_pos[0], self._loaded_pos[1]))
