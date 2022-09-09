"""
Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.
"""

def past(h, m, s):
    print(h,m,s)
    s1 = h*3600000
    s2 = m*60000
    s3 = s*1000
    t = s1+s2+s3
    return t

    