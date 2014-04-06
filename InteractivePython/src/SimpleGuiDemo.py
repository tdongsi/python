'''
Created on Apr 6, 2014

Demo of SimpleGuiTk:
https://pypi.python.org/pypi/SimpleGUITk

For Windows 64-bit, find pygame and pillow at
http://www.lfd.uci.edu/~gohlke/pythonlibs/

@author: EpipolarGineer
'''

import simpleguitk as simplegui

# Event handler
def tick():
    print "tick!"

def demo1():
    # Register handler
    timer = simplegui.create_timer(1000, tick)
    # Start timer
    timer.start()

message = "Welcome!"

# Handler for mouse click
def click():
    global message
    message = "Good job!"

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [50,112], 36, "Red")

def demo2():
    # Create a frame and assign callbacks to event handlers
    frame = simplegui.create_frame("Home", 300, 200)
    frame.add_button("Click me", click)
    frame.set_draw_handler(draw)
    
    # Start the frame animation
    frame.start()
    
    
# Test
# demo1()
demo2()
