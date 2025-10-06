import random 

def build_sentence(num_sent, words_insent, one_syllwords, two_syllwords, words): 
    """Creates a list of lists of sentences, adds # of one syll words, adds # two syll words, shuffles sentences, 
    joins to one string, returns one syl, two syl and sentences. """

    # Initionates a list of lists with numsent rows 
    sent = [ []*words_insent for i in range (num_sent)]
    #List of just words with 1 syll
    onesyl = words["1"]
    #list of just words with 2 syll
    twosyl = words["2"]

    # one iteration for each sentence requested 
    for x in range(0, num_sent):
        # Adds random one_syllwords number of onesyll words  
        one = random.sample(onesyl, one_syllwords)
        #adds random two_syllwords number of two syll words 
        two = random.sample(twosyl, two_syllwords)
        # Combines those two lists to make a sentences 
        sentence= one + two
        # randomly shuffles the order of those words 
        random.shuffle(sentence)
        # turns that sentences in to just one string instead of a bunch of strings sepeared by commas 
        string = ' '.join(sentence)
        # this iterations row becomes the one syl words, the two syl words and the clean sentence 
        sent[x] = one, two, string
    # returns that list of 3 things per row
    return (sent)