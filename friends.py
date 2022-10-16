"""
    File: friends.py
    Author: Ethan Huang
    Purpose: Create a Linked List of nodes that consist of peoples' names and
        each node contains a Linked List attribute, which consists of the
        names of people that that person is friends with. Then, take two names
        and print out any mutual friends between the two people.
    CSC 120 FA22 001
"""

from linked_list import LinkedList, Node


def create_dict_of_names(x, adict):
    """Takes a file and a dictionary and for each name in the file if the
        name is not already in the dictionary, it gets added to the
        dictionary. The key is a name and the value is a list, which
        consists of other names that are friends of that person.

    Parameters: x is a file with each line containing two names.
        adict is a dictionary.
    
    Returns: None."""
    for line in x:
        names = line.strip("\n\t ").split()
        if names[0] not in adict:
            adict[names[0]] =  []
        if names[1] not in adict[names[0]]:
            adict[names[0]].append(names[1])
        if names[1] not in adict:
            adict[names[1]] = []
        if names[0] not in adict[names[1]]:
            adict[names[1]].append(names[0])

def add_friends_to_node(adict, ll):
    """Takes a dictionary and a Linked List object and each key in the
        dictionary gets added into the Linked List as a node. Then, for
        each friend that corresponds to a certain name, another node is added
        to that person's friend attribute.

    Parameters: adict is a dictionary whose keys are names and values are a
        list of names.
        ll is a Linked List object.

    Returns: None."""
    for name in adict:
        ll.add(Node(name))
    for name in adict:
        current = ll._head
        while current._name != name:
            current = current._next
        for person in adict[name]:
            current.add_friend(Node(person))

def get_friends_of(ll, name):
    """Takes a Linked List object and a name and finds the names of that
        person's friends.
        
    Parameters: ll is a Linked List.
        name is a string representation of the name of the person whose
        friends you want to find.
    
    Returns: A list that contains the names of the specified person's
        friends."""
    alist = []
    current = ll._head
    while current._name != name:
        current = current._next
    current = current._friends._head
    while current != None:
        alist.append(current._name)
        current = current._next
    return alist

def find_mutuals_of(ll, name, alist):
    """Takes a Linked List, a name, and a list of friends to find any mutual
        friends.
    
    Parameters: ll is a Linked List object that consists of nodes that have
        peoples' names.
        name is a string representation of the name of the person you want to
        find mutuals of.
        alist is a list of strings with each string representing a person's
        name.
    
    Returns: A list that contains any mutual friends."""
    mutuals = []
    current = ll._head
    while current._name != name:
        current = current._next
    current = current._friends._head
    while current != None:
        if current._name in alist:
            mutuals.append(current._name)
        current = current._next
    return mutuals

def known_or_unknown(adict, name1, name2):
    """Takes a dictionary and 2 string representations of names and determines
        whether or not the names are keys in the dictionary. If not, it prints
        out an error message and returns False. Otherwise, it returns True.
    
    Parameters: adict is a dictionary with names as its keys.
        name1 is a string representation of a name.
        name2 is a string representation of a name.
    
    Returns: False if either name1 or name2 is not in adict.
        True if they are both in adict."""
    if name1 not in adict:
        print("ERROR: Unknown person " + name1)
        return False
    if name2 not in adict:
        print("ERROR: Unknown person " + name2)
        return False
    return True

def main():
    x = open(input("Input file: "), "r")
    adict = {}
    create_dict_of_names(x, adict)
    x.close()
    ll = LinkedList()
    add_friends_to_node(adict, ll)
    name1 = input("Name 1: ")
    name2 = input("Name 2: ")
    known = known_or_unknown(adict, name1, name2)
    if known == True:
        friends = get_friends_of(ll, name1)
        mutuals = find_mutuals_of(ll, name2, friends)
        if mutuals != []:
            i = 0
            mutuals.sort()
            print("Friends in common:")
            while i != len(mutuals):
                print(mutuals[i])
                i += 1

main()