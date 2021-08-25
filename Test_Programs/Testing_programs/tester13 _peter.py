from app import App
from Layouts.Box_Layout import BoxLayout
from Widgets.Button_widget import Button
from Widgets.Image_widget import Image
from Widgets.Text_Input import Text_Input

class Example(App):
    def build(self):
        self.screen_width = 400
        self.screen_height = 600
        self.font = "arial"
        self.title = "Peter's App"

        main_layout = {}

        image_layout = BoxLayout()
        image_layout.background_colour = (200, 200, 200)

        image1 = Image()
        image1.image_path = "/Test_Programs/boring_logo.png"
        image_layout.add_widget(image1)
        main_layout[image_layout] = 0.45

        text_layout = BoxLayout()
        text_layout.background_colour = (200, 200, 200)

        text_box = Text_Input()
        text_box.background_colour = (200, 200, 255)
        text_box.font = self.font
        text_box.rounded = True
        text_box.radius = 0.5
        text_layout.add_widget(text_box)
        main_layout[text_layout] = 0.45

        bar = BoxLayout()
        bar.background_colour = (200, 200, 255)

        button1 = Button()
        button1.colour = (154, 122, 135)
        button1.hover_colour = (114, 82, 95)
        button1.pressed_colour = (0, 255, 0)
        button1.rounded = True
        button1.radius = 0.5
        button1.display_icon = True
        button1.icon_name = "calendar"
        button1.icon_align = "center"
        button1.icon_scale = 0.9
        button1.icon_colour = (150, 150, 200)
        bar.add_widget(button1)

        button2 = Button()
        button2.colour = (154, 122, 135)
        button2.pressed_colour = (255, 0, 0)
        button2.rounded = True
        button2.radius = 0.5
        button2.display_icon = True
        button2.icon_name = "settings"
        button2.icon_align = "center"
        button2.icon_scale = 0.9
        button2.icon_colour = (150, 150, 200)
        bar.add_widget(button2)

        button3 = Button()
        button3.colour = (154, 122, 135)
        button3.pressed_colour = (0, 0, 255)
        button3.rounded = True
        button3.radius = 0.5
        button3.display_icon = True
        button3.icon_name = "home"
        button3.icon_align = "center"
        button3.icon_scale = 0.9
        button3.icon_colour = (150, 150, 200)
        bar.add_widget(button3)

        button4 = Button()
        button4.colour = (154, 122, 135)
        button4.pressed_colour = (255, 0, 255)
        button4.rounded = True
        button4.radius = 0.5
        button4.display_icon = True
        button4.icon_name = "home"
        button4.icon_align = "center"
        button4.icon_scale = 0.9
        button4.icon_colour = (150, 150, 200)
        bar.add_widget(button4)


        main_layout[bar] = 0.1

        return main_layout

if __name__ == "__main__":
    application = Example()
    application.run()