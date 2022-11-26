"""
    File: writer_bot_ht.py
    Author: Ethan Huang
    Purpose: Simulate a Markov Chain Algorithm to generate text based on
        preceding words while manually implementing a Hashtable without
        using Python dictionaries.
    CSC 120 FA22 001
"""

import sys
import random

class Hashtable:
    def __init__(self, size):
        """Initializes the Hashtable object with two attributes, pairs
            and size.
        
        Parameters: size is the size of the Hashtable.
        
        Returns: None."""
        self._pairs = [None] * size
        self._size = size
    
    def pairs(self):
        return self._pairs
    
    def size(self):
        return self._size
    
    def put(self, key, value):
        """Places a key-value pair into the Hashtable's table if its hash is
            empty. On collision, performs linear probing to find the next
            available spot in the Hashtable.
            
        Parameters: key is the key of the key-value pair.
            value is the value of the key-value pair.
            
        Returns: None."""
        hash = self._hash(key)
        if self.pairs()[hash] == None:
            self.pairs()[hash] = [key, [value]]
        
        elif self.pairs()[hash][0] == key:
            self.pairs()[hash][1].append(value)
        
        elif self.pairs()[hash][0] != key:
            hash -= 1
            while self.pairs()[hash] != None:
                if hash < 0:
                    hash = len(self.pairs()) - 1
                if self.pairs()[hash][0] == key:
                    self.pairs()[hash][1].append(value)
                    return
                hash -= 1
            self.pairs()[hash] = [key, [value]]

    def get(self, key):
        """Returns the value given the key from the Hashtable. Returns None
            if the key does not exist in the Hashtable.
        
        Parameters: key is the key whose value you want to search for.
        
        Returns: the value of the corresponding key-value pair. 
            None if the key does not exist in the Hashtable."""
        hash = self._hash(key)
        if self.pairs()[hash][0] == key:
            return self.pairs()[hash][1]
        if self.pairs()[hash][0] != key:
            hash -= 1
        while hash != self._hash(key):
            if hash < 0:
                hash = len(self.pairs()) - 1
            if self.pairs()[hash][0] == key:
                return self.pairs()[hash][1]
            hash -= 1
        return None

    def __contains__(self, key):
        """Returns True if a give key is in the Hashtable and False if not.
        
        Parameters: key is the key that you want to search for in the
            Hashtable.
            
        Returns: True if the key is found in the Hashtable.
            False if the key is not found in the Hashtable."""
        if self.get(key) == None:
            return False
        return True

    def _hash(self, key):
        """Uses Horner's Rule to hash a given key.
        
        Parameters: key is the key that you want to hash.
        
        Returns: The resulting hash from the given key."""
        p = 0
        for c in key:
            p = 31*p + ord(c)
        return p % self._size

def create_list_from_file(sfile):
    """Takes a file and for each line in the file, splits up the words in
        each line and adds it to a list.
        
    Parameters: sfile is a file object that is being read.
    
    Returns: a list containing all the words in sfile."""
    alist = []
    for line in sfile:
        line = line.split()
        alist += line
    return alist

def put_into_hashtable(words, adict, alist):
    """Takes a list of words, a Hashtable object, and another list and places
        the corresponding key-value pairs into the Hashtable.
        
    Parameters: words is a list of all the words that you want to place
        into the Hashtable.
        adict is a Hashtable object.
        alist is a list that will only contain a certain number of strings
            within it at any given time. The strings within will be used
            as the keys within the Hashtable.
                
    Returns: None."""
    for x in range(len(words)):
        val = " ".join(alist)
        adict.put(val, words[x])
        alist.append(words[x])
        alist = alist[1:]

def generate_output_list(alist, adict, num_words):
    """Takes a list, a Hashtable object, and a specified length and creates
        a list of words that will be converted into a sentence.
        
    Parameters: alist is a list of strings that will be used as the keys to
        search for values within the Hashtable.
        adict is a Hashtable object.
        num_words is the total number of words that will be generated.
        
    Returns: a list that contains the randomly generated words."""
    output = []
    i = 0
    while len(output) != num_words:
        key = " ".join(alist)
        val = adict.get(key)
        if len(val) > 1:
            output.append(val[random.randint(0, len(val) - 1)])
        
        elif len(val) == 1:
            output.append(val[0])
        
        alist.append(output[i])
        alist = alist[1:]
        i += 1
    return output

def generate_sentence(output):
    """Takes a list of strings and adds every 10 of them together.
        Once the length of the string exceeds 10, the function goes to
        a new line and adds the next 10 strings within the list.
    
    Parameters: output is a list of strings that will be added together.
    
    Returns: The resulting string from adding the strings within output."""
    sentence = ""
    astring = ""
    
    while len(output) > 10:
        astring = " ".join(output[0:10])
        sentence += astring + "\n"
        astring = ""
        output = output[10:]
    
    sentence += " ".join(output)
    return sentence

def main():
    SEED = 8
    NONWORD = "@"
    random.seed(SEED)
    sfile = open(input(), "r")
    M = int(input())
    n = int(input())
    num_words = int(input())
    if n < 1:
        print("ERROR: specified prefix size is less than one")
        sys.exit(0)
    if num_words < 1:
        print("ERROR: specified size of the generated text is less than one")
        sys.exit(0)

    words = create_list_from_file(sfile)

    adict = Hashtable(M)
    alist = [NONWORD] * n

    put_into_hashtable(words, adict, alist)

    alist = [NONWORD] * n
    output = generate_output_list(alist, adict, num_words)

    final = generate_sentence(output)
    print(final)

main()