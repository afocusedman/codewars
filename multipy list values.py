""" Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
"""
def grow(arr):
    #set initial mutliplier of 1
    multi = 1
    #iterate through the list to multiply all values
    for i in arr:
        multi *= int(i)
        i += 1
    return multi