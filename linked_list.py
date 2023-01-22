"""
    Implements the Linked List class and Node class so that
        the file linked_list_friend.py can import this file and use those classes.
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

    def sort(self):
        """Sorts the names in a Linked List by alphabetical order.
        
        Parameters: None.
        
        Returns: None."""
        ll = LinkedList()
        if self._head != None and self._head._next != None:
            while self._head != None:
                current = self._head
                self._head = current._next
                if ll._head == None or ll._head._name >= current._name:
                    ll.add(current)
                else:
                    current_2 = ll._head
                    while current_2 != None:
                        if current_2._next == None or \
                        current_2._next._name >= current._name:
                            current._next = current_2._next
                            current_2._next = current
                            break
                        current_2 = current_2._next
            self._head = ll._head

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
