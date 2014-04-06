'''
Created on Apr 5, 2014

@author: cuongd
'''

# Rock-paper-scissors-lizard-Spock

import random


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    '''
    Convert the name to number.
    Use dictionary instead of if/elif/else.
    After all, what represents a mapping better than a map?
    '''
    nameMap = {'rock': 0, 'Spock': 1, 'paper': 2, 'lizard':3, 'scissors':4}
    if name in nameMap:
        return nameMap[name];
    else:
        print "Error: Unknown choice:", name



def number_to_name(number):
    '''
    Convert the number to name.
    Use dictionary instead of if/elif/else.
    '''
    # Use the same nameMap as in name_to_number()
    nameMap = {'rock': 0, 'Spock': 1, 'paper': 2, 'lizard':3, 'scissors':4}
    
    # for CodeSkulptor
#     numberMap = { v:k for k,v in nameMap.iteritems() };
    numberMap = dict((v,k) for k, v in nameMap.items());
    
    if number in numberMap:
        return numberMap[number]
    else:
        print "Error: Number out of range:", number
    

def rpsls(player_choice): 
    # print a blank line to separate consecutive games
    print

    # print out the message for the player's choice
    print "Player chooses", player_choice

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses", comp_choice

    # compute difference of comp_number and player_number modulo five
    diff = (comp_number - player_number) % 5

    # use if/elif/else to determine winner, print winner message
    if diff == 0:
        print "Player and computer tie!"
    elif diff == 1 or diff == 2:
        print "Computer wins!"
    elif diff == 3 or diff == 4:
        print "Player wins!"
    else:
        print "Error occurs"

    
# test your code - LEAVE THESE CALLS IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# Testing

# # Test calls to name_to_number()
# print "== Testing name_to_number =="
# print name_to_number("rock")
# print name_to_number("Spock")
# print name_to_number("paper")
# print name_to_number("lizard")
# print name_to_number("scissors")
# print name_to_number("random")
# 
# # Test calls to number_to_name()
# print "== Testing number_to_name =="
# print number_to_name(0)
# print number_to_name(1)
# print number_to_name(2)
# print number_to_name(3)
# print number_to_name(4)
# print number_to_name(10)