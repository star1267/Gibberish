import re 
import os
import split_words

onesyll=[]
twosyll = []
words =[]
def split_words(tag):
    """This function estimates the number of syllables of each word in the dict."""
    
    # Counts how many set of vowels there are seperated by consinents. So individual vowels. and counts that as a syllable 
    syllables = re.findall(r'[aeiouy]+', tag) 
    
    length=len(syllables)
    return (length)