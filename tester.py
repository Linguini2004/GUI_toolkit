from app import App
from Widgets.Button_widget import Button
from Layouts.Box_Layout import BoxLayout

class Example(App):
    def build(self):
        main_layout = BoxLayout()
        main_layout.background_colour = (255, 255, 255)
        main_layout.widget_border = 10
        main_layout.mode = "vertical"

        button1 = Button()
        button1.text = "hello"
        button1.colour = (100, 100, 100)
        button1.pressed_colour = (0, 255, 0)
        main_layout.add_widget(button1)

        button2 = Button()
        button2.text = "goodbye"
        button2.colour = (100, 100, 100)
        button2.pressed_colour = (255, 0, 0)
        main_layout.add_widget(button2)

        button3 = Button()
        button3.text = "Go away"
        button3.colour = (100, 100, 100)
        button3.pressed_colour = (0, 0, 255)
        main_layout.add_widget(button3)

        return main_layout

if __name__ == "__main__":
    application = Example()
    application.run()


