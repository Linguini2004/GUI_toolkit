# The purpose of this program is to act as a foundation for the application
# This involves drawing everything to the screen and housing the event loop
# It does not house any classes and does not handle the logic behind objects (which are to be dealt with by the object's methods)
import pygame
from pygame.locals import *

# noinspection PyAttributeOutsideInit
class App:
    def __init__(self):
        self._running = False
        self.screen_width = 400
        self.screen_height = 600
        self.title = "GUI"
        self._main_layout = None
        self._update = False

    def build(self):
        return None

    def remove_layout(self):
        """This allows the user to remove a specific layout from the list or dictionary of layouts"""
        return None

    def replace_layout(self, old_layout, new_layout):
        """This allows the user to replace one layout with another layout"""
        self._update = True

        for e, i in enumerate(self._layouts):
            if i == old_layout:
                self._layouts[e] = new_layout

        main_layout = self._main_layout
        print("main_layout", main_layout)

        if type(main_layout) == list:
            if type(main_layout[0]) == list:
                if type(main_layout[0][0]) == list:
                    for column in main_layout:
                        for layout in column:
                            if layout == old_layout:
                                main_layout[main_layout.index(column)][column.index(layout)] = new_layout

                elif type(main_layout[0][0]) == dict:
                    for column in main_layout:
                        for layout in column[0].keys():
                            if layout == old_layout:
                                main_layout[main_layout.index(column)][column[0].keys().index(layout)] = new_layout

            elif type(main_layout[0]) == dict:
                for column in main_layout:
                    for layout in column.keys():
                        if layout == old_layout:
                            main_layout[main_layout.index(column)][column[0].keys().index(layout)] = new_layout

            else:
                for layout in main_layout:
                    if layout == old_layout:
                        main_layout[main_layout.index(layout)] = new_layout

        elif type(main_layout) == dict:
            for layout in main_layout:
                if layout == old_layout:
                    print("before", main_layout)
                    #print("new", new_layout)
                    main_layout[layout] = new_layout
                    print("middle")
                    main_layout[main_layout.index(layout)] = new_layout
                    #main_layout[main_layout.index(layout)] = new_layout
                    print("after", main_layout)

        else:
            if main_layout == old_layout:
                main_layout = new_layout

        self._main_layout = main_layout

    def add_layout(self):
        """This allows the user to add a layout to a position in the list or dictionary"""
        return None

    def _get_layouts(self, main_layout):
        layouts = []

        if type(main_layout) == list:
            if type(main_layout[0]) == list:
                if type(main_layout[0][0]) == list:
                    for column in main_layout:
                        for layout in column:
                            layouts.append(layout)

                elif type(main_layout[0][0]) == dict:
                    for column in main_layout:
                        for layout in column[0].keys():
                            layouts.append(layout)

            elif type(main_layout[0]) == dict:
                for column in main_layout:
                    for layout in column.keys():
                        layouts.append(layout)
            else:
                for layout in main_layout:
                    layouts.append(layout)

        elif type(main_layout) == dict:
            for layout in main_layout:
                layouts.append(layout)

        else:
            layouts.append(main_layout)

        return layouts

    def _assign_layout_params(self, main_layout):
        layout_surfaces = []
        layout_surface_positions = []
        if type(main_layout) == list:
            height_list = []
            width_list = []
            if type(main_layout[0]) == list:
                if type(main_layout[0][0]) == list:
                    layout_width = self.screen_width / len(main_layout)
                    for column in main_layout:
                        height_list.append(self.screen_height / len(column))
                    for i, column in enumerate(main_layout):
                        for n, layout in enumerate(column):
                            layout.assign_dimensions((layout_width, height_list[i]))
                            layout.assign_position((i * layout_width, n * height_list[i]))
                            layout_surface_positions.append((i * layout_width, n * height_list[i]))
                            layout_surfaces.append(pygame.surface.Surface((layout_width, height_list[i])))

                elif type(main_layout[0][0]) == dict:
                    for i, column in enumerate(main_layout):
                        width_list.append(column[1] * self.screen_width)
                        height_list.append([])
                        for layout_height in column[0].values():
                            height_list[i].append(self.screen_height * layout_height)
                    for i, column in enumerate(main_layout):
                        for n, layout in enumerate(column[0].keys()):
                            layout.assign_dimensions((width_list[i], height_list[i][n]))
                            layout.assign_position((sum(width_list[:i]), n * sum(height_list[i][:n])))
                            layout_surface_positions.append((sum(width_list[:i]), n * sum(height_list[i][:n])))
                            layout_surfaces.append(pygame.surface.Surface((width_list[i], height_list[i][n])))

            elif type(main_layout[0]) == dict:
                layout_width = self.screen_width / len(main_layout)
                for i, column in enumerate(main_layout):
                    height_list.append([])
                    for layout_height in column.values():
                        height_list[i].append(self.screen_height * layout_height)
                for i, column in enumerate(main_layout):
                    for n, layout in enumerate(column.keys()):
                        layout.assign_dimensions((layout_width, height_list[i][n]))
                        layout.assign_position((i * layout_width, n * sum(height_list[i][:n])))
                        layout_surface_positions.append((i * layout_width, n * sum(height_list[i][:n])))
                        layout_surfaces.append(pygame.surface.Surface((layout_width, height_list[i][n])))

            else:
                layout_width = self.screen_width
                layout_height = self.screen_height / len(main_layout)
                for i, layout in enumerate(main_layout):
                    layout.assign_dimensions((layout_width, layout_height))
                    layout.assign_position((0, i * layout_height))
                    layout_surface_positions.append((0, i * layout_height))
                    layout_surfaces.append(pygame.surface.Surface((layout_width, layout_height)))

        elif type(main_layout) == dict:
            layout_width = self.screen_width
            layout_heights = []
            for size in main_layout.values():
                print(repr(size))
                print(repr(self.screen_height))
                layout_heights.append(size * self.screen_height)

            for i, (layout, size) in enumerate(main_layout.items()):
                layout.assign_dimensions((layout_width, layout_heights[i]))
                layout.assign_position((0, sum(layout_heights[:i])))
                layout_surface_positions.append((0, sum(layout_heights[:i])))
                layout_surfaces.append(pygame.surface.Surface((layout_width, layout_heights[i])))
        else:

            main_layout.assign_dimensions((self.screen_width, self.screen_height))
            main_layout.assign_position((0, 0))
            layout_surface_positions.append((0, 0))
            layout_surfaces.append(pygame.surface.Surface((self.screen_width, self.screen_height)))

        return layout_surfaces, layout_surface_positions

    def _draw_layout_surfaces(self, surface_layouts, surface_positions):
        for e, surface in enumerate(surface_layouts):
            self._screen.blit(surface, surface_positions[e])

    def run(self):
        pygame.init()
        self._main_layout = self.build()
        main_layout = self._main_layout

        pygame.display.set_caption(self.title)
        self._screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self._running = True
        scroll_list = []
        self._layouts = self._get_layouts(main_layout)
        layouts = self._layouts

        widgets = []
        layout_surfaces, layout_positions = self._assign_layout_params(main_layout)

        clock = pygame.time.Clock()

        for layout in layouts:
            if layout.scroll_enabled:
                scroll_list.append(layout)
            widgets += layout.provide_widgets()

        while self._running:
            #print("fps:", clock.get_fps())
            clock.tick(60)
            #if scroll_list != []:
            #    self._assign_layout_params(self._main_layout)
            if self._update:
                layout_surfaces, layout_positions = self._assign_layout_params(main_layout)
                layouts = self._get_layouts(self._main_layout)
                self._update = False

            self._draw_layout_surfaces(layout_surfaces, layout_positions)

            for e, layout in enumerate(layouts):
                layout.draw(layout_surfaces[e], pygame.mouse.get_pos())

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 4 or event.button == 5:
                        for layout in scroll_list:
                            if layout._mouse_over(pygame.mouse.get_pos()):
                                layout.scroll(event.button)

                    else:
                        for widget in widgets:
                            if widget._type in ["button", "text_input", "checkbox"]:
                                if widget.mouse_click():
                                    try:
                                        widget.action()
                                    except AttributeError:
                                        pass

                if event.type == KEYDOWN:
                    for widget in widgets:
                        if widget._type == "text_input":
                            widget.update(event)