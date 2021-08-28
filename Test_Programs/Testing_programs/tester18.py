from app import App
from Layouts.Box_Layout import BoxLayout
from Widgets.Text_widget import Text
from Widgets.Button_widget import Button

class Example(App):
    def build(self):
        layout = BoxLayout()
        layout.background_colour = (255, 255, 255)
        layout.mode = "vertical"

        text = Text()
        text.text_colour = (0, 0, 0)
        text.text = "This is a test"
        layout.add_widget(text)

        button1 = Button()
        button1.rounded = True
        button1.hover_colour = (255, 255, 255)
        layout.add_widget(button1)

        return layout

if __name__ == "__main__":
    application = Example()
    application.run()