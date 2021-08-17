# This is one of the widgets
# This is a simple button which initiates a response when clicked
# Eventually you will be able to modify all aspects of the button such as image and texture
import pygame
import os
from Resources.Curved import curve_shape
from Resources.Image_size import adaptive_image_proportion
from Resources.Errors import PaddingError, Icon_Error

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

        # dimension attributes:
        self.size_hint = [1, 1]
        self.pos_hint = ""
        self.rounded = False
        self.radius = 0.1
        self.image_padding = [0, 0, 0, 0]
        # relative sizes [header, footer, left margin, right margin]

        # image attributes:
        self.display_image = False
        self.just_image = False
        self.image_path = ""
        self.keep_proportion = True
        self.scale_image = 1
        # 0 to 1 (0 to 100% of maximum possible size)

        # icon attributes:
        self.display_icon = False
        self.icon_name = ""
        self.icon_path = ""
        self.icon_align = "center"
        self.icon_spacing = 0.1
        self.icon_scale = 1
        self.icon_colour = (0, 0, 0)
        # left, right, center

        # private attributes:
        self._type = "button"
        self._hover = False
        self._pressed = False
        self._pressed_timeout = 20
        self._dimensions = [0, 0]
        self._position = [0, 0]
        self._action = None
        self._previous_image = None
        self._loaded_image = None
        self._image_loaded = False
        self._loaded_icon = None
        self._icon_loaded = False
        self._action_args = None
        self._cwd = os.getcwd()

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
            self._pressed = True
            return True

    def _load_image(self):
        image_to_draw = pygame.image.load(self.image_path)
        return image_to_draw

    def _load_icon(self):
        while True:
            os.chdir(os.path.dirname(os.getcwd()))
            if "GUI_toolkit" in os.getcwd()[12:]:
                break
            else:
                os.chdir(os.path.dirname(os.getcwd()))

        if self.icon_name != "":
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
        if not self._icon_loaded:
            self._loaded_icon = self._load_icon()
            self._icon_loaded = True

        icon_to_draw = self._loaded_icon
        icon_position = list(self._position)

        icon_height = (self._dimensions[1] - ((self.icon_spacing * self._dimensions[1]) * 2)) * self.icon_scale
        icon_width = icon_height
        icon_position[1] += (self._dimensions[1] / 2) - (icon_height / 2)

        if self.icon_align == "left":
            icon_position[0] += self.icon_spacing * self._dimensions[0]
        elif self.icon_align == "right":
            icon_position[0] = (icon_position[0] + self._dimensions[0]) - (self.icon_spacing * self._dimensions[0])
        else:
            icon_position[0] += ((self._dimensions[0] / 2) - (icon_width / 2))

        image_to_draw = pygame.transform.smoothscale(icon_to_draw, (int(icon_width), int(icon_height)))

        surface.blit(image_to_draw, (icon_position[0], icon_position[1]))

    def _draw_image(self, surface):
        if self.image_path != self._previous_image:
            self._image_loaded = False

        self._previous_image = self.image_path

        if not self._image_loaded:
            self._loaded_image = self._load_image()
            self._image_loaded = True

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

        if self.keep_proportion:
            image_to_draw = adaptive_image_proportion(width, height, image_position, image_dimensions, adjustments, image_to_draw, self.scale_image)
        else:
            image_to_draw = pygame.transform.smoothscale(image_to_draw, (int(image_dimensions[0]), int(image_dimensions[1])))

        surface.blit(image_to_draw, (image_position[0], image_position[1]))

    def draw(self, surface, pos):
        """Surface is the window on which the widget will be drawn and is defined by the app.py program"""
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
                curved_rectangle, pos = curve_shape(self.radius, (self._position[0], self._position[1], self._dimensions[0], self._dimensions[1]), draw_colour)
                surface.blit(curved_rectangle, pos)

            if self.text != "":
                font = pygame.font.SysFont(self.font, self.font_size)
                b_text = font.render(self.text, True, self.text_colour)
                x_coord = self._position[0] + (self._dimensions[0] / 2 - b_text.get_width() / 2)
                y_coord = self._position[1] + (self._dimensions[1] / 2 - b_text.get_height() / 2)
                surface.blit(b_text, (x_coord, y_coord))

        if self.display_image:
            self._draw_image(surface)
        elif self.display_icon:
            self._draw_icon(surface)

    def bind(self, function, *args):
        self._action = function
        self._action_args = args

    def action(self):
        if self._action is not None:
            self._action(self, *self._action_args)
        else:
            print("NoActionBound")
