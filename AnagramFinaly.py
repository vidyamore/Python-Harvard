def build_dict():
    # Load in word file and sort each line.
    with open('words.txt') as my_file: 
        words = {} # initialize a dictionary 
        for word in my_file: 
            word = word.strip() 
             # Sort the chars in each word and return a string.
            chars = list(word)
            chars.sort()
            key = "".join(chars)
        # Add each line to a dictionary based on its sorted key.
            if key in words:
                value = words.get(key) + "," + word 
                words[key] = value
            else:
                words[key] = word
    return words

# find all the anagram in the given dictionary
def find_all_anagram(words):
    # Return a list of anagrams from the dictionary.
    # ... Use a sorted string as the key.
    anagramlist=[]#store anagramlist
    for word in words:
        chars = list(word)
        chars.sort()
        key = "".join(chars)
        values = words.get(key, "NONE")# if key doesnt exist then return "NONE" else print value of each word
        anagrams = values.split(",")
        if (anagrams != "NONE" and len(anagrams)>7):
            anagramlist.append([len(anagrams),anagrams])# build anagram tuple 
        
    anagramlist.sort(reverse=True)# sort tupple in reverse order     
    for i in range(10): # take only largest 10 set
        print(anagramlist[i])