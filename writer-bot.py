"""
    File: writer-bot.py
    Author: Ethan Huang
    Purpose: Simulate a Markov Chain Algorithm to generate text based on
        preceding words.
    CSC 120 FA22 001
"""

import random

def put_tuples_in_dictionary(alist, adict, n):
    """Takes a list of strings and a dictionary and the length that each
        string tuple in the dictionary should be.
    
    Parameters: alist is a list of strings.
    adict is a dictionary that will have tuples as key values based on alist.
    n is the length of each tuple that will be a key in adict from alist.
    
    Returns: a dictionary after having been given key-value pairs."""
    for i in range(0, len(alist) - n):
        if tuple(alist[i : i + n]) not in adict:
            adict[tuple(alist[i : i + n])] = []
        adict[tuple(alist[i : i + n])].append(alist[i + n])
    return adict

def create_tlist(num_words, new_list, adict, n):
    """Randomly generates text using Markov Chain Analysis where the words
        that came before influence the words that will come directly
        after it.
    
    Parameters: num_words is the max number of words you want to generate.
    new_list is the list that you want to add these words to.
    adict is a dictionary of key-value tuple pairs that are words within
        new_list.
    n is an integer that represents how long each tuple used as a key in adict
        is.
    
    Returns: a list that has words added to it."""
    i = 0
    while len(new_list) < num_words:
        markov = tuple(new_list[i : i + n])
        if markov not in adict:
            break
        if markov in adict:
            if len(adict[markov]) > 1:
                new_list.append(adict[markov][random.randint(0,len(adict[markov])- 1)])
            elif len(adict[markov]) == 1:
                new_list.append(adict[markov][0]) 
        i += 1
    return new_list

def add_NONWORD_to_list(alist, n, NONWORD):
    """Adds NONWORD to alist n times.
    
    Parameters: alist is a list that you want to add to.
    n is the number of times you will do so.
    NONWORD is a string that you are going to append to alist.
    
    Returns: a list that has NONWORD appended to it n times."""
    for i in range(n):
        alist.append(NONWORD)
    return alist

def get_all_input_lines(file, alist):
    """Takes a file, splits its contents by spaces and adds them to a list.
    
    Parameters: file is a read file object.
    alist is a list that you are adding the file contents to.
    
    Returns: a list that has all the file contents added to it."""
    alist = []
    for line in file:
        line = line.split()
        alist += line
    return alist

def construct_sentence(new_list):
    """Takes a list and constructs a sentence by concatenating the contents
        of the list to a string. Every 10 words, the newline marker is added
        to signify a new line.
        
    new_list is a list of words.
    
    Returns: a string that is a result of adding the contens of new_list to
        an empty string."""
    i = 0
    astring = ""
    final_string = ""
    for element in new_list:
        if i == 9:
            astring += element + "\n"
            i = 0
            final_string += astring
            astring = ""
        elif i != 9:
            astring += element + " "
            i += 1

    if astring != "":
        final_string += astring.strip()
    
    return final_string.strip("\n")


def main():
    SEED = 8
    NONWORD = " "
    random.seed(SEED)

    file = open(input(), "r")
    n = int(input())
    num_words = int(input())

    adict = {}
    alist = []
    alist2 = []

    alist2 = add_NONWORD_to_list(alist2, n, NONWORD)

    alist = get_all_input_lines(file, alist)

    alist2 += alist

    adict = put_tuples_in_dictionary(alist2, adict, n)

    new_list = []
    [new_list.append(alist[i]) for i in range(n)]

    new_list = create_tlist(num_words, new_list, adict, n)

    written = construct_sentence(new_list)
    print(written)

main()