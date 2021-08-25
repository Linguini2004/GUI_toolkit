from app import App
from Widgets.Button_widget import Button
from Widgets.Text_Input import Text_Input
from Layouts.Box_Layout import BoxLayout


class Example(App):
    def build(self):
        self.screen_width = 400
        self.screen_height = 600
        self.font = "arial"
        self.title = "Proof of concept"

        main_layout = {}
        top_layout = BoxLayout()
        top_layout.background_colour = (235, 222, 200)
        top_layout.padding = [0.1, 0.1, 0.1, 0.1]
        main_layout[top_layout] = 0.9

        test_text = Text_Input()
        test_text.text_colour = (11, 62, 146)
        test_text.background_colour = (139, 153, 175)
        test_text.hover_colour = (104, 109, 135)
        test_text.active_colour = (200, 200, 200)
        test_text.border_thickness = 0
        test_text.font = self.font
        test_text.border_colour = (133, 168, 186)
        test_text.rounded = True
        test_text.radius = 0.075
        top_layout.add_widget(test_text)

        bottom_layout = BoxLayout()
        bottom_layout.background_colour = (198, 168, 154)
        bottom_layout.padding = [0, 0, 0, 0]
        main_layout[bottom_layout] = 0.1

        if True:
            button1 = Button()
            button1.text = "Home"
            button1.font = self.font
            button1.colour = (154, 122, 135)
            button1.pressed_colour = (0, 255, 0)
            button1.rounded = True
            bottom_layout.add_widget(button1)

            button2 = Button()
            button2.text = "Shop"
            button2.font = self.font
            button2.colour = (154, 122, 135)
            button2.pressed_colour = (255, 0, 0)
            button2.rounded = True
            bottom_layout.add_widget(button2)

            button3 = Button()
            button3.text = "Story"
            button3.font = self.font
            button3.colour = (154, 122, 135)
            button3.pressed_colour = (0, 0, 255)
            button3.rounded = True
            bottom_layout.add_widget(button3)

            button4 = Button()
            button4.text = "Friends"
            button4.font = self.font
            button4.colour = (154, 122, 135)
            button4.pressed_colour = (255, 0, 255)
            button4.rounded = True
            bottom_layout.add_widget(button4)

        return main_layout

if __name__ == "__main__":
    application = Example()
    application.run()