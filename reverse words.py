def reverse_words(s):
    #create a list of words in s
    word  = s.split(' ')
    #use reverse function to reverse th words
    word.reverse()
    #join the reversed words
    s = " ".join(str(w) for w in word)
    
    return s