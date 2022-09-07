"""
Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.

Examples:(Input1, Input2 --> Output (explanation)))
"""
def add_binary(a,b):
    #sum the two numbers
    c = a + b
    #convert the number to binary and remove the 0b at the beginning
    d = bin(c).replace("0b","")
    return d