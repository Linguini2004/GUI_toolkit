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
        main_layout.padding = [0.1, 0.1, 0.2, 0.2]

        button1 = Button()
        button1.colour = (150, 150, 150)
        button1.rounded = True
        button1.text = "PRESS ME"
        main_layout.add_widget(button1)


        return main_layout

if __name__ == "__main__":
    application = Example()
    application.run()