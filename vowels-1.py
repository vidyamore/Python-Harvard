# vowels.py
#
# This program that takes a command line parameter with the name of a file of words (such as words.txt) and finds every line that includes all of the vowels (a, e, i, o, and u)
# We need to get the file name from the user.
#
# Created and Modified by Vidya More
#
# July 2017

# In order to do get the file name from user , we'll need the sys arguments, so we need the system library:we should import the system library
import sys

# Once we've imported the system library, we need to extract our desired file name from the system arguments and store the impur file data in my file
# This line reads the command line arguments it was given and then prints out sys.argv
my_file = open(sys.argv[1])

# function that takes in a word,
# and returns True if all the vowels are present, and
# returns False if any of the vowels are missing.
def checkvowels (word):
    if "a" in word and "e" in word  and "i" in word and "o" in word and "u" in word:
        return True
    else:
        return False

# now that the file is open and stored to my_file, I can start working with it.
# After getting the name of the file we need to load, we need to actually load it!
# we can iterate through files by line.

for line in my_file:
    if checkvowels (line.lower()):
        print(line)
