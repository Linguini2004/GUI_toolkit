from app import App
from Widgets.Button_widget import Button
from Layouts.Box_Layout import BoxLayout

class Example(App):
    def build(self):
        self.screen_width = 400
        self.screen_height = 600

        main_layout = BoxLayout()
        main_layout.background_colour = (255, 255, 255)
        main_layout.widget_spacing = 0.05
        main_layout.mode = "horizontal"
        main_layout.padding = [0, 0, 0, 0]

        button1 = Button()
        button1.text = "B1"
        button1.colour = (100, 100, 100)
        button1.pressed_colour = (0, 255, 0)
        button1.bind(self.test_button)
        button1.rounded = True
        main_layout.add_widget(button1)

        button2 = Button()
        button2.text = "B2"
        button2.colour = (100, 100, 100)
        button2.pressed_colour = (255, 0, 0)
        button2.rounded = True
        main_layout.add_widget(button2)

        button3 = Button()
        button3.text = "B3"
        button3.colour = (100, 100, 100)
        button3.pressed_colour = (0, 0, 255)
        button3.rounded = True
        main_layout.add_widget(button3)

        button4 = Button()
        button4.text = "B4"
        button4.colour = (100, 100, 100)
        button4.pressed_colour = (255, 0, 255)
        button4.rounded = True
        main_layout.add_widget(button4)

        return main_layout

    def test_button(self, button):
        print("Button 1 has been pressed")
        print(button.text)

if __name__ == "__main__":
    application = Example()
    application.run()


