"""
    File: linked_list.py
    Author: Ethan Huang
    Purpose: Implements the Linked List class and Node class so that
        the file friends.py can import this file and use those classes.
    CSC 120 FA22 001
"""

class LinkedList():
    def __init__(self):
        """Instantiates a Linked List object with its head attribute set
            to None.
        
        Parameters: None.
        
        Returns: None."""
        self._head = None

    def add(self, node):
        """Adds a node to the beginning of the Linked List.
        
        Parameters: node is a Node object.
        
        Returns: None."""
        node._next = self._head
        self._head = node
    
    def is_empty(self):
        """Returns whether or not the Linked List is empty or not.
        
        Parameters: None.
        
        Returns: A boolean depending on whether or not the list is empty."""
        return self._head == None

class Node():
    def __init__(self, name):
        """Instantiates a Node object with its name attribute set to name,
            a friends attribute instantiating a Linked List object, and its
            next attribute set to None.
        
        Parameters: name is a string.
        
        Returns: None."""
        self._name = name
        self._friends = LinkedList()
        self._next = None

    def add_friend(self, node):
        """Adds a node to the friends attribute of a Node object.
        
        Parameters: node is the node you want to add to the friends attribute.
        
        Returns: None."""
        self._friends.add(node)