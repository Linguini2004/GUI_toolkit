from app import App
from Widgets.Button_widget import Button
from Layouts.Box_Layout import BoxLayout


class Example(App):
    def build(self):
        self.screen_width = 400
        self.screen_height = 600

        main_layout = {}
        top_layout = BoxLayout()
        top_layout.background_colour = (200, 200, 200)
        main_layout[top_layout] = 0.8

        bottom_layout = BoxLayout()
        bottom_layout.background_colour = (50, 50, 50)
        bottom_layout.padding = [0, 0, 0, 0]
        main_layout[bottom_layout] = 0.2

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

        return main_layout

if __name__ == "__main__":
    application = Example()
    application.run()