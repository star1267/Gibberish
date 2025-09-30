import re 
import os
import split_words

onesyll=[]
twosyll = []
words =[]
def split_words(tag):
    # //TODO Doc string 
    
    # Counts how many set of vowels there are seperated by consinents. So individual vowels. and counts that as a syllable 
    syllables = re.findall(r'[aeiouy]+', tag) 
    
    length=len(syllables)
    return (length)
    #if len(syllables) == 1: 
        #return syllables
    




        # onesyll.append(tag)
    # if len(syllables) == 2: 
    #     twosyll.append(tag)

        


#calculatae # of syllables 