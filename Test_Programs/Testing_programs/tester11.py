from app import App
from Widgets.Button_widget import Button
from Widgets.Text_widget import Text
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
        top_layout.padding = [0.1, 0, 0.05, 0.1]
        main_layout[top_layout] = 0.6

        bottom_layout = BoxLayout()
        bottom_layout.background_colour = (50, 50, 50)
        bottom_layout.padding = [0, 0, 0, 0]
        main_layout[bottom_layout] = 0.4

        if True:
            button1 = Button()
            button1.display_image = True
            button1.image_path = "/Test_Programs/NASA_logo.svg.png"
            #button1.image_path = "C:/Users/david/Documents/other_documents/pyhton/GUI_toolkit/Test_Programs/SpaceX-Logo.svg.png"
            #button1.image_path = "C:/Users/david/Documents/other_documents/pyhton/GUI_toolkit/Test_Programs/tesla_logo.png"
            #button1.image_path = "C:/Users/david/Documents/other_documents/pyhton/GUI_toolkit/Test_Programs/boring_logo.png"
            #button1.image_path = "C:/Users/david/Documents/other_documents/pyhton/GUI_toolkit/Test_Programs/starship.png"
            button1.colour = (100, 100, 100)
            button1.image_padding = [0, 0, 0, 0]
            button1.scale_image = 1
            button1.rounded = True
            button1.bind(self.button1_clicked)
            bottom_layout.add_widget(button1)


            button2 = Button()
            button2.display_image = True
            button2.image_path = "/Test_Programs/SpaceX-Logo.svg.png"
            button2.colour = (100, 100, 100)
            button2.pressed_colour = (255, 0, 0)
            button2.rounded = True
            bottom_layout.add_widget(button2)


        return main_layout

    def button1_clicked(self, button):
        button.image_path = "/Test_Programs/SpaceX-Logo.svg.png"


if __name__ == "__main__":
    application = Example()
    application.run()