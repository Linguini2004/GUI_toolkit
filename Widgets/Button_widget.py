# This is one of the widgets
# This is a button which initiates a response when clicked
# Eventually you will be able to modify all aspects of the button such as image and texture
import pygame
import os
from Resources.Curved import curve_shape
from Resources.Image_size import adaptive_image_proportion
from Resources.Image_size import image_proportion
#from Resources.Errors import PaddingError, Icon_Error
from Resources.Errors import *
import time

class Button:
    def __init__(self):
        # colour attributes:
        self.colour = (50, 50, 50)
        self.hover_colour = (50, 50, 50)
        self.pressed_colour = (50, 50, 50)
        self.text_colour = (255, 255, 255)

        # text attributes:
        self.text = ""
        self.font = "arial"
        self.font_size = 20
        self.text_spacing = 0.05
        self.text_align = "centre"
        # default center, can be left, centre/er, or right

        # dimension attributes:
        self.size_hint = [1, 1]
        self.pos_hint = [0, 0]
        self.compressible = True
        self.rounded = False
        self.radius = 0.1

        # image attributes:
        self.display_image = False
        self.just_image = False
        self.image_path = ""
        self.keep_proportion = True
        self.scale_image = 1
        self.image_spacing = 0.01
        # 0 to 1 (0 to 100% of maximum possible size)
        self.image_padding = [0, 0, 0.1, 0.1]
        # relative sizes [header, footer, left margin, right margin]
        self.image_align = ""
        # default none, can be left, center/re, or right

        # icon attributes:
        self.display_icon = False
        self.icon_name = ""
        self.icon_path = ""
        self.icon_spacing = 0.1
        self.icon_scale = 1
        self.icon_colour = (0, 0, 0)
        self.icon_align = "center"
        # left, right, center

        # private attributes:
        self._type = "button"
        self._hover = False
        self._pressed = False
        self._pressed_timeout = 20
        self._dimensions = [0, 0]
        self._total_dimensions = [0, 0]
        self._position = [0, 0]
        self._actual_position = [0, 0]
        self._action = None
        self._previous_image = None
        self._loaded_image = None
        self._loaded_icon = None
        self._loaded_buttons = None
        self._button_position = None
        self._action_args = None
        self._button_text = None
        self._text_loaded = False
        self._cwd = os.getcwd()

    def assign_dimensions(self, dimensions):
        """The provided size_hint is only advisory as certain layouts may manipulate dimensions in different ways
        Therefore the dimensions are set by the layout object itself rather than the user or widget"""

        self._dimensions = list(dimensions)

        '''
        self._total_dimensions = list(dimensions)
        #self._dimensions[0] = self._dimensions[0]# * self.size_hint[0]
        #self._dimensions[1] = self._dimensions[1]# * self.size_hint[1]
        '''

    def assign_position(self, position, actual_position):
        """The provided pos_hint is only advisory as certain layouts may align and place widgets in different ways
        Therefore the position is set by the layout object itself rather than the user or widget"""

        self._position = list(position)
        self._actual_position = list(actual_position)

        '''
        self._position = list(position)

        available_width = self._total_dimensions[0] - self._dimensions[0]
        available_height = self._total_dimensions[1] - self._dimensions[1]
        print("AVAILABLE", available_width, available_height)
        self._position[0] += (self.pos_hint[0] * available_width)
        self._position[1] += (self.pos_hint[1] * available_height)

        self._actual_position = list(actual_position)

        self._actual_position[0] += (self.pos_hint[0] * available_width)
        self._actual_position[1] += (self.pos_hint[1] * available_height)
        '''

    def _mouse_over(self, pos):
        """This requires the position of the mouse which can be accessed through pygame. This will be provided by
        the draw or mouse_click methods which will in turn receive it from the app.py program"""

        if self._actual_position[0] < pos[0] < (self._actual_position[0] + self._dimensions[0]):
            if self._actual_position[1] < pos[1] < (self._actual_position[1] + self._dimensions[1]):
                self._hover = True
            else:
                self._hover = False
        else:
            self._hover = False

    def mouse_click(self):
        if self._hover:
            self._pressed = True
            return True

    def _load_image(self):
        image_to_draw = pygame.image.load(self.image_path)
        return image_to_draw

    def _load_icon(self):
        while True:
            os.chdir(os.path.dirname(os.getcwd()))
            if "GUI_toolkit" in os.getcwd()[-12:]:
                break
            #else:
            #    os.chdir(os.path.dirname(os.getcwd()))

        if self.icon_name != "":
            found = False
            icon_paths = "Resources/Icons"
            icon_paths = os.path.abspath(icon_paths).replace(os.sep, "/")
            for icon in os.listdir(icon_paths):
                if icon.strip(".png")[4:] == self.icon_name:
                    icon_path = os.path.join(icon_paths, icon).replace(os.sep, "/")
                    found = True

            if not found:
                raise Icon_Error("The selected icon does not exist")

        else:
            try:
                icon_path = self.icon_path
            except FileNotFoundError:
                raise Icon_Error("The given icon path does not exist")

        icon_to_draw = pygame.image.load(icon_path)
        os.chdir(self._cwd)

        icon_to_draw.fill(self.icon_colour, special_flags=pygame.BLEND_ADD)

        return icon_to_draw

    def _draw_icon(self, surface):
        if self._loaded_icon is None:
            self._loaded_icon = self._load_icon()

        icon_to_draw = self._loaded_icon
        icon_position = list(self._position)

        if self._dimensions[0] > self._dimensions[1]:
            icon_height = (self._dimensions[1] - ((self.icon_spacing * self._dimensions[1]) * 2)) * self.icon_scale
            icon_width = icon_height
        else:
            icon_width = (self._dimensions[0] - ((self.icon_spacing * self._dimensions[0]) * 2)) * self.icon_scale
            icon_height = icon_width

        icon_position[1] += (self._dimensions[1] / 2) - (icon_height / 2)

        if self.icon_align == "left":
            icon_position[0] += self.icon_spacing * self._dimensions[0]
            if self.text != "":
                width = self._dimensions[0] - (icon_width + (self.icon_spacing * self._dimensions[0]))
                self._draw_text(surface, self.text_align, [icon_position[0] + icon_width, self._position[1]], [width, self._dimensions[1]])

        elif self.icon_align == "right":
            icon_position[0] = (icon_position[0] + self._dimensions[0]) - ((self.icon_spacing * self._dimensions[0]) + icon_width)
            if self.text != "":
                width = self._dimensions[0] - (icon_width + (self.icon_spacing * self._dimensions[0]))
                self._draw_text(surface, self.text_align, [self._position[0], self._position[1]], [width, self._dimensions[1]])

        else:
            icon_position[0] += ((self._dimensions[0] / 2) - (icon_width / 2))
            if self.text != "":
                raise Button_Error("You cannot currently have text and an icon in a button if the button is not left or right aligned")

        image_to_draw = pygame.transform.smoothscale(icon_to_draw, (int(icon_width), int(icon_height)))

        surface.blit(image_to_draw, (icon_position[0], icon_position[1]))

    def _draw_image(self, surface):
        if self.image_path != self._previous_image:
            self._image_loaded = False

        self._previous_image = self.image_path

        if self._loaded_image is None:
            self._loaded_image = self._load_image()

        image_to_draw = self._loaded_image

        width = image_to_draw.get_width()
        height = image_to_draw.get_height()
        image_position = list(self._position)
        image_position[0] += self.image_padding[2] * self._dimensions[0]
        image_position[1] += self.image_padding[0] * self._dimensions[1]

        for i in self.image_padding:
            if i > 1:
                raise PaddingError("Padding must be between 0 and 1")

        adjustments = [self.image_padding[0] * self._dimensions[1],
                       self.image_padding[1] * self._dimensions[1],
                       self.image_padding[2] * self._dimensions[0],
                       self.image_padding[3] * self._dimensions[0]]

        image_dimensions = list(self._dimensions)
        image_spacing = self.image_spacing * self._dimensions[0]

        if self.keep_proportion:
            if self.image_align != "":
                image_to_draw = image_proportion(width, height, image_dimensions, image_to_draw, self.scale_image)
                image_position[1] += (self._dimensions[1] / 2) - (image_to_draw.get_height() / 2)

                if self.image_align == "left":
                    image_position[0] = self._position[0] + image_spacing
                elif self.image_align == "right":
                    image_position[0] = (self._position[0] + self._dimensions[0]) - (image_to_draw.get_width() + image_spacing)
                else:
                    image_position[0] = self._position[0] + ((self._dimensions[0] / 2) - (image_to_draw.get_width() / 2))

            else:
                image_to_draw = adaptive_image_proportion(width, height, image_position, image_dimensions, adjustments, image_to_draw, self.scale_image)
        else:
            image_to_draw = pygame.transform.smoothscale(image_to_draw, (int(image_dimensions[0]), int(image_dimensions[1])))

        surface.blit(image_to_draw, (image_position[0], image_position[1]))

    def _draw_text(self, surface, text_align, position, dimensions):
        spacing = self.text_spacing * dimensions[0]

        if self._button_text is None:
            while True:
                font = pygame.font.SysFont(self.font, self.font_size)
                b_text = font.render(self.text, True, self.text_colour)
                if (spacing * 2) + b_text.get_width() > dimensions[0]:
                    self.font_size -= 1
                else:
                    self._button_text = b_text
                    break

        b_text = self._button_text

        if text_align == "left":
            x_coord = position[0] + spacing
        elif text_align == "right":
            x_coord = (position[0] + dimensions[0]) - (b_text.get_width() + spacing)
        else:
            x_coord = position[0] + (dimensions[0] / 2 - b_text.get_width() / 2)

        y_coord = position[1] + (dimensions[1] / 2 - b_text.get_height() / 2)

        surface.blit(b_text, (x_coord, y_coord))

    def draw(self, surface, pos, scroll_dif):
        """Surface is the window on which the widget will be drawn and is defined by the app.py program"""
        pos[1] -= scroll_dif
        self._mouse_over(pos)

        if self._pressed and self._pressed_timeout > 0:
            draw_colour = self.pressed_colour
            self._pressed_timeout -= 1
            if self._pressed_timeout <= 0:
                self._pressed = False
                self._pressed_timeout = 20
        elif self._hover:
            draw_colour = self.hover_colour
        else:
            draw_colour = self.colour

        if not self.just_image:
            if not self.rounded:
                pygame.draw.rect(surface,
                                 draw_colour,
                                 [self._position[0], self._position[1], self._dimensions[0], self._dimensions[1]]
                                 )
            else:
                if self._loaded_buttons is None:
                    default_button, hover_button, pressed_button, button_pos = self.load_curved_buttons(
                        self.radius, (self._position[0], self._position[1], self._dimensions[0], self._dimensions[1])
                    )
                    self._loaded_buttons = (default_button, hover_button, pressed_button)
                    self._button_position = button_pos

                if self._pressed:
                    surface.blit(self._loaded_buttons[2], self._button_position)
                elif self._hover:
                    surface.blit(self._loaded_buttons[1], self._button_position)
                else:
                    surface.blit(self._loaded_buttons[0], self._button_position)

        if self.text != "" and self.display_image:
            raise Button_Error("You cannot currently display an image and text within a button")

        if self.display_image and self.display_icon:
            raise Button_Error("You cannot currently display an image and an icon within a button")

        if self.display_image:
            self._draw_image(surface)

        if self.display_icon:
            self._draw_icon(surface)
        elif self.text != "":
            self._draw_text(surface, self.text_align, self._position, self._dimensions)

    def load_curved_buttons(self, radius, rect_dimensions):
        default_button, pos = curve_shape(radius, rect_dimensions, self.colour)
        hover_button, pos = curve_shape(radius, rect_dimensions, self.hover_colour)
        pressed_button, pos = curve_shape(radius, rect_dimensions, self.pressed_colour)

        return (default_button, hover_button, pressed_button, pos)

    def bind(self, function, *args):
        self._action = function
        print("function", function)
        self._action_args = args

    def action(self):
        if self._action is not None:
            self._action(self, *self._action_args)
        else:
            print("No action bound")
