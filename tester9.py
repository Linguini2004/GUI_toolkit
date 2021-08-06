from app import App
from Widgets.Button_widget import Button
from Widgets.Text_widget import Text
from Layouts.Box_Layout import BoxLayout


class Example(App):
    def build(self):
        self.screen_width = 400
        self.screen_height = 600

        main_layout = []

        left_column = []
        left_layouts = {}

        right_column = []
        right_layouts = {}

        left_top = BoxLayout()
        left_top.background_colour = (200, 200, 200)
        left_top.padding = [0, 0, 0, 0]
        left_top.mode = "horizontal"
        left_layouts[left_top] = 0.4

        left_bottom = BoxLayout()
        left_bottom.background_colour = (200, 200, 200)
        left_bottom.padding = [0, 0, 0, 0]
        left_layouts[left_bottom] = 0.6

        right_top = BoxLayout()
        right_top.background_colour = (200, 200, 200)
        right_top.padding = [0, 0, 0, 0]
        right_top.mode = "horizontal"
        right_layouts[right_top] = 0.5

        right_bottom = BoxLayout()
        right_bottom.background_colour = (200, 200, 200)
        right_bottom.padding = [0, 0, 0, 0]
        right_layouts[right_bottom] = 0.5

        left_column += [left_layouts, 0.6]
        right_column += [right_layouts, 0.4]
        main_layout.append(left_column)
        main_layout.append(right_column)

        if True:
            button1 = Button()
            button1.text = "B1"
            button1.colour = (100, 100, 100)
            button1.pressed_colour = (0, 255, 0)
            button1.rounded = True
            left_top.add_widget(button1)

            button2 = Button()
            button2.text = "B2"
            button2.colour = (100, 100, 100)
            button2.pressed_colour = (255, 0, 0)
            button2.rounded = True
            left_top.add_widget(button2)

            button3 = Button()
            button3.text = "B3"
            button3.colour = (100, 100, 100)
            button3.pressed_colour = (0, 0, 255)
            button3.rounded = True
            right_top.add_widget(button3)

            button4 = Button()
            button4.text = "B4"
            button4.colour = (100, 100, 100)
            button4.pressed_colour = (255, 0, 255)
            button4.rounded = True
            left_bottom.add_widget(button4)

        return main_layout

if __name__ == "__main__":
    application = Example()
    application.run()