# GUI_toolkit
I thought I'd try my hand at creating my own GUI toolkit.

This is loosely based on the kivy framework however uses pygame to draw items on the screen.
The point is the user does not interact with pygame themselves.

As can be seen in the tester.py files the user must:
  1. import App
  2. create a child class with App as its parent class
  3. add a build method to the child class
  4. return the layout config within the build method

There are several configurations for how the layout/layouts can be arranged:
return main_layout
where main_layout can be:
  - = layout1 --> (this will display a single layout on the screen)
  - = [layout1, layout2] --> (this will display multiple layouts stacked on top of eachother with each layout occupying the same amount of space)
  - = {layout1: 0.6, layout2: 0.4} --> (this sets the proportions for each layout in the vertical stack)
  - = [[layout1, layout2], [layout3]] --> (each nested list here is a column; so you will have layout3 in a seperate column to the right (the size of each layout cannot be changed in this config))
  - = [{layout1: 0.6, layout2:0.4}, {layout3: 0.2, layout4: 0.8}] --> (Similar to the previous config this allows for seperate columns in which the size of each layout can be changed)
  - COMING SOON: = [[{layout1 : 0.6, layout: 0.4}, 0.7] , [{layout3: 0.2, layout4: 0.8}, 0.3]] --> (This allows for the changing of the size of the layouts in the columns but also the widths of the columns themselves)
