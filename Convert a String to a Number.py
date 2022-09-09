"""
We need a function that can transform a string into a number. What ways of achieving this do you know?

Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.
"""
def string_to_number(s):
    #get all elements of s and assign them a varibale n
    n = [i for i in s]
    num = ''
    #iterate through n and pick integers as strings, concatenate them and convert them to integer
    for a in n:
        a = str(a)
        num += a
    n = int(num)
    return n
