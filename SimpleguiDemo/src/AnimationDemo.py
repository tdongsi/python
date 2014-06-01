'''
Created on May 31, 2014

Week 8:
http://www.codeskulptor.org/#examples-asteroid_animation.py
'''

# demo of animation using asteroid sprite sheet

import simpleguitk as simplegui

# load 64 frame sprite sheer for asteroid - image source is opengameart, artist is warspawn 
ROCK_CENTER = [64, 64]
ROCK_SIZE = [128, 128]
ROCK_DIM = 64
rock_image = simplegui.load_image("https://dl.dropbox.com/s/wnr4b2vfax81sy9/asteroid1.opengameart.warspawn.png")

# global time for animation
time = 0

# draw handler    
def draw(canvas):
    global time
    current_rock_index = (time % ROCK_DIM) // 1
    current_rock_center = [ROCK_CENTER[0] +  current_rock_index * ROCK_SIZE[0], ROCK_CENTER[1]]
    canvas.draw_image(rock_image, current_rock_center, ROCK_SIZE, ROCK_CENTER, ROCK_SIZE) 
    time += 0.3
    
# create frame and size frame based on 128x128 pixel sprite
frame = simplegui.create_frame("Asteroid sprite", ROCK_SIZE[0], ROCK_SIZE[1])

# set draw handler and canvas background using custom HTML color
frame.set_draw_handler(draw)
frame.set_canvas_background("Blue")

# start animation
frame.start()


