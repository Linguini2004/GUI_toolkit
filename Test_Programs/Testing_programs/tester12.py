from app import App
from Widgets.Button_widget import Button
from Widgets.Text_Input import Text_Input
from Widgets.Text_widget import Text
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
        main_layout[top_layout] = 0.45

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
        test_text.header_active = True
        test_text.header_text = "Type Here:"
        test_text.header_align = "top"
        test_text.default_text = "Type here"
        test_text.default_text_colour = (255, 255, 255)
        top_layout.add_widget(test_text)

        middle_layout = BoxLayout()
        middle_layout.background_colour = (235, 222, 200)
        middle_layout.padding = [0.1, 0.1, 0.1, 0.1]
        main_layout[middle_layout] = 0.45

        test_text2 = Text_Input()
        test_text2.text_colour = (11, 62, 146)
        test_text2.background_colour = (139, 153, 175)
        test_text2.hover_colour = (104, 109, 135)
        test_text2.active_colour = (200, 200, 200)
        test_text2.border_thickness = 0
        test_text2.font = self.font
        test_text2.border_colour = (133, 168, 186)
        test_text2.rounded = True
        test_text2.radius = 0.075
        test_text2.header_active = True
        test_text2.header_text = "Type Here:"
        test_text2.header_align = "left"
        middle_layout.add_widget(test_text2)

        bottom_layout = BoxLayout()
        bottom_layout.background_colour = (198, 168, 154)
        bottom_layout.padding = [0, 0, 0, 0]
        main_layout[bottom_layout] = 0.1

        if True:
            button1 = Button()
            button1.colour = (154, 122, 135)
            button1.hover_colour = (114, 82, 95)
            button1.pressed_colour = (0, 255, 0)
            button1.rounded = True
            button1.radius = 0.5
            button1.display_icon = True
            button1.icon_name = "left-arrow"
            button1.icon_align = "center"
            button1.icon_scale = 0.9
            button1.icon_colour = (0, 0, 255)
            bottom_layout.add_widget(button1)

            button2 = Button()
            button2.colour = (154, 122, 135)
            button2.pressed_colour = (255, 0, 0)
            button2.rounded = True
            button2.radius = 0.5
            button2.display_icon = True
            button2.icon_name = "right-arrow"
            button2.icon_align = "center"
            button2.icon_scale = 0.9
            bottom_layout.add_widget(button2)

            button3 = Button()
            button3.colour = (154, 122, 135)
            button3.pressed_colour = (0, 0, 255)
            button3.rounded = True
            button3.radius = 0.5
            button3.display_icon = True
            button3.icon_name = "home"
            button3.icon_align = "center"
            button3.icon_scale = 0.9
            bottom_layout.add_widget(button3)

            button4 = Button()
            button4.colour = (154, 122, 135)
            button4.pressed_colour = (255, 0, 255)
            button4.rounded = True
            button4.radius = 0.5
            button4.display_icon = True
            button4.icon_name = "add"
            button4.icon_align = "center"
            button4.icon_scale = 0.9
            bottom_layout.add_widget(button4)

        return main_layout




if __name__ == "__main__":
    application = Example()
    application.run()