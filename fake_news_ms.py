"""
    File: fake_news_ms.py
    Author: Ethan Huang
    Purpose: Takes a csv file of fake news articles and counts how many times
        each word occurs in the title of each line of the file and stores this
        information in an object called Word. Then uses merge sort to sort the
        list.
    CSC 120 FA22 001
"""

import csv, string, sys

class Word():
    def __init__(self, word):
        """Instanstiates a Word object with a string passed through it as its
            word attribute and the count attribute set to 1.
        
        Parameters: word is a string.

        Returns: None."""
        self._word = word
        self._count = 1
    
    def word(self):
        """Getter method for the word attribute of a Word object.
        
        Parameters: None.

        Returns: None."""
        return self._word
    
    def count(self):
        """Getter method for the count attribute of a Word object.
        
        Parameters: None.

        Returns: None."""
        return self._count
    
    def incr(self):
        """Increases the count attribute of a Word object by 1.
        
        Parameters: None.

        Returns: None."""
        self._count += 1
    
    def __lt__(self, other):
        """Determines if the word attribute of a Word object is less than
            the word attribute of another word attribute.
        
        Parameters: other is another Word object.

        Returns: True if the Word object's word attribute is less than the
            other Word object's.
        False if the Word object's word attribute is greater than the
            other Word object's."""
        if self.word() < other.word():
            return True
        return False
    
    def __str__(self):
        """Represents the string representation of a Word object.
        
        Parameters: None.

        Returns: The Word object's word attribute followed by a colon, and
            its count attribute."""
        return self._word + ": " + str(self._count)


def merge_word(list1, list2, merged):
    """Takes two lists of Word objects and sorts in descending order based
        on their count attributes. If two objects have the same count, then
        they are sorted in alphabetical order.
        
        Parameters: list1 is a list of Word objects.
            list2 is a list of Word objects.
            merged is the list that you want list1 and list2 to be
            sorted into.

        Returns: A list that represents the Word objects sorted in descending
            order based on their counts and in alphabetical order if they have
            the same count value."""
    if list1 == [] or list2 == []:
        return merged + list1 + list2
    else:
        if list1[0].count() > list2[0].count():
            merged.append(list1[0])
            return merge_word(list1[1:], list2, merged)
        elif list1[0].count() < list2[0].count():
            merged.append(list2[0])
            return merge_word(list1, list2[1:], merged)
        else:
            if list1[0].word() < list2[0].word():
                merged.append(list1[0])
                return merge_word(list1[1:], list2, merged)
            else:
                merged.append(list2[0])
                return merge_word(list1, list2[1:], merged)

def merge_sort_list(alist):
    """Takes a list of Word objects and continuously breaks it down until
        there is either no elements left or only 1 and calls merge_word each
        time to sort the broken down lists.
        
        Parameters: alist is a list of Word objects.

        Returns: A new list that is alist but sorted in descending order based
            on each Word object's count attribute, and if two objects share
            the same count, then sorted in alphabetical order."""
    if alist == [] or len(alist) == 1:
        return alist
    else:
        x = len(alist) // 2
        first_half = alist[:x]
        second_half = alist[x:]
        sort_first_half = merge_sort_list(first_half)
        sort_second_half = merge_sort_list(second_half)
        return merge_word(sort_first_half, sort_second_half, [])

def process_punctuation(line):
    """Removes any punctuation in a string.
        
        Parameters: line is a string.

        Returns: A string that is the original string, but without
            any punctuation."""
    astring = ""
    for letter in line[4]:
        if letter not in string.punctuation:
            astring += letter
        else:
            astring += " "
    return astring

def process_whitespace(line):
    """Removes any whitespace in a string.
        
        Parameters: line is a string.

        Returns: A string that is the original string, but without
            any whitespace."""
    astring = ""
    for letter in line:
        if letter not in string.whitespace:
            astring += letter
        else:
            astring += " "
    return astring
        
def get_rid_of_small_words(line):
    """Takes a list and removes any elements that have a length of 2 or less.
        
        Parameters: line is a list of strings.

        Returns: A new list that is the old list but without any elements
            that have a length of two or less."""
    i = 0
    while i != len(line):
        if len(line[i]) <= 2:
            del(line[i])
        else:
            i += 1
    return line

def create_list_of_words(alist, line):
    """Takes an empty list to be appended to and a list of strings. Creates
        a Word object for each word in the line and appends that object to the
        empty list. If an object that represents the word already exists in
        the empty list, then the count attribute of the object is incremented
        instead.
        
        Parameters: alist is a list that will have Word objects appeded to it.
            line is a list of strings.

        Returns: None."""
    for word in line:
        found = False
        for element in alist:
            if element._word == word.lower():
                element.incr()
                found = True
        if found == False:
            alist.append(Word(word.lower()))

def print_out_words(alist, k):
    """Takes a list of Word objects and recursively searches through it for
        any objects that have a count equal to or greater than k and prints
        their words out.
        
    Parameters: alist is a list of Word objects.
        k is an integer.
    
    Returns: None."""
    if alist == []:
        return
    else:
        if alist[0]._count >= k:
            print("{} : {:d}".format(alist[0].word(), alist[0].count()))
        return print_out_words(alist[1:], k)

def main():
    afile = csv.reader(open(input("File: "), "r"))
    alist = []
    for line in afile:
        if "#" not in line[0]:
            line = process_punctuation(line)
            line = process_whitespace(line)
            line = line.split()
            line = get_rid_of_small_words(line)
            create_list_of_words(alist, line)
    merged = merge_sort_list(alist)
    n = input("N: ")
    k = merged[int(n)].count()
    print_out_words(merged, k)

sys.setrecursionlimit(4000)
main()