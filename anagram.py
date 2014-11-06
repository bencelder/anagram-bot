import string

# needed for sys.getsizeof()
import sys

exclude = set(string.punctuation)
exclude.add(' ')
exclude.update( set('1234567890') )

# remove whitespace, punctuation, etc
# there are faster ways to do this, see 
# https://stackoverflow.com/questions/265960
def clean(s):
    s = s.lower()
    s = ''.join( ch for ch in s if ch not in exclude )
    return s

def letter2num(ch):
    return ord( ch ) - 97

def sentence2nums( s ):
    return [ letter2num( c ) for c in clean( s ) ]

def letter_histogram( s ):
    hist = [0]*26
    for n in sentence2nums(s):
        hist[n] += 1
    return hist

def anagram_match( s1, s2 ):
    if letter_histogram(s1) == letter_histogram(s2):
        return True
    return False

#ana1 = "The earthquakes1230     ****''''! narlge"
#ana1 = "The earthquakes"
#ana2 = "That queer shake"

#s1 = string.lowercase

#print letter_histogram( ana1 )
#print letter_histogram( ana2 )

#print anagram_match( ana1, ana2 )
