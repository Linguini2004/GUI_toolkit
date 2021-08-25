# This is one of the widgets
# This widget will allow the user to use the keyboard to type into the textbox on screen
import pygame
from Resources.Curved import curve_shape
from Resources.Wrap_text import wrap_text
from Resources.Errors import PaddingError
from pygame import *


class Text_Input:
    def __init__(self):
        # colour attributes:
        self.border_colour = (0, 0, 0)
        self.background_colour = (100, 100, 100)
        self.hover_colour = (100, 100, 100)
        self.active_colour = (100, 100, 100)

        # text attributes:
        self.text = ""
        self.font = "arial"
        self.text_colour = (255, 255, 255)
        self.font_size = 20
        self.default_text = ""
        self.default_text_colour = (150, 150, 150)
        self.align = 0
        # align must be 0, 1, 2 or 3

        # dimension attributes:
        self.border_thickness = 0
        self.rounded = False
        self.radius = 0.1
        self.size_hint = [1, 1]
        self.pos_hint = [0, 0]
        self.compressible = True
        self.padding = [0, 0, 0, 0]
        # header, footer, margin_left, margin_right

        # header attributes:
        self.header_active = True
        self.header_text = ""
        self.header_align = "top"
        self.header_spacing = 0.01

        # private attributes:
        self._active = False
        self._act_padding = [0, 0, 0, 0]
        self._dimensions = [0, 0]
        self._position = [0, 0]
        self._actual_position = [0, 0]
        self._hover = False
        self._type = "text_input"
        self._total_dimensions = [0, 0]

    def assign_dimensions(self, dimensions):
        """The provided size_hint is only advisory as certain layouts may manipulate dimensions in different ways
        Therefore the dimensions are set by the layout object itself rather than the user or widget"""

        self._dimensions = list(dimensions)

        self._total_dimensions = list(dimensions)
        self._dimensions[0] = self._dimensions[0]# * self.size_hint[0]
        self._dimensions[1] = self._dimensions[1]# * self.size_hint[1]

        for pad in self.padding:
            if pad > 1:
                raise PaddingError("Padding can not be more than 100% of total size")

        self._act_padding[0] = self.padding[0] * self._dimensions[1]
        self._act_padding[1] = self.padding[1] * self._dimensions[1]
        self._act_padding[2] = self.padding[2] * self._dimensions[0]
        self._act_padding[3] = self.padding[3] * self._dimensions[0]

    def assign_position(self, position, actual_position):
        """The provided pos_hint is only advisory as certain layouts may align and place widgets in different ways
        Therefore the position is set by the layout object itself rather than the user or widget"""

        self._position = list(position)

        available_width = self._total_dimensions[0] - self._dimensions[0]
        available_height = self._total_dimensions[1] - self._dimensions[1]
        self._position[0] += (self.pos_hint[0] * available_width)
        self._position[1] += (self.pos_hint[1] * available_height)

        self._actual_position = list(actual_position)

        self._actual_position[0] += (self.pos_hint[0] * available_width)
        self._actual_position[1] += (self.pos_hint[1] * available_height)

    def _mouse_over(self, pos):
        """This requires the position of the mouse which can be accessed through pygame. This will be provided by
        the draw or mouse_click methods which will in turn receive it from the app.py program"""
        header_size = pygame.font.SysFont(self.font, self.font_size).render(self.header_text, False, (0, 0, 0)).get_size()
        spacing = self.header_spacing * self._dimensions[1]

        if self.header_align == "left":
            if (self._actual_position[0] + header_size[0] + spacing) < pos[0] < (self._actual_position[0] + self._dimensions[0]):
                if self._actual_position[1] < pos[1] < (self._actual_position[1] + self._dimensions[1]):
                    self._hover = True
                else:
                    self._hover = False
            else:
                self._hover = False

        if self.header_align == "top":
            if self._actual_position[0] < pos[0] < (self._actual_position[0] + self._dimensions[0]):
                if (self._actual_position[1] + header_size[1] + spacing) < pos[1] < (self._actual_position[1] + self._dimensions[1]):
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

    def update(self, event):
        if self._active:
            if event.key == K_BACKSPACE:
                self.text = self.text.rstrip(self.text[-1])
            elif event.key == K_RETURN:
                self.text += " ¦ "
            else:
                self.text += event.unicode

    def _draw_header(self, surface, font, color):
        surface.blit(font.render(self.header_text, True, color), ((self._position[0]), self._position[1]))

    def _draw_default_text(self, surface, text, color, rect, font, align):
        wrap_text(surface, text, color, rect, font, align)

    def _draw_background(self, surface, modified_pos, modified_dim):
        if self._active:
            draw_colour = self.active_colour
        elif self._hover:
            draw_colour = self.hover_colour
        else:
            draw_colour = self.background_colour

        if not self.rounded:
            if self.border_thickness != 0:
                pygame.draw.rect(surface, self.border_colour,
                                [modified_pos[0], modified_pos[1], modified_dim[0], modified_dim[1]])

            pygame.draw.rect(surface, draw_colour,
                             [modified_pos[0] + self.border_thickness,
                              modified_pos[1] + self.border_thickness,
                              modified_dim[0] - (self.border_thickness * 2),
                              modified_dim[1] - (self.border_thickness * 2)])
        else:
            if self.border_thickness != 0:
                curved_border, pos = curve_shape(self.radius, [modified_pos[0], modified_pos[1], modified_dim[0],
                                                            modified_dim[1]],
                                                self.border_colour)
                surface.blit(curved_border, pos)

            curved_box, pos = curve_shape(self.radius,
                                          [modified_pos[0] + self.border_thickness,
                                           modified_pos[1] + self.border_thickness,
                                           modified_dim[0] - (self.border_thickness * 2),
                                           modified_dim[1] - (self.border_thickness * 2)],
                                          draw_colour
                                          )

            surface.blit(curved_box, pos)

    def draw(self, surface, pos):
            self._mouse_over(pos)
            padding = self._act_padding
            
            box_position = list(self._position)
            box_dimensions = list(self._dimensions)

            font = pygame.font.SysFont(self.font, self.font_size)
            text = self.text
            color = self.text_colour
            align = self.align
            spacing = self.header_spacing * self._dimensions[1]

            if self.header_active:
                if self.header_align == "top":
                    box_position[1] += font.render("H", False, color).get_height() + spacing
                    box_dimensions[1] -= font.render("H", False, color).get_height() + spacing

                elif self.header_align == "left":
                    box_position[0] += (font.render(self.header_text, False, color).get_width() + spacing)
                    box_dimensions[0] -= (font.render(self.header_text, False, color).get_width() + spacing)

                self._draw_header(surface, font, color)
            
            # passing through the modified params as to not modify the widgets own position and dimensions
            self._draw_background(surface, box_position, box_dimensions)
            
            rect = [box_position[0] + self.border_thickness + padding[2],
                    box_position[1] + self.border_thickness + padding[0],
                    box_dimensions[0] - (self.border_thickness * 2) - (padding[3] + padding[2]),
                    box_dimensions[1] - (self.border_thickness * 2) - (padding[1] + padding[0])]

            if self.default_text != "" and self.text == "":
                self._draw_default_text(surface, self.default_text, self.default_text_colour, rect, font, align)

            wrap_text(surface, text, color, rect, font, align)





