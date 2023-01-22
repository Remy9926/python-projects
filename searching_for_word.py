"""
    Takes two files, a list of words and a grid of letters,
    respectively and searches the grid for any words that are in
    the list of words. Words will be searched for horizontally, vertically,
    and diagonally from the top-left to bottom-right.
"""


def concat_elements(slist, startpos, stoppos):

    """Takes a list and concatenates the elements of the list from
    a starting index to an ending index.
    
    Parameters: slist is a list.
    startpos is the starting index.
    stoppos is the stopping index.
    
    Returns: A string that is the result of concatenating the elements of
    slist.
    
    Pre-condition: slist is a list of strings.
    startpos is an integer.
    stoppos is an integer.
    
    Post-condition: The return value is a string."""

    empty_string = ""
    
    if startpos < 0:
        i = 0
    else:
        i = startpos
        
    if stoppos > len(slist) - 1:
        stoppos = len(slist) - 1
    
    if startpos > stoppos:
        return empty_string
    
    while i <= stoppos:
        
        empty_string += slist[i]
        i += 1
    
    return empty_string

def column2list(grid, n):

    """Takes a list of lists and takes the nth column of the list and creates
    a list from it.

    Parameters: grid is a list of lists.
    n is a positive integer.

    Returns: A list that used to be the nth column of the list of lists.
    
    Pre-condition: grid is a list of lists.
    n is a positive integer.
    
    Post-condition: The return value is a list."""

    new_list = []
    
    i = 0
    
    while i < len(grid):
        
        new_list.append(grid[i][n])
        i += 1
    
    return new_list

def horizontal_search(list, word_list, found_words):

    """This function takes a list and searches through every word that
    consists of at least 3 consecutive letters in the list and if a word
    is found to be in word_list, then it appends the word to found_words.
    
    Parameters: list is a list of strings.
    word_list is a list of strings we are looking for.
    found_words is a list of strings we have found.
    
    Returns: None.
    
    Pre-condition: list is a list of strings.
    word_list is a list of strings.
    found_words is a list of strings.
    
    Post-condition: If any of the words in list are found to be within
    word_list, then they will be appended to found_words."""

    first_letter_index = 0
    last_letter_index = first_letter_index + 2
    
    while first_letter_index != len(list) - 2:

        while last_letter_index != len(list):

            word = concat_elements(list, first_letter_index, last_letter_index)

            if word in word_list and word not in found_words:

                found_words.append(word)

            last_letter_index += 1
        
        first_letter_index += 1
        last_letter_index = first_letter_index + 2

def vertical_search(grid_list, word_list, found_words):

    """Takes a list of lists and searches for words vertically from top to
    bottom and bottom to top to see if they're in word_list and if so
    appends them to found_words.

    Parameters: grid_list is a list of lists.
    word_list is a list of strings that we are looking for.
    found_words is a list of strings of words we have found.
    
    Returns: None.
    
    Pre-condition: grid_list is a list of lists.
    word_list is a list of strings.
    found_words is a list of strings.
    
    Post-condition: Any words found in grid_list that are at least
    three consecutive characters long and found in word_list will be
    appended to found_words."""

    for index in range(len(grid_list)):
        
        vertical_list = column2list(grid_list, index)
        horizontal_search(vertical_list, word_list, found_words)
        vertical_list = vertical_list[::-1]
        horizontal_search(vertical_list, word_list, found_words)

def diagonal_search(grid_list, word_list, found_words):
    
    """This function takes a list of lists and searches it diagonally for
    any words that may exist within word_list.
    
    Parameters: grid_list is a list of lists.
    word_list is a list of strings that we are looking for.
    found_words is a list of strings of words we have found.
    
    Returns: None.
    
    Pre-condition: grid_list is a list of lists.
    word_list is a list of strings
    found_words is a list of strings.
    
    Post-condition: Any words found in grid_list that are at least
    three consecutive characters long and found in word_list will be
    appended to found_words."""

    diagonal_words = []
    empty_list = []
    empty_list_2 = []
    y_coord = 0

    while y_coord != len(grid_list) - 2:
        
        for index in range(0, len(grid_list) - y_coord):
            
            if empty_list == []:

                empty_list.append(grid_list[index][y_coord])
                empty_list_2.append(grid_list[y_coord][index])

            else:

                empty_list.append(grid_list[index][index + y_coord])
                empty_list_2.append(grid_list[index + y_coord][index])
                
        if empty_list not in diagonal_words:
        
            diagonal_words.append(empty_list)
        
        if empty_list_2 not in diagonal_words:
        
            diagonal_words.append(empty_list_2)
        
        empty_list = []
        empty_list_2 = []
        y_coord += 1
    
    for word in diagonal_words:
        
        if word[::-1] not in diagonal_words:
            
            diagonal_words.append(word[::-1])
    
    for grid_list in diagonal_words:

        horizontal_search(grid_list, word_list, found_words)

def occurs_in(substr, word_list):
    
    """This function determines whether or not the string substr is in the
    list word_list.

    Parameters: substr is a string.
    word_list is a list of strings that we will search.

    Returns: True or False depending on whether or not substr is in word_list.
    
    Pre-condition: substr is a string.
    word_list is a list of strings.
    
    Post-condition: The return value is either True or False."""

    for word in word_list:

        if word.lower() == substr:

            return True
        
    return False

words = open(input(), "r")
grid = open(input(), "r")

grid_list = []
word_list = []
found_words = []

for word in words:
    
    word = word.strip("\n")
    word_list.append(word)

for row in grid:
    
    temp_list = []
    row = row.strip("\n")
    
    for word in row:
        
        if word != " ":
        
            temp_list.append(word)
    
    grid_list.append(temp_list)
    temp_list = []

for list in grid_list:

    horizontal_search(list, word_list, found_words)

    list = list[::-1]

    horizontal_search(list, word_list, found_words)

    vertical_search(grid_list, word_list, found_words)

    diagonal_search(grid_list, word_list, found_words)

found_words.sort()

for word in found_words:

    print(word)
