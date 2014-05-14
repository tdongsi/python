'''
Created on May 14, 2014

Week 7:
http://www.codeskulptor.org/#examples-sound.py
'''

# simple music player, uses buttons and sounds
# note that .ogg sounds are not supported in Safari

import simpleguitk as simplegui
    
# define callbacks
def play():
    """play some music, starts at last paused spot"""
    music.play()

def pause():
    """pause the music"""
    music.pause()
    
def rewind():
    """rewind the music to the beginning """
    music.rewind()
    
def laugh():
    """play an evil laugh
    will overlap since it is separate sound object"""
    laugh.play()
    
def vol_down():
    """turn the current volume down"""
    global vol
    if vol > 0:
        vol = vol - 1
    music.set_volume(vol / 10.0)
    volume_button.set_text("Volume = " + str(vol))
    
def vol_up():
    """turn the current volume up"""
    global vol
    if vol < 10:
        vol = vol + 1
    music.set_volume(vol / 10.0)
    volume_button.set_text("Volume = " + str(vol))


# create frame - canvas will be blank
frame = simplegui.create_frame("Music demo", 250, 250, 100)

# set up control elements 
frame.add_button("play", play,100)
frame.add_button("pause", pause,100)
frame.add_button("rewind",rewind,100)
frame.add_button("laugh",laugh,100)
frame.add_button("Vol down", vol_down,100)
frame.add_button("Vol up", vol_up,100)

# initialize volume, create button whose label will display the volume
vol = 7
volume_button = frame.add_label("Volume = " + str(vol))


# load some sounds
music = simplegui.load_sound("https://dl.dropbox.com/s/a3gcm5kfyfkzwfw/Epoq-Lepidoptera.ogg")
laugh = simplegui.load_sound("https://dl.dropbox.com/s/6zwdvbl8hikzgad/Evillaugh.ogg")

# make the laugh quieter so my ears don't bleed
laugh.set_volume(.1)

frame.start()

