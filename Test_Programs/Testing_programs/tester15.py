from app import App
from Widgets.Button_widget import Button
from Widgets.Text_widget import Text
from Layouts.Box_Layout import BoxLayout


class Example(App):
    def build(self):
        self.screen_width = 400
        self.screen_height = 600

        main_layout = []

        left_top = BoxLayout()
        left_top.background_colour = (200, 200, 200)
        left_top.padding = [0, 0, 0, 0]
        left_top.mode = "horizontal"
        main_layout.append(left_top)

        left_bottom = BoxLayout()
        left_bottom.background_colour = (200, 200, 200)
        left_bottom.padding = [0, 0, 0, 0]
        left_bottom.mode = "horizontal"
        main_layout.append(left_bottom)

        if True:
            button1 = Button()
            button1.text = "Left align"
            button1.text_align = "left"
            button1.colour = (100, 100, 100)
            button1.pressed_colour = (0, 255, 0)
            button1.rounded = True
            left_top.add_widget(button1)

            button2 = Button()
            button2.text = "Right align"
            button2.text_align = "right"
            button2.colour = (100, 100, 100)
            button2.pressed_colour = (255, 0, 0)
            button2.rounded = True
            left_top.add_widget(button2)

            button3 = Button()
            button3.text = "This is a test to see if it is able to reduce the font size if the text is too large"
            button3.colour = (100, 100, 100)
            button3.pressed_colour = (255, 0, 255)
            button3.rounded = True
            left_bottom.add_widget(button3)

            button4 = Button()
            button4.text = "Home"
            button4.colour = (100, 100, 100)
            button4.pressed_colour = (255, 0, 255)
            button4.display_icon = True
            button4.icon_name = "home"
            button4.icon_align = "left"
            button4.icon_scale = 0.4
            button4.icon_spacing = 0.04
            button4.rounded = True
            left_bottom.add_widget(button4)

            button5 = Button()
            button5.text = "Calendar"
            button5.colour = (100, 100, 100)
            button5.pressed_colour = (255, 0, 255)
            button5.display_icon = True
            button5.icon_name = "calendar"
            button5.icon_align = "right"
            button5.icon_scale = 0.4
            button5.icon_spacing = 0.04
            button5.rounded = True
            left_bottom.add_widget(button5)

        return main_layout

if __name__ == "__main__":
    application = Example()
    application.run()