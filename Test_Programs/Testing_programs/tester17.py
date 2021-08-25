from app import App
from Widgets.Button_widget import Button
from Widgets.Text_widget import Text
from Layouts.Box_Layout import BoxLayout


class Example(App):
    def build(self):
        self.screen_width = 400
        self.screen_height = 600

        main_layout = BoxLayout()
        main_layout.background_colour = (200, 200, 255)
        main_layout.scroll_enabled = True
        main_layout.real_size = 2
        main_layout.padding = (0.1, 0.1, 0.2, 0.2)

        layout2 = BoxLayout()
        layout2.background_colour = (100, 100, 100)

        button1 = Button()
        button1.colour = (50, 50, 50)
        button1.text = "Button"
        button1.rounded = True
        button1.hover_colour = (100, 100, 100)
        layout2.add_widget(button1)

        text1 = Text()
        text1.text = "This is a test to see if the refactor still allows this to work properly"
        layout2.add_widget(text1)

        return [main_layout, layout2]

if __name__ == "__main__":
    application = Example()
    application.run()