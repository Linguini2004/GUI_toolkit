# This is one of the widgets
# This is a simple button which initiates a response when clicked
# Eventually you will be able to modify all aspects of the button such as image and texture
import pygame
from pygame import *

class Button:
    def __init__(self):
        self.colour = (50, 50, 50)
        self.hover_colour = (50, 50, 50)
        self.pressed_colour = (50, 50, 50)
        self.text = ""
        self.text_colour = (255, 255, 255)
        self.size_hint = [1, 1]
        self.pos_hint = ""
        self.font = "Rockwell"
        self.font_size = 20
        self.rounded = True
        self.radius = 0.1

        self._type = "button"
        self._hover = False
        self._pressed = False
        self._pressed_timeout = 20
        self._dimensions = [0, 0]
        self._position = [0, 0]
        self._action = None

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
        if not self.rounded:
            pygame.draw.rect(surface,
                             draw_colour,
                             [self._position[0], self._position[1], self._dimensions[0], self._dimensions[1]],
                             5,
                             5
                             )
        else:
            radius = self.radius
            rect = Rect((self._position[0], self._position[1], self._dimensions[0], self._dimensions[1]))
            color = Color(*draw_colour)
            alpha = color.a
            color.a = 0
            pos = rect.topleft
            rect.topleft = 0, 0
            rectangle = Surface(rect.size, SRCALPHA)

            circle = Surface([min(rect.size) * 3] * 2, SRCALPHA)
            draw.ellipse(circle, (0, 0, 0), circle.get_rect(), 0)
            circle = transform.smoothscale(circle, [int(min(rect.size) * radius)] * 2)

            radius = rectangle.blit(circle, (0, 0))
            radius.bottomright = rect.bottomright
            rectangle.blit(circle, radius)
            radius.topright = rect.topright
            rectangle.blit(circle, radius)
            radius.bottomleft = rect.bottomleft
            rectangle.blit(circle, radius)

            rectangle.fill((0, 0, 0), rect.inflate(-radius.w, 0))
            rectangle.fill((0, 0, 0), rect.inflate(0, -radius.h))

            rectangle.fill(color, special_flags=BLEND_RGBA_MAX)
            rectangle.fill((255, 255, 255, alpha), special_flags=BLEND_RGBA_MIN)

            surface.blit(rectangle, pos)

        if self.text != "":
            font = pygame.font.SysFont(self.font, self.font_size)
            b_text = font.render(self.text, True, self.text_colour)
            x_coord = self._position[0] + (self._dimensions[0] / 2 - b_text.get_width() / 2)
            y_coord = self._position[1] + (self._dimensions[1] / 2 - b_text.get_height() / 2)
            surface.blit(b_text, (x_coord, y_coord))

    def bind(self, Application, method):
        self._action = getattr(Application, method)

    def action(self):
        if self._action is not None:
            self._action(self)
        else:
            print("NoActionBound")
