from sys import *
from math import *




def check_palin(s):
    global init
    print("Init is %d" %(init))
    if len(s) <= 1 :
        if not init :
            print("returning 1")
            return True
        else :
            print("Please supply a string of atleast 2 characters! Exiting...\n")
            print("returning 0")
            return False
    else :
        init = 0
        if first_word(s) == last_word(s) :
            return check_palin(middle(s))
        else :
            print("returning 0")
            return False


def first_word(s) :
    return s[0]

def last_word(s):
    return s[-1]

def middle(s):
    return s[1:-1]

init  = 1
s = raw_input("Please enter a string")
print(check_palin(s))
if not check_palin(s) :
    print ("String %s IS NOT a palindrome!" %(s))
else :
    print ("String %s IS a palindrome!" %(s))

