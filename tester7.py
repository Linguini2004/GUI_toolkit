from app import App
from Widgets.Button_widget import Button
from Layouts.Box_Layout import BoxLayout


class Example(App):
    def build(self):
        self.screen_width = 800
        self.screen_height = 600

        main_layout = []
        left_column = []
        right_column = []
        top_layout = BoxLayout()
        top_layout.background_colour = (200, 200, 200)
        left_column.append(top_layout)

        bottom_layout = BoxLayout()
        bottom_layout.background_colour = (50, 50, 50)
        bottom_layout.padding = [0, 0, 0, 0]
        left_column.append(bottom_layout)

        right_layout = BoxLayout()
        right_layout.background_colour = (150, 150, 150)
        right_layout.padding = [100, 100, 66, 66]
        right_column.append(right_layout)

        main_layout.append(left_column)
        main_layout.append(right_column)

        print(main_layout)

        if True:
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