'''
Created on Apr 19, 2014

@author: cuongd
'''

# define global variables

import simpleguitk as simplegui

# Time in number 0.1 seconds
mTime = 0
runStatus = False
trialNum = 0
scoreNum = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def formatTime(t):
    c = t % 10
    t = t // 10
    b = t % 60
    a = t // 60
    return '%d:%02d.%d' %(a,b,c)

def formatScore(scoreNum, trialNum):
    return '%d/%d' % (scoreNum, trialNum)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global runStatus
    runStatus = True


def stop():
    global runStatus
    global trialNum
    global scoreNum
    
    # Define the game rule
    if runStatus:
        trialNum += 1
        if mTime % 10 == 0:
            scoreNum += 1
    
    runStatus = False
    

def reset():
    global trialNum
    global scoreNum
    global mTime
    global runStatus
    
    trialNum = 0
    scoreNum = 0
    mTime = 0
    runStatus = False

# define event handler for timer with 0.1 sec interval
def tick():
    global mTime
    if runStatus:
        mTime += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(formatTime(mTime), [100,150], 30, "White")
    canvas.draw_text(formatScore(scoreNum,trialNum), [200, 50], 20, "Green")
    
# create frame
frame = simplegui.create_frame( "Stopwatch", 300, 300 )
frame.set_draw_handler(draw)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

# register event handlers
timer = simplegui.create_timer( 100, tick )
timer.start()

# start frame
frame.start();
