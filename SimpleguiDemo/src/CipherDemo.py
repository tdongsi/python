'''
Created on May 8, 2014

Week 5:
http://www.codeskulptor.org/#examples-dictionaries.py
'''

# Cipher

import simpleguitk as simplegui

CIPHER = {'a': 'x', 'b': 'c', 'c': 'r', 'd': 'm', 'e': 'l'}

message = ""

# Encode button
def encode():
    emsg = ""
    for ch in message:
        emsg += CIPHER[ch]
    print message, "encodes to", emsg

# Decode button
def decode():
    dmsg = ""
    for ch in message:
        for key, value in CIPHER.items():
            if ch == value:
                dmsg += key
    print message, "decodes to", dmsg

# Update message input
def newmsg(msg):
    global message
    message = msg
    label.set_text(msg)
    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Cipher", 2, 200, 200)
frame.add_input("Message:", newmsg, 200)
label = frame.add_label('')
frame.add_button("Encode", encode)
frame.add_button("Decode", decode)

# Start the frame animation
frame.start()
