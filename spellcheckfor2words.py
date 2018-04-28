# spellcheck.py
#
# The user supplies a word and a dictionary on the command line.  If the word is not in the dictionary, this program suggests some likely alternatives. 
#
# Created and Modified by Vidya More
# used stackoverflow.com for optimization
#
# July 2017

# In order to do get the file name from user , we'll need the sys arguments, so we need the system library:we should import the system library
import sys

def build_dict():
    with open(sys.argv[3]) as my_file:
        words = {} # initialize a dictionary
        for word in my_file:
            word = word.strip()
            if (word in words): # add words to the dictionary
                words[word] = words[word] + 1
            else:
                words[word] = 1

    return words

def processword(word):
    words = build_dict() # Build Dictinary

    letters    = 'abcdefghijklmnopqrstuvwxyz' # set of a-z
    # Initialize lists to store results

    addlist= []
    finaladd =[]
    removelist = []
    finalremove =[]
    exchangelist =[]
    finalexchange =[]
    replacelist=[]
    finalreplace=[]
    # iterate loop till it reaches length of the word provided

    for i in range(len(word) + 1):
        part1 = word[:i]
        part2 = word[i:]
        #Legal words you can reach by adding a single letter
        for c in letters:
            addlist.append(part1 + c + part2)#a+thme, t+a+hme, th+a+me,thm+a+e,thme+a
            #Legal words you can reach by changing a single letter
            if part2: # check if index out of range 
                replacelist.append(part1 + c + part2[1:])#['tame', 'time', 'tome', 'thae', 'thee']
        #Legal words you can reach by removing a single letter
        if part2:
            removelist.append(part1 + part2[1:])# hme , tme, 'the', 'thm'
        #Legal words you can reach by exchanging two adjacent letters, like thsi. 
        if len(part2)>1:
            exchangelist.append(part1 + part2[1] + part2[0] + part2[2:] )#['htme', 'tmhe', 'them']


    #print (addlist)
    for word in addlist:
        if (word in words):
            finaladd.append(word)
    #print (removelist)    
    for word in removelist:
        if (word in words):
            finalremove.append(word)

    #print (exchangelist)    
    for word in exchangelist:
        if (word in words):
            finalexchange.append(word)

    #print (replacelist)    
    for word in replacelist:
        if (word in words):
            finalreplace.append(word)

    #print(finaladd)
    #print(finalremove)
    #print(finalexchange) 
    #print(finalreplace)

    finallist = set(finaladd )| set(finalremove) | set (finalexchange) | set(finalreplace)
    finallist = list(finallist)
    finallist.sort()
    print("Saw", len(finallist), "suggestions")
    print (finallist)
    return finallist

processword(sys.argv[1])
processword(sys.argv[2])
