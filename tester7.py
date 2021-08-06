from app import App
from Widgets.Button_widget import Button
from Widgets.Text_Input import Text_Input
from Widgets.Text_widget import Text
from Layouts.Box_Layout import BoxLayout

class Example(App):
    def build(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.font = "arial"

        main_layout = []
        left_column = []
        centre_column = []
        right_column = []

        left_layout = BoxLayout()
        left_layout.background_colour = (200, 200, 200)
        left_layout.padding = [0, 0, 0, 0]
        left_column.append(left_layout)

        top_layout = BoxLayout()
        top_layout.background_colour = (200, 200, 200)
        centre_column.append(top_layout)

        bottom_layout = BoxLayout()
        bottom_layout.background_colour = (200, 200, 200)
        bottom_layout.padding = [0, 0, 0, 0]
        centre_column.append(bottom_layout)

        right_layout = BoxLayout()
        right_layout.background_colour = (200, 200, 200)
        right_layout.padding = [0.2, 0.2, 0.1, 0.1]
        right_column.append(right_layout)

        main_layout.append(left_column)
        main_layout.append(centre_column)
        main_layout.append(right_column)

        print(main_layout)

        if True:
            test_text = Text()
            test_text.text_colour = (0, 0, 0)
            test_text.text = "This is a really long text intended to test whether the text wrapping works. There are 4 " \
                             "options for how this text can be aligned: left, right, center, and block."
            test_text.font = self.font
            top_layout.add_widget(test_text)

            test_text2 = Text_Input()
            test_text2.text_colour = (0, 0, 0)
            test_text2.background_colour = (175, 175, 175)
            test_text2.hover_colour = (150, 150, 150)
            test_text2.active_colour = (125, 125, 125)
            test_text2.padding = [0.2, 0.2, 0, 0]
            test_text2.font = self.font
            test_text2.rounded = True
            test_text2.radius = 0.075
            test_text2.header_active = True
            test_text2.header_text = "Type Here:"
            test_text2.header_align = "top"
            left_layout.add_widget(test_text2)

            button1 = Button()
            button1.text = "B1"
            button1.colour = (100, 100, 100)
            button1.pressed_colour = (0, 255, 0)
            button1.rounded = True
            bottom_layout.add_widget(button1)

            button2 = Button()
            button2.text = "B2"
            button2.colour = (100, 100, 100)
            button2.pressed_colour = (255, 0, 0)
            button2.rounded = True
            bottom_layout.add_widget(button2)

            button3 = Button()
            button3.text = "B3"
            button3.colour = (100, 100, 100)
            button3.pressed_colour = (0, 0, 255)
            button3.rounded = True
            bottom_layout.add_widget(button3)

            button4 = Button()
            button4.text = "B4"
            button4.colour = (100, 100, 100)
            button4.pressed_colour = (255, 0, 255)
            button4.rounded = True
            bottom_layout.add_widget(button4)

            button5 = Button()
            button5.text = "B5"
            button5.colour = (100, 100, 100)
            button5.pressed_colour = (255, 0, 255)
            button5.rounded = True
            right_layout.add_widget(button5)

        return main_layout

if __name__ == "__main__":
    application = Example()
    application.run()