from app import App
from Layouts.Box_Layout import BoxLayout
from Widgets.Button_widget import Button
from Widgets.Text_Input import Text_Input
from Widgets.Text_widget import Text
from Widgets.Image_widget import Image
from Widgets.Checkbox_widget import CheckBox

def create_home_layout():
    top_layout = BoxLayout()
    top_layout.mode = "vertical"
    top_layout.background_colour = (240, 240, 240)
    top_layout.scroll_enabled = True
    top_layout.real_size = 1.5
    top_layout.padding = [0, 0, 0, 0]
    # top_layout.widget_spacing = 0

    '''Creates the username text box and adds it to the top_layout'''
    username = Text_Input()
    # box config:
    username.background_colour = (216, 216, 216)
    username.hover_colour = (158, 158, 159)
    username.active_colour = (153, 158, 159)
    username.text_colour = (79, 99, 103)
    username.rounded = True
    username.radius = 0.3
    username.padding = [0.1, 0.1, 0.05, 0.05]
    username.size_hint = [1, 0.6]
    # header:
    username.header_active = True
    username.header_align = "top"
    username.header_text = "Username:"
    username.header_spacing = 0.05
    # default text:
    username.default_text_colour = (158, 158, 159)
    username.default_text = "username"
    top_layout.add_widget(username)

    '''Creates the password text box and adds it to the top_layout'''

    password = Text_Input()
    # box config:
    password.background_colour = (216, 216, 216)
    password.hover_colour = (158, 158, 159)
    password.active_colour = (158, 158, 159)
    password.text_colour = (79, 99, 103)
    password.rounded = True
    password.radius = 0.3
    password.padding = [0.1, 0.1, 0.05, 0.05]
    password.size_hint = [1, 0.6]
    password.compressible = True
    # header:
    password.header_active = True
    password.header_align = "top"
    password.header_text = "Password:"
    password.header_spacing = 0.05
    # default text:
    password.default_text_colour = (158, 158, 159)
    password.default_text = "password"
    top_layout.add_widget(password)

    '''Creates the enter button and adds it to the top_layout'''
    enter_button = Button()
    # box config:
    enter_button.colour = (216, 216, 216)
    enter_button.hover_colour = (158, 158, 159)
    enter_button.size_hint = [0.4, 0.4]
    enter_button.pos_hint = [1, 0.3]
    enter_button.rounded = True
    enter_button.radius = 0.3
    # text and icon:
    enter_button.text = "Confirm"
    enter_button.text_colour = (79, 99, 103)
    enter_button.text_align = "center"
    enter_button.display_icon = True
    enter_button.icon_name = "right-arrow"
    enter_button.icon_spacing = 0.1
    enter_button.icon_align = "right"
    enter_button.icon_colour = (254, 95, 85)
    enter_button.icon_scale = 0.5
    top_layout.add_widget(enter_button)

    tcs = CheckBox()
    tcs.header_active = True
    tcs.header_text = "Accept terms and conditions:"
    tcs.header_orientation = "left"
    tcs.header_align = "center"
    tcs.header_colour = (79, 99, 103)
    tcs.colour = (240, 240, 240)
    tcs.icon_type = "tick"
    tcs.border_thickness = 2
    tcs.box_size = 0.3
    tcs.rounded = True
    tcs.radius = 0.3
    tcs.size_hint = [1, 0.5]
    tcs.pos_hint = [0, 0]
    tcs.compressible = True
    tcs.box_align = "right"
    tcs.header_spacing = 0.01
    top_layout.add_widget(tcs)

    text = Text()
    text.text = "By ticking above you agree to our terms and conditions. The full terms and conditions can be" \
                " viewed on our website at www.termsandconditoins.com."
    text.align = "left"
    text.text_colour = (79, 99, 103)
    top_layout.add_widget(text)

    image1 = Image()
    image1.image_path = "C:/Users/david/Documents/other_documents/pyhton/GUI_toolkit/Test_Programs/SpaceX-Logo.svg.png"
    image1.size_hint = [0.5, 0.5]
    image1.pos_hint = [0.5, 0.5]
    image1.compressible = False
    top_layout.add_widget(image1)

    image2 = Image()
    image2.image_path = "C:/Users/david/Documents/other_documents/pyhton/GUI_toolkit/Test_Programs/boring_logo.png"
    image2.size_hint = [0.5, 0.5]
    image2.pos_hint = [0.5, 0.5]
    image2.compressible = False
    top_layout.add_widget(image2)

    return top_layout

def create_bottom_layout(app, home_layout, settings_layout):
    bottom_layout = BoxLayout()
    bottom_layout.mode = "horizontal"
    bottom_layout.background_colour = (158, 158, 158)
    bottom_layout.padding = [0, 0, 0, 0]

    button1 = Button()
    button1.colour = (230, 230, 230)
    button1.hover_colour = (210, 210, 210)
    button1.pressed_colour = (158, 158, 158)
    button1.display_icon = True
    button1.icon_name = "home"
    button1.icon_colour = (254, 95, 85)
    button1.icon_scale = 0.85
    button1.rounded = True
    button1.radius = 0.5
    button1.bind(app.show_home_screen, home_layout, settings_layout)
    bottom_layout.add_widget(button1)

    button2 = Button()
    button2.colour = (230, 230, 230)
    button2.hover_colour = (210, 210, 210)
    button2.pressed_colour = (158, 158, 158)
    button2.rounded = True
    button2.display_icon = True
    button2.icon_name = "settings"
    button2.icon_colour = (254, 95, 85)
    button2.icon_scale = 0.85
    button2.radius = 0.5
    bottom_layout.add_widget(button2)

    button3 = Button()
    button3.colour = (230, 230, 230)
    button3.hover_colour = (210, 210, 210)
    button3.pressed_colour = (158, 158, 158)
    button3.rounded = True
    button3.display_icon = True
    button3.icon_name = "left-arrow"
    button3.icon_colour = (254, 95, 85)
    button3.icon_scale = 0.75
    button3.radius = 0.5
    bottom_layout.add_widget(button3)

    button4 = Button()
    button4.colour = (230, 230, 230)
    button4.hover_colour = (210, 210, 210)
    button4.pressed_colour = (158, 158, 158)
    button4.rounded = True
    button4.display_icon = True
    button4.icon_name = "right-arrow"
    button4.icon_colour = (254, 95, 85)
    button4.icon_scale = 0.75
    button4.radius = 0.5
    bottom_layout.add_widget(button4)

    return bottom_layout

def create_settings_layout():
    top_layout = BoxLayout()
    top_layout.mode = "vertical"
    top_layout.background_colour = (240, 240, 240)
    top_layout.scroll_enabled = True
    top_layout.real_size = 1.5
    top_layout.padding = [0, 0, 0, 0]

    return top_layout

class Showcase(App):
    def build(self):
        self.screen_width = 400
        self.screen_height = 600
        self.title = "Showcase1"

        screen = {}

        home_layout = create_home_layout()
        settings_layout = create_settings_layout()
        bottom_layout = create_bottom_layout(self, home_layout, settings_layout)

        #return top_layout
        return {home_layout: 0.9, bottom_layout: 0.1}

    def show_home_screen(self, button, home_layout, settings_layout):
        self.replace_layout(home_layout, settings_layout)

    def show_settings(self):
        pass

if __name__ == "__main__":
    application = Showcase()
    application.run()