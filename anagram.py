# anagram.py
# 
# This progarm finds all anagrams from our dictionarry  and print the 10 largest sets
#
# Created by: Vidya More
# July  , 2017

#Time progarm takes to run CPU times: user 547 ms, sys: 13.9 ms, total: 561 ms

"""lardgest 10 sets
[11, ['apers', 'asper', 'pares', 'parse', 'pears', 'prase', 'presa', 'rapes', 'reaps', 'spare', 'spear']]
[11, ['alerts', 'alters', 'artels', 'estral', 'laster', 'ratels', 'salter', 'slater', 'staler', 'stelar', 'talers']]
[10, ['least', 'setal', 'slate', 'stale', 'steal', 'stela', 'taels', 'tales', 'teals', 'tesla']]
[9, ['estrin', 'inerts', 'insert', 'inters', 'niters', 'nitres', 'sinter', 'triens', 'trines']]
[9, ['capers', 'crapes', 'escarp', 'pacers', 'parsec', 'recaps', 'scrape', 'secpar', 'spacer']]
[8, ['peris', 'piers', 'pries', 'prise', 'ripes', 'speir', 'spier', 'spire']]
[8, ['palest', 'palets', 'pastel', 'petals', 'plates', 'pleats', 'septal', 'staple']]
[8, ['lapse', 'leaps', 'pales', 'peals', 'pleas', 'salep', 'sepal', 'spale']]
[8, ['earings', 'erasing', 'gainers', 'reagins', 'regains', 'reginas', 'searing', 'seringa']]
[8, ['carets', 'cartes', 'caster', 'caters', 'crates', 'reacts', 'recast', 'traces']]
"""

def build_dict():
    # Load in word file and sort each line.
    with open('words.txt') as my_file: 
        words = {} # initialize a dictionary 
        for word in my_file: 
            word = word.strip() 
            key = sorted_word(word)
        # Add each line to a dictionary based on its sorted key.
            if key in words:
                value = words.get(key) + "," + word 
                words[key] = value
            else:
                words[key] = word
    return words

def sorted_word(word):
    # Sort the chars in each word and return a string.
    chars = list(word)
    chars.sort()
    return "".join(chars)


# find all the anagram in the given dictionary
def find_all_anagram(words):
    # Return a list of anagrams from the dictionary.
    # ... Use a sorted string as the key.
    anagramlist=[]#store anagramlist
    for word in words:
        key = sorted_word(word)
        values = words.get(key, "NONE")# if key doesnt exist then return "NONE" else print value of each word
        anagrams = values.split(",")
        if (anagrams != "NONE" and len(anagrams)>7):
            anagramlist.append([len(anagrams),anagrams])# build anagram tuple 
        
    anagramlist.sort(reverse=True)# sort tupple in reverse order     
    for i in range(10): # take only largest 10 set
        print(anagramlist[i])

words = build_dict()
results = find_all_anagram(words)