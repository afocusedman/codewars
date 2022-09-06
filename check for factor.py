
"""
This function should test if the factor is a factor of base.

Return true if it is a factor or false if it is not.
"""
def check_for_factor(base, factor):
    #use modulus operator to check if base is divisible by factor
    if base % factor == 0:
        #if yes, return True
        return True
    #if no, return False
    else:
        return False