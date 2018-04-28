# Assignment8
# Total pair of words 488
# 13th pair of word is ['airts', 'stria']
#
# This program produces a sorted list of all pairs of words from our
# dictionary that are reverses of each other.
#
# modified by: Vidya More
# July , 2017
#

# Build a dictionary of all words
def build_dict():
    with open('words.txt') as my_file:
        words = {} # initialize a dictionary
        for word in my_file:
            word = word.strip()
            if (word in words): # add words to the dictionary
                words[word] = words[word] + 1
            else:
                words[word] = 1

    return words


# this function checks if the reverse word is in the dictionary
def isreversewordindict(word,reverseword, words):
    if (reverseword in words):
        return [word, reverseword]
    return None

# this function checks all the pair of reverse words
def find_all_words():
    words = build_dict()
    res = []  #create a list to store all the pair of words
    reversewordlist = [] #create a list to store reverse words
    for w in words:
        reverseword  = w[::-1] # reverse word with slice
        if w not in reversewordlist: #check in the reverse words list to make sure we are not adding duplicates
            newwordtoadd = isreversewordindict(w,reverseword, words) #if not already exists then check for reverse word pair in the dictionary
            # newwordtoadd will be None or a word
            if (newwordtoadd ): #if newwordtoadd is not none then add to to final pair of list
                res.append(newwordtoadd)
                print (newwordtoadd)
                reversewordlist.append(reverseword) #add reverseword to list to check the duplicate next time
    return res


find_all_words()
