
# CompareList_withchallenge.py
#
# This program Write a recursive function called is_equal_with_challenge() that takes two lists and decides if they are equal.
# This program covers the challenge part to use the type() function to decide if an element of a list is another list.
# 
# Created and Modified by Vidya More
#
# July 2017

def is_equal_with_challenge(x_list,y_list):
# check if only one list is empty if true then retyrn false
    if (x_list and not y_list ) or (not x_list and y_list ) :
        return False
# check if both the lists are empty then return true
    if not x_list and not y_list:
        return True
# check if both lists are not empty and perform further steps
    elif x_list and y_list:
# check if two lists have differnt lengths
        if len(x_list) != len(y_list):
            return False
        # check if the first element of each list is type List
        if type(x_list[0])== list and type (y_list[0])== list:
             # if true then compare these 2 lists with the same function
            return is_equal_with_challenge(x_list[0],y_list[0])
        # check if the first element of each list is not same
        if x_list[0] != y_list[0]:
            return False
# if the first element of each list is same then call recursive function by sendig the list from second element 
        return is_equal_with_challenge(x_list[1:],y_list[1:])
    else:
        return True



