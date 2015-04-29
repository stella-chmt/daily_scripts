__author__ = 'mengting.chen'


import types

def distance_from_zero(arg):
    tp = type(arg)
    #return tp
    if  (tp is types.IntType) or (tp is types.FloatType):
        return abs(arg)
    else:
        return "Not an integer or float!"

input = raw_input("type something")
print distance_from_zero(input)

"""
def shut_down(s):
    if s == "Yes" or s == "yes" or s == "YES":
        return "Shutting down..."
    elif s == "No" or s == "no" or s == "NO":
        return "Shutdown aborted!"
    else :
        return "Sorry, I didn't understand you."

input = raw_input("Do you want to shut down?")
print shut_down(input)
"""

"""
from math import pi

def area_of_circle(radius):
    return pi * (radius ** 2)
"""
