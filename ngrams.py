"""
    File: ngrams.py
    Author: Ethan Huang
    Purpose: Reads a file, creates n-grams of a specified length, and returns
        the n-grams that occur most often in the file.
    CSC 120 FA22 001
"""

class Input():
    def __init__(self):
        """Instantiates an Input object which has 3 attributes. The _n
            attribute is the length of n-grams that want to be found.
            _file is the file object that is opened, and _wordlist is a
            list of the words from the file object.
        
        Parameters: None.

        Returns: None."""
        
        self._file = open(input(), "r")
        self._n = int(input())
        self._wordlist = self.wordlist()
        
    def wordlist(self):
        """Takes a string and splits it by spaces, removes all punctuation on
            the outside of each string, and returns the new list like that.

        Parameters: None.

        Returns: A list that represents the original string, after it has
            been processed."""

        new_list = []
        for line in self._file:
            split_line = line.split(" ")
            for i in range(len(split_line)):
                if split_line[i].strip(" :,;!?'-\n").strip('".()$&,!?_') != "":
                    new_list.append\
                        (split_line[i].strip(" :,;!?'-\n").strip('".()$&'))
        return new_list

class Ngrams():
    def __init__(self):
        """Instantiates a Ngrams object as well as a Input object and assigns
            the Input object to the _input attribute of the Ngrams object.
            A dictionary is then created for the _dict attribute of the Ngrams
            object and proceeds to find the n-grams.

        Parameters: None.

        Returns: None."""

        self._input = Input()
        self._dict = {}
        self.process_wordlist(self._input._wordlist)
    
    def update(self, ngram):
        """Increments or initializes the dictionary value for an n-gram.

        Parameters: ngram is the n-gram of the n-gram whose value is to be
            initialized or incremented.
        
        Returns: None"""

        if ngram not in self._dict:
            self._dict[ngram] = 1
        else:
            self._dict[ngram] += 1
    
    def process_wordlist(self, wordlist):
        """Searches for the n-grams within a list of strings, wordlist.
        
        Parameters: wordlist is a list of strings.
        
        Returns: None."""

        for i in range(len(wordlist) - self._input._n + 1):
            empty_string = ""
            for j in range(self._input._n):
                if j != self._input._n - 1:
                    empty_string += wordlist[i +j] + " "
                else:
                    empty_string += wordlist[i +j]
                    self.update(empty_string.lower())

    def print_max_ngrams(self):
        """Searches through a Ngrams object's dictionary for the n-grams
            that occur most often. Then proceeds to print them out in
            a specified format.
        
        Parameters: None.

        Returns: None."""

        M = None
        for element in self._dict:
            if M == None or M < self._dict[element]:
                M = self._dict[element]
        for ngram_string in sorted(self._dict):
            if self._dict[ngram_string] == M:
                print("{:d} -- {}".format(M, ngram_string))


def main():
    Ngrams().print_max_ngrams()

main()