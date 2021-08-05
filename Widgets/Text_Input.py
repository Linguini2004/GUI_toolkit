# This is one of the widgets
# This widget will allow the user to use the keyboard to type into the textbox on screen
import pygame
from Resources.Curved import curve_shape
from Resources.Wrap_text import wrap_text
from pygame import *


class Text_Input:
    def __init__(self):
        self.text_colour = (255, 255, 255)
        self.text = ""
        self.font = "Rockwell"
        self.font_size = 20
        self.align = 0
        self.border_thickness = 0
        self.padding = [5, 5, 5, 5]
        # header, footer, margin_left, margin_right
        self.border_colour = (50, 50, 50)
        self.background_colour = (100, 100, 100)
        self.hover_colour = (100, 100, 100)
        self.active_colour = (100, 100, 100)
        # align must be 0, 1, 2 or 3
        self.rounded = False
        self.radius = 0.1
        self.header = ""
        self.header_align = "top"

        self._active = False
        self._type = "text"
        self._dimensions = [0, 0]
        self._position = [0, 0]
        self._hover = False
        self._type = "text_input"

    def assign_dimensions(self, dimensions):
        """The provided size_hint is only advisory as certain layouts may manipulate dimensions in different ways
        Therefore the dimensions are set by the layout object itself rather than the user or widget"""

        self._dimensions = dimensions

    def assign_position(self, position):
        """The provided pos_hint is only advisory as certain layouts may align and place widgets in different ways
        Therefore the position is set by the layout object itself rather than the user or widget"""

        self._position = position

    def _mouse_over(self, pos):
        """This requires the position of the mouse which can be accessed through pygame. This will be provided by
        the draw or mouse_click methods which will in turn receive it from the app.py program"""

        if self._position[0] < pos[0] < (self._position[0] + self._dimensions[0]):
            if self._position[1] < pos[1] < (self._position[1] + self._dimensions[1]):
                self._hover = True
            else:
                self._hover = False
        else:
            self._hover = False

    def mouse_click(self, pos):
        if self._hover:
            self._active = True
            return True
        else:
            self._active = False
            return False

    def _update(self, event):
        if self._active:
            if event.key == K_BACKSPACE:
                self.text = self.text.rstrip(self.text[-1])
            elif event.key == K_RETURN:
                self.text += " ¦ "
            else:
                self.text += event.unicode

    def _draw_background(self, surface):
        if self._active:
            draw_colour = self.active_colour
        elif self._hover:
            draw_colour = self.hover_colour
        else:
            draw_colour = self.background_colour

        if not self.rounded:
            pygame.draw.rect(surface, self.border_colour,
                             [self._position[0], self._position[1], self._dimensions[0], self._dimensions[1]])

            pygame.draw.rect(surface, draw_colour,
                             [self._position[0] + self.border_thickness,
                              self._position[1] + self.border_thickness,
                              self._dimensions[0] - (self.border_thickness * 2),
                              self._dimensions[1] - (self.border_thickness * 2)])
        else:
            curved_border, pos = curve_shape(self.radius, [self._position[0], self._position[1], self._dimensions[0],
                                                           self._dimensions[1]],
                                             self.border_colour)
            surface.blit(curved_border, pos)

            curved_box, pos = curve_shape(self.radius,
                                          [self._position[0] + self.border_thickness,
                                           self._position[1] + self.border_thickness,
                                           self._dimensions[0] - (self.border_thickness * 2),
                                           self._dimensions[1] - (self.border_thickness * 2)],
                                          draw_colour
                                          )

            surface.blit(curved_box, pos)

    def draw(self, surface, pos):
        self._mouse_over(pos)
        self._draw_background(surface)

        padding = self.padding

        text = self.text
        color = self.text_colour
        rect = [self._position[0] + self.border_thickness + padding[2],
                self._position[1] + self.border_thickness + padding[0],
                self._dimensions[0] - (self.border_thickness * 2) - (padding[3] + padding[2]),
                self._dimensions[1] - (self.border_thickness * 2) - (padding[1] + padding[0])]

        font = pygame.font.SysFont(self.font, self.font_size)
        align = self.align

        wrap_text(surface, text, color, rect, font, align)
