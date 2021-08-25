# Layouts contain widgets such as buttons and text boxes
# Depending on the type of layout, widgets can be arranged in different ways
# The box layout allows for widgets to be stacked vertically or horizontally
import pygame
import time
from Resources.Errors import *

class BoxLayout:
    def __init__(self):
        # config attributes
        self.mode = "horizontal"
        self.background_colour = (0, 0, 0)
        self.widget_spacing = 0.025
        self.scroll_enabled = False
        self.merge_scroll = False
        self.padding = [0, 0, 0, 0]
        # padding = [header, footer, left_margin, right_margin] must be 0 to 1
        self.real_size = 1
        # if scroll is enabled then the real size determines how tall the layout actually is relative to its
        # on-screen size where 1 is 1x the size (must be greater than 1)

        # private attributes:
        self._widgets = []
        self._num_widgets = 0
        self._widget_width = 0
        self._widget_height = 0
        self._widget_coords = []
        self._widget_dimensions = []
        self._dimensions = [400, 600]
        self._actual_position = []
        self._actual_widget_coords = []
        self._position = [0, 0]
        self._layout_width = 0
        self._layout_height = 0
        self._scroll_amount = 0
        self._act_padding = [0, 0, 0, 0]
        self._widget_adjust = False
        self._widget_assigned = False
        #self._intermediate = None

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
            self._scroll_amount -= 15
        if mouse_button == 4 and self._scroll_amount < 0:
            self._scroll_amount += 15

    def active(self, mouse_pos):
        pass

    def add_widget(self, widget: object):
        self._widgets.append(widget)
        self._num_widgets += 1

    def _align(self):
        self._widget_coords = []
        self._widget_dimensions = []

        usable_width = self._layout_width - (self._act_padding[2] + self._act_padding[3])
        usable_height = self._layout_height - (self._act_padding[0] + self._act_padding[1])
        padding = self._act_padding

        if self._num_widgets > 0:
            '''
            if self.mode == "horizontal":
                self._widget_width = (usable_width - (self._act_spacing * (self._num_widgets + 1))) / self._num_widgets
                self._widget_height = usable_height - (self._act_spacing * 2)

                for i in range(len(self._widgets)):
                    x_coord = (padding[2] + (self._act_spacing * (i + 1)) + (i * self._widget_width)) + self._position[0]
                    y_coord = (padding[0] + self._act_spacing) + self._position[1]
                    self._widget_coords.append([x_coord, y_coord])
                    
            space_freed = [0]
            default_width = usable_width - (self._act_spacing * 2)
            default_height = (usable_height - (self._act_spacing * (self._num_widgets + 1))) / self._num_widgets
            for i, widget in enumerate(self._widgets):
                available_width = default_width - (widget.size_hint[0] * default_width)
                available_height = default_height - (widget.size_hint[1] * default_height)
                reduced_width = (widget.size_hint[0] * default_width)
                reduced_height = (widget.size_hint[1] * default_height)
                self._widget_dimensions.append([reduced_width, reduced_height])
                x_coord = ((padding[2] + self._act_spacing) + self._position[0]) + (available_width * self._widgets[i].pos_hint[0])
                y_coord = padding[0] + sum(space_freed) + (self._act_spacing * (i + 1)) + (sum([coord[1] for coord in self._widget_dimensions[:i]])) + (available_height * self._widgets[i].pos_hint[1])
                #space_freed.append((default_height - reduced_height) * widget.pos_hint[1])
                #print("space free", space_freed)

                if widget.compressible:
                    space_freed.append((default_height - reduced_height) * widget.pos_hint[1])
                else:
                    print("HELLO")
                    space_freed.append(default_height - reduced_height)

                self._widget_coords.append([x_coord, y_coord])
            '''
            if self.mode == "horizontal":
                #print("HERE")
                space_freed = [0]
                default_width = (usable_width - (self._act_spacing * (self._num_widgets + 1))) / self._num_widgets
                default_height = usable_height - (self._act_spacing * 2)
                for i, widget in enumerate(self._widgets):
                    available_width = default_width - (widget.size_hint[0] * default_width)
                    available_height = default_height - (widget.size_hint[1] * default_height)
                    reduced_width = (widget.size_hint[0] * default_width)
                    reduced_height = (widget.size_hint[1] * default_height)
                    self._widget_dimensions.append([reduced_width, reduced_height])
                    x_coord = padding[2] + sum(space_freed) + (self._act_spacing * (i + 1)) + (sum([coord[0] for coord in self._widget_dimensions[:i]])) + (available_width * self._widgets[i].pos_hint[0])
                    y_coord = ((padding[0] + self._act_spacing) + self._position[1]) + (available_height * self._widgets[i].pos_hint[1])

                    if widget.compressible:
                        space_freed.append((default_width - reduced_width) * widget.pos_hint[0])
                    else:
                        space_freed.append(default_width - reduced_width)

                    self._widget_coords.append([x_coord, y_coord])

            elif self.mode == "vertical":
                space_freed = [0]
                default_width = usable_width - (self._act_spacing * 2)
                default_height = (usable_height - (self._act_spacing * (self._num_widgets + 1))) / self._num_widgets
                for i, widget in enumerate(self._widgets):
                    available_width = default_width - (widget.size_hint[0] * default_width)
                    available_height = default_height - (widget.size_hint[1] * default_height)
                    reduced_width = (widget.size_hint[0] * default_width)
                    reduced_height = (widget.size_hint[1] * default_height)
                    self._widget_dimensions.append([reduced_width, reduced_height])
                    x_coord = ((padding[2] + self._act_spacing) + self._position[0]) + (available_width * self._widgets[i].pos_hint[0])
                    y_coord = padding[0] + sum(space_freed) + (self._act_spacing * (i + 1)) + (sum([coord[1] for coord in self._widget_dimensions[:i]])) + (available_height * self._widgets[i].pos_hint[1])

                    if widget.compressible:
                        space_freed.append((default_height - reduced_height) * widget.pos_hint[1])
                    else:
                        space_freed.append(default_height - reduced_height)

                    self._widget_coords.append([x_coord, y_coord])

                '''
                for i in range(len(self._widgets)):
                    x_coord = ((padding[2] + self._act_spacing) + self._position[0]) + (available_width * self._widgets[i].pos_hint[0])
                    #y_coord = ((padding[0] + (self._act_spacing * (i + 1)) + (i * self._widget_dimensions[i][1])) + self._position[1]) - space_freed[i]
                    y_coord = padding[0] + (self._act_spacing * (i + 1)) + (sum([coord[1] for coord in self._widget_dimensions[:i]])) + (available_height * self._widgets[i].pos_hint[1])
                    #y_coord = ((padding[0] + (self._act_spacing * (i + 1)) + (i * self._widget_height)) + self._position[1])
                    self._widget_coords.append([x_coord, y_coord])
                    
                '''

        '''
        total_free_space = 0
        for widget in self.widgets:
            self._widget_width = usable_width - (self.act_spacing * 2)
            default_height = (usable_height - (self._act_spacing * (self._num_widgets + 1))) / self._num_widgets
            available_height = default_height - (widget.size_hint[1] * default_height)
            if widget.size_hint != [1, 1]:
                if default_height > (widget.size_hint[1] * default_height) + (self.pos_hint[1] * available_height):
                    reduced_height = default_height - (widget.size_hint[1] * default_height) + (self.pos_hint[1] * available_height)
        '''

    def _update_widgets(self):
        self._actual_widget_coords = []
        for widget_coords in self._widget_coords:
            self._actual_widget_coords.append([widget_coords[0] + self._actual_position[0], widget_coords[1] + self._actual_position[1]])

        for i, widget in enumerate(self._widgets):
            previous_coords = 0
            #widget.assign_dimensions((self._widget_width, self._widget_height))
            #print("dimensions before assign", self._widget_dimensions)
            widget.assign_dimensions(self._widget_dimensions[i])
            widget.assign_position(self._widget_coords[i], self._actual_widget_coords[i])

            '''
            print("before", self._widget_coords[1][1])

            for coords in self._widget_coords[:i+1]:
                previous_coords += coords[1]
                free_space = (previous_coords + widget._total_dimensions[1]) - (
                            widget._position[1] + widget._dimensions[1])

            if not self._widget_adjust:
                print(free_space)
                self._widget_coords[i+1][1] -= free_space

            print("after", self._widget_coords[1][1])

            self._widget_adjust = True/
            
            if not self._widget_adjust:
                if widget._position[1] + widget._dimensions[1] < (previous_coords + widget._total_dimensions[1]):
                    free_space = (previous_coords + widget._total_dimensions[1]) - (widget._position[1] + widget._dimensions[1])
                    for coords in self._widget_coords[:i+1]:
                        print("before", coords[1])
                        coords[1] -= free_space
                        print("after", coords[1])
            
            '''

        #self._widget_adjust = True

                #self._widget_coords[i][1]


    def draw(self, surface, mouse_pos):
        self._draw_background()
        self._draw_widgets(mouse_pos)
        self._draw_self(surface)

    def _draw_background(self):
        pygame.draw.rect(self._intermediate, self.background_colour, [self._position[0], self._position[1], self._layout_width, self._layout_height])

    def _draw_widgets(self, mouse_pos):
        for widget in self._widgets:
            widget.draw(self._intermediate, mouse_pos)

    def _draw_self(self, surface):
        surface.blit(self._intermediate, (self._position[0], self._position[1] + self._scroll_amount))

    def provide_widgets(self):
        return self._widgets
        # return dict(zip(self._widgets, self._widget_coords))
