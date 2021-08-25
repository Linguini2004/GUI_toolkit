from app import App
from Widgets.Button_widget import Button
from Widgets.Text_widget import Text
from Widgets.Image_widget import Image
from Layouts.Box_Layout import BoxLayout


class Example(App):
    def build(self):
        self.screen_width = 400
        self.screen_height = 600

        main_layout = {}
        top_layout = BoxLayout()
        top_layout.background_colour = (200, 200, 200)

        test_text = Text()
        test_text.text_colour = (50, 50, 50)
        test_text.text = "This is a really long text intended to test whether the text wrapping works. There are 4 " \
                         "options for how this text can be aligned: left, right, center, and block."
        top_layout.add_widget(test_text)
        top_layout.padding = [0, 0, 0.1, 0.1]
        top_layout.mode = "vertical"
        main_layout[top_layout] = 0.4

        middle_layout = BoxLayout()
        middle_layout.background_colour = (200, 200, 200)
        middle_layout.padding = [0, 0, 0, 0]
        main_layout[middle_layout] = 0.4

        bottom_layout = BoxLayout()
        bottom_layout.background_colour = (50, 50, 50)
        bottom_layout.padding = [0, 0, 0, 0]
        main_layout[bottom_layout] = 0.2

        if True:
            image1 = Image()
            #image1.image_path = "C:/Users/david/Documents/other_documents/pyhton/GUI_toolkit/Test_Programs/NASA_logo.svg.png"
            #image1.image_path = "C:/Users/david/Documents/other_documents/pyhton/GUI_toolkit/Test_Programs/SpaceX-Logo.svg.png"
            #image1.image_path = "C:/Users/david/Documents/other_documents/pyhton/GUI_toolkit/Test_Programs/tesla_logo.png"
            image1.image_path = "/Test_Programs/boring_logo.png"
            #image1.image_path = "C:/Users/david/Documents/other_documents/pyhton/GUI_toolkit/Test_Programs/starship.png"

            image1.padding = [0, 0, 0, 0]
            image1.keep_proportion = True
            image1.transparent = True
            image1.header_active = True
            image1.header_text = "Image:"
            image1.header_align = "top"
            image1.header_colour = (50, 50, 50)
            image1.header_spacing = 0.05
            image1.scale = 0.75
            middle_layout.add_widget(image1)

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
