"""
     Takes a csv file of fake news articles and counts how many times
        each word occurs in the title of each line of the file.
"""

import csv, string

class Node():
    def __init__(self, word):
        """Instantiates a Node object with the parameter word as its word,
            sets its _count attribute to 1 and it's _next attribute to None.
        
        Parameters: word is a string.
        
        Returns: None."""
        self._word = word
        self._count = 1
        self._next = None
    
    def word(self):
        """Returns the _word attribute of a node.
        
        Parameters: None.
        
        Returns: A string that is the _word attribute of a node"""
        return self._word
    
    def count(self):
        """Returns the _count attribute of a node.
        
        Parameters: None.
        
        Returns: An integer that is the count attribute of a node."""
        return self._count
    
    def next(self):
        """Returns the _next attribute of a node.
        
        Parameters: None.
        
        Returns: A reference to the next node or None."""
        return self._next
    
    def set_next(self, target):
        """Sets the _next attribute of a node to be the parameter target.
        
        Parameters: target is whatever you want the _next attribute of your
            node to be.
        
        Returns: None."""
        self._next = target
    
    def incr(self):
        """Increments the _count attribute of the node.
        
        Parameters: None.
        
        Returns: None."""
        self._count += 1
    
    def __str__(self):
        """Returns the _word attribute of a node and its _count attribute.
        
        Parameters: None.
        
        Returns: None."""
        return self._word + ": " + str(self._count)


class LinkedList():
    def __init__(self):
        """Instantiates a linked list object.
        
        Parameters: None.
        
        Returns: None."""
        self._head = None
    
    def is_empty(self):
        """Returns whether or not a Linked List object is empty or not.

        Parameters: None.

        Returns: True if the Linked List is empty.
            False if the Linked List is not empty."""
        return self._head == None
    
    def head(self):
        """Returns a reference to the head/first node of the Linked List.

        Parameters: None.

        Returns: A reference to the first node of the Linked List."""
        return self._head
    
    def update_count(self, word):
        """Increments the _count attribute of a node if a node exists who's
            _word attribute is the parameter word in the Linked List. If 
            there does not exist such a node, then a node is created and added
            to the Linked List.
        
        Parameters: word is a string.
        
        Returns: None."""
        current = self._head
        updated = False
        while current != None:
            if current._word == word:
                current.incr()
                updated = True
            current = current._next
        if updated == False:
            new_node = Node(word)
            self.add(new_node)
    
    def rm_from_hd(self):
        """Removes the first node of a Linked List.
        
        Parameters: None.
        
        Returns: None."""
        removed = self._head
        self._head = self._head._next
        removed.set_next(None)

    def insert_after(self, node1, node2):
        """Takes two nodes, node1 and node2, and places node2 right after
            node1 sequentially in the Linked List.
        
        Parameters: node1 is a node object.
            node2 is a node object.
        
        Returns: None."""
        node2._next = node1._next
        node1.set_next(node2)

    def sort(self):
        """Imported from CloudCoder/short problems. Sorts a Linked List by
            checking the value of the _count attribute of each node and
            sorting it in descending order.
        
        Parameters: None.
        
        Returns: None."""
        ll = LinkedList()
        if self._head != None and self._head._next != None:
            while self._head != None:
                current = self._head
                self._head = current._next
                if ll._head == None or ll._head._count <= current._count:
                    ll.add(current)
                else:
                    current_2 = ll._head
                    while current_2 != None:
                        if current_2._next == None or \
                        current_2._next._count <= current._count:
                            current._next = current_2._next
                            current_2._next = current
                            break
                        current_2 = current_2._next
            self._head = ll._head

    def get_nth_highest_count(self, n):
        """Returns the _count attribute of the nth node in a Linked List.
        
        Parameters: n is the number representing the nth node who's _count
            attribute you want in a Linked List.
        
        Returns: An integer that represents the _count attribute of a node."""
        counter = 0
        current = self._head
        while counter != n:
            if current == None:
                return None
            counter += 1
            current = current._next
        return current._count
    
    def print_upto_count(self, n):
        """Traverses through a Linked List and prints out the _word and _count
            attribute of each node in the Linked List who's _count attribute
            is at least n.
        
        Parameters: n is an integer.
        
        Returns: None."""
        current = self._head
        while current != None:
            if current._count >= n:
                print("{} : {:d}".format(current._word, current._count))
            current = current._next
    
    def __str__(self):
        """If the Linked List is empty, then None is printed out. Otherwise,
            the word of the first node in the Linked List is printed out.
        
        Parameters: None.
        
        Returns: The _word attribute of the first node in a Linked List. If
            the Linked List is empty, then it returns None."""
        if self._head != None:
            return self._head._word
        return None
        
    def add(self, node):
        """Adds a node into a Linked List at the front.
        
        Parameters: node is the node object that you want to insert into the
            Linked List,
        
        Returns: None."""
        node._next = self._head
        self._head = node


def remove_punctuation(line):
    """Takes a csv line and strips it of any extra punctuation as well as
        only returning the line that represents the title of an article.
        
    Parameters: line is a line in a csv file.
        
    Returns: A string that represents the title of the article after being
        stripped of any extra punctuation."""
    empty_string = ""
    if "title" not in line:
        for letter in line[4]:
            if letter not in string.punctuation:
                empty_string += letter
            else:
                empty_string += " "
    return empty_string

def remove_whitespace(a_string):
    """Removes any whitespace in the title of an article.
        
    Parameters: a_string is a string that is the title of an article.
        
    Returns: A string that is the title of an article after having been
        stripped of whitespace."""
    string_to_list = ""
    for element in a_string:
        if element not in string.whitespace:
            string_to_list += element
        else:
            string_to_list += " "
    return string_to_list

def remove_small_words(a_list):
    """Removes any words in a list whose length is not at least 3.
        
    Parameters: a_list is a list of strings
        
    Returns: A new list that is the old list except it doesn't contain any
        strings with a length of less than 3."""
    index = 0
    while index != len(a_list):
        if len(a_list[index]) <= 2:
            del a_list[index]
        else:
            index += 1
    return a_list

def main():
    readfile = csv.reader(open(input(), "r"))
    x = LinkedList()

    for line in readfile:
        string_to_list = remove_punctuation(line)
        string_to_list = remove_whitespace(string_to_list)
        string_to_list = string_to_list.split()
        string_to_list = remove_small_words(string_to_list)
        for word in string_to_list:
            x.update_count(word.lower())

    n = input()
    x.sort()
    k = x.get_nth_highest_count(int(n))
    x.print_upto_count(k)

main()
