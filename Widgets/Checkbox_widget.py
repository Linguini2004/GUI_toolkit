# This is one of the widgets
# This is a check box which can trigger a response or the state can be retrieved
import pygame
import os
from Resources.Curved import curve_shape
from Resources.Errors import *

class CheckBox:
    def __init__(self):
        # colour attributes:
        self.colour = (255, 255, 255)
        self.border_colour = (0, 0, 0)
        self.icon_colour = (0, 0, 0)
        self.header_colour = (0, 0, 0)

        # header_attributes:
        self.header_active = True
        self.header_text = ""
        self.header_orientation = "left"
        self.header_align = "center"
        self.header_font = "arial"
        self.header_font_size = 20
        self.header_spacing = 0.1

        # icon attributes:
        self.icon_type = "tick"
        self.icon_scale = 1

        # dimensions attributes:
        self.size_hint = [1, 1]
        self.pos_hint = [0, 0]
        self.box_size = 1
        self.box_align = "center"
        self.compressible = False
        self.rounded = False
        self.radius = 0.1
        self.border_thickness = 0

        # private attributes:
        self._type = "checkbox"
        self._hover = False
        self._pressed = False
        self._dimensions = [0, 0]
        self._total_dimensions = [0, 0]
        self._position = [0, 0]
        self._actual_position = [0, 0]
        self._action = None
        self._loaded_icon = None
        self._loaded_boxes = None
        self._loaded_pos = None
        self._loaded_header = None
        self._boxes_loaded = False
        self._box_rect = [0, 0, 0, 0]
        self._cwd = os.getcwd()

    def assign_dimensions(self, dimensions):
        """The provided size_hint is only advisory as certain layouts may manipulate dimensions in different ways
        Therefore the dimensions are set by the layout object itself rather than the user or widget"""

        self._dimensions = list(dimensions)

    def assign_position(self, position, actual_position):
        """The provided pos_hint is only advisory as certain layouts may align and place widgets in different ways
        Therefore the position is set by the layout object itself rather than the user or widget"""

        self._position = list(position)
        self._actual_position = list(actual_position)

    def _mouse_over(self, pos):
        """This requires the position of the mouse which can be accessed through pygame. This will be provided by
        the draw or mouse_click methods which will in turn receive it from the app.py program"""

        if self._actual_position[0] + self._box_rect[0] < pos[0] < (self._actual_position[0] + self._box_rect[0] + self._box_rect[2]):
            if self._actual_position[1] + self._box_rect[1] < pos[1] < (self._actual_position[1] + self._box_rect[1] + self._box_rect[3]):
                self._hover = True
            else:
                self._hover = False
        else:
            self._hover = False

    def mouse_click(self):
        if self._hover:
            if not self._pressed:
                self._pressed = True
            else:
                self._pressed = False
            return True
        else:
            return False

    def _load_icon(self, box_dim):
        while True:
            os.chdir(os.path.dirname(os.getcwd()))
            if "GUI_toolkit" in os.getcwd()[-12:]:
                break

        path = os.path.abspath("Resources/Icons").replace(os.sep, "/")

        if self.icon_type == "tick":
            icon_path = os.path.join(path, "043-tick.png").replace(os.sep, "/")
        elif self.icon_type == "cross":
            icon_path = os.path.join(path, "016-cancel.png").replace(os.sep, "/")

        icon_to_draw = pygame.image.load(icon_path)
        os.chdir(self._cwd)

        icon_to_draw = pygame.transform.smoothscale(icon_to_draw, (int(box_dim[0]), int(box_dim[1])))
        icon_to_draw.fill(self.icon_colour, special_flags=pygame.BLEND_ADD)

        return icon_to_draw

    def _draw_icon(self, surface, box_pos, box_dim):
        icon_pos = list(box_pos)
        icon_dim = list(box_dim)

        if self.icon_type == "tick":
            icon_pos[0] -= self.border_thickness
            icon_pos[1] -= self.border_thickness * 3

            icon_dim[0] += self.border_thickness * 3
            icon_dim[1] += self.border_thickness * 3
        elif self.icon_type == "cross":
            icon_pos[0] += self.border_thickness * 1
            icon_pos[1] += self.border_thickness * 1

            icon_dim[0] -= self.border_thickness * 2
            icon_dim[1] -= self.border_thickness * 2

        if self._loaded_icon is None:
            self._loaded_icon = self._load_icon(icon_dim)

        surface.blit(self._loaded_icon, icon_pos)

    def _draw_header(self, surface, box_dim):
        if self.header_orientation == "left":
            max_width = self._dimensions[0] - box_dim[0] - (self.header_spacing * self._dimensions[0])
            if self._loaded_header is None:
                while True:
                    font = pygame.font.SysFont(self.header_font, self.header_font_size)
                    text = font.render(self.header_text, True, self.header_colour)
                    if text.get_width() > max_width:
                        self.header_font_size -= 1
                    else:
                        self._loaded_header = text
                        break

            x_coord = self._position[0]
            if self.header_align == "left":
                pass
            elif self.header_align == "right":
                x_coord += self._dimensions[0] - (box_dim[0] + (self.header_spacing * self._dimensions[0]) + self._loaded_header.get_width())
            else:
                available_width = self._dimensions[0] - (box_dim[0] + (self.header_spacing * self._dimensions[0]))
                x_coord += (available_width / 2) - (self._loaded_header.get_width() / 2)

            y_coord = self._position[1] + ((self._dimensions[1] / 2) - (self._loaded_header.get_height() / 2))

        else:
            max_width = self._dimensions[0]
            if self._loaded_header is None:
                while True:
                    font = pygame.font.SysFont(self.header_font, self.header_font_size)
                    text = font.render(self.header_text, True, self.header_colour)
                    if text.get_width() > max_width:
                        self.header_font_size -= 1
                    else:
                        self._loaded_header = text
                        break

            y_coord = self._position[1]
            x_coord = self._position[0]
            if self.header_align == "left":
                pass
            elif self.header_align == "right":
                x_coord += self._dimensions[0] - self._loaded_header.get_width()
            else:
                x_coord += (self._dimensions[0] / 2) - (self._loaded_header.get_width() / 2)

        surface.blit(self._loaded_header, (x_coord, y_coord))



    def draw(self, surface, pos, scroll_dif):
        """Surface is the window on which the widget will be drawn and is defined by the app.py program"""
        pos[1] -= scroll_dif
        self._mouse_over(pos)
        box_position = list(self._position)

        if self._dimensions[0] > self._dimensions[1]:
            box_height = self._dimensions[1] * self.box_size
            box_width = box_height
        else:
            box_width = self._dimensions[0] * self.box_size
            box_height = box_width

        box_position[1] += (self._dimensions[1] / 2) - (box_height / 2)
        box_dimensions = [box_width, box_height]

        if self.box_align == "left":
            pass
        elif self.box_align == "right":
            box_position[0] += (self._dimensions[0] - box_width)
        else:
            box_position[0] += (self._dimensions[0] / 2) - (box_width / 2)

        if self.header_active:
            self._draw_header(surface, box_dimensions)

        if self.header_orientation == "top":
            print("before:", box_position[1])
            box_position[1] -= (self._dimensions[1] / 2) - (box_height / 2)
            print("after:", box_position[1])
            header_height = self._loaded_header.get_height() + (self.header_spacing * self._dimensions[1])
            print("header height:", header_height)
            box_position[1] += header_height
            print("really after:", box_position[1])
        if not self.rounded:
            if self.border_thickness != 0:
                pygame.draw.rect(surface, self.border_colour,
                                 [box_position[0], box_position[1], box_dimensions[0], box_dimensions[1]])

            pygame.draw.rect(surface, self.colour,
                             [box_position[0] + self.border_thickness,
                              box_position[1] + self.border_thickness,
                              box_dimensions[0] - (self.border_thickness * 2),
                              box_dimensions[1] - (self.border_thickness * 2)])

            self._box_rect = [box_position[0] - self._position[0], box_position[1] - self._position[1], box_dimensions[0], box_dimensions[1]]
        else:
            if not self._boxes_loaded:
                curved_border, border_pos = curve_shape(self.radius,
                                                        [box_position[0], box_position[1], box_dimensions[0], box_dimensions[1]],
                                                        self.border_colour)

                box, box_pos = curve_shape(self.radius,
                                           [box_position[0] + self.border_thickness,
                                           box_position[1] + self.border_thickness,
                                           box_dimensions[0] - (self.border_thickness * 2),
                                           box_dimensions[1] - (self.border_thickness * 2)], self.colour)

                self._box_rect = [box_position[0] - self._position[0], box_position[1] - self._position[1], box_dimensions[0], box_dimensions[1]]
                self._loaded_boxes = (box, curved_border)
                self._loaded_pos = (box_pos, border_pos)
                self._boxes_loaded = True

            if self.border_thickness != 0:
                surface.blit(self._loaded_boxes[1], self._loaded_pos[1])

            surface.blit(self._loaded_boxes[0], self._loaded_pos[0])

        if self._pressed:
            self._draw_icon(surface, box_position, box_dimensions)




