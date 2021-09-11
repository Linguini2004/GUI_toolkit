# Layouts contain widgets such as buttons and text boxes
# Depending on the type of layout, widgets can be arranged in different ways
# The grid layout allows for widgets to be assigned to certain sectors within the layout
import pygame
import time
from Resources.Errors import *

class GridLayout:
    def __init__(self):
        # config attributes:
        self.size = (2, 3)
        self.background_colour = (0, 0, 0)
        self.widget_spacing = 0.025
        self.scroll_enabled = False
        self.scroll_speed = 8
        self.padding = [0, 0, 0, 0]
        # padding = [header, footer, left_margin, right_margin] must be 0 to 1
        self.real_size = 1
        # if scroll is enabled then the real size determines how tall the layout actually is relative to its
        # on-screen size where 1 is 1x the size (must be greater than 1)

        # private attributes:
        self._widgets = []
        self._dimensions = [0, 0]
        self._position = [0, 0]
        self._actual_position = []
        self._layout_width = 0
        self._layout_height = 0
        self._act_padding = [0, 0, 0, 0]
        self._act_spacing = 0
        self._scroll_progressions = 0
        self._scroll_direction = 0
        self._scroll_amount = 0
        self._widget_assigned = False
        self._intermediate = None


    def assign_dimensions(self, dimensions):
        """With the option of having multiple layouts on one screen, it must be the app.py
        program that assigns the dimensions of the layout as the layout itself is unaware of
        other layouts"""

        if self.real_size < 1:
            raise Layout_Error("Real size must be larger than the layout itself (hence must be more than 1)")

        if not self.scroll_enabled:
            self.real_size = 1

        self._dimensions = dimensions
        self._layout_width = self._dimensions[0]
        self._layout_height = self._dimensions[1] * self.real_size

        self._intermediate = pygame.surface.Surface((self._layout_width, self._layout_height))

        for pad in self.padding:
            if pad > 1:
                raise PaddingError("Padding must range between 0 and 1")

        self._act_padding[0] = self.padding[0] * self._layout_height
        self._act_padding[1] = self.padding[1] * self._layout_height
        self._act_padding[2] = self.padding[2] * self._layout_width
        self._act_padding[3] = self.padding[3] * self._layout_width

        if self.widget_spacing > 1:
            raise Spacing_Error("Spacing must range between 0 and 1")
        self._act_spacing = self.widget_spacing * self._dimensions[0]

    def assign_position(self, position):
        """With the option of having multiple layouts on one screen, it must be the app.py
        program that assigns the position of the layout (based on the top left corner) as the layout
        itself is unaware of other layouts"""

        self._actual_position = list(position)
        self._position = [0, 0]
        if not self._widget_assigned:
            self._align()
            self._update_widgets()
            self._widget_assigned = True

    def scroll(self, mouse_button):
        if mouse_button == 5 and self._scroll_amount > (self._layout_height - (self._layout_height / self.real_size)) * -1:
            self._scroll_progressions = 10
            self._scroll_direction = -1
        if mouse_button == 4 and self._scroll_amount < 0:
            self._scroll_progressions = 10
            self._scroll_direction = 1
