"""
Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

name + " plays banjo" 
name + " does not play banjo"

"""


def are_you_playing_banjo(name):
    n = [i for i in name]
    print(n)
    if (n[0]) == 'R' or (n[0]) == 'r':
        name = name + " plays banjo"
    else:
        name = name + " does not play banjo"
    return name