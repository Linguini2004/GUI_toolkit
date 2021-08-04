from app import App
from Widgets.Button_widget import Button
from Layouts.Box_Layout import BoxLayout

class Example(App):
    def build(self):
        self.screen_width = 400
        self.screen_height = 600

        main_layout = []

        for i in range(3):
            layout = BoxLayout()
            layout.background_colour = (255, 255, 255)
            for b in range(2):
                layout.add_widget(Button())
            main_layout.append(layout)

        layout = BoxLayout()
        layout.background_colour = (200, 200, 200)
        for i in range(4):
            layout.add_widget(Button())
        main_layout.append(layout)

        return main_layout


if __name__ == "__main__":
    application = Example()
    application.run()