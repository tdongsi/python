'''
Created on Apr 6, 2014

@author: cuongd
'''

# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import math
import simpleguitk as simplegui

# initialize global variables used in your code
num_range = 100
secret_num = 0
guess_count = 0

# helper function to start and restart the game
def new_game():
    print "\nNew game. Range is from 0 to", num_range
    
    global secret_num 
    secret_num = random.randrange(num_range)
    global guess_count
    guess_count = int(math.ceil(math.log(num_range,2)))
    
    print "Number of remaining guesses is", guess_count
#     # DEBUG
#     print "Secret number:", secret_num


# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global num_range
    num_range = 100
    new_game()
    

def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range
    num_range = 1000
    new_game()
    
    
def input_guess(guess):
    # main game logic
    guess_int = int(guess)
    print "\nGuess was", guess_int
    
    global guess_count
    guess_count -= 1
    print "Number of remaining guesses is", guess_count
    
    if guess_int == secret_num:
        print "Correct!"
        new_game()
    else:
        if guess_count > 0:
            if guess_int < secret_num:
                print "Higher!"
            elif guess_int > secret_num:
                print "Lower!"
        else:
            print "You ran out of guesses. The number was", secret_num
            new_game()        
    

    
# create frame
frame =simplegui.create_frame("Guess the number", 200, 200, 200)

# register event handlers for control elements
frame.add_input("Enter your guess:", input_guess, 200)
frame.add_button("Range is [0,100)", range100, 200)
frame.add_button("Range is [0,1000)", range1000, 200)


# call new_game and start frame
num_range = 100
new_game()
frame.start()


