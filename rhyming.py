"""
    Takes a file to establish a dictionary of words and their
        phonemes. Then, takes in user input and finds words that are perfect
        rhymes to the word input by the user.
"""


def establish_dictionary(dictionary):
    """Takes a file and reads through it separating each word from its
    phonemes and establishes a dictionary using the word as a key and
    a list of its phonemes as the value.

    Parameters: dictionary is the dictionary that you want to create
        key-value pairs for.

    Returns: None.
    """

    pfile = input()
    pfile = open(pfile, "r")
    
    for line in pfile:

        phoneme_list = []

        for index in range(len(line.strip("\n").split(" "))):

            if index == 0:
                
                if line.strip("\n").split(" ")[index] not in dictionary:
                    
                    dictionary[line.strip("\n").split(" ")[index]] = []
            
            else:

                if line.strip("\n").split(" ")[index] != "":

                    phoneme_list.append(line.strip("\n").split(" ")[index])
            
            if index == len(line.strip("\n").split(" ")) - 1:

                dictionary[line.strip("\n").split(" ")[0]].append(phoneme_list)
        
    pfile.close()


new_dict = {}
rhyming_words = []

establish_dictionary(new_dict)

user_input = input()
for list in new_dict[user_input.upper()]:
    
    index_of_primary_stress = None
    list_of_remaining_phonemes = None

    for index in range(len(list)):

        if "1" in list[index]:

            index_of_primary_stress = index
        
            list_of_remaining_phonemes = list[index:]

    for word in new_dict:
        
        for index in range(len(new_dict[word])):
            
            index_2_of_primary_stress = None
            list_2_of_remaining_phonemes = None

            for index_2 in range(len(new_dict[word][index])):

                if "1" in new_dict[word][index][index_2]:

                    index_2_of_primary_stress = index_2
                    list_2_of_remaining_phonemes\
                        = new_dict[word][index][index_2:]
            
            if list_of_remaining_phonemes == list_2_of_remaining_phonemes:
                
                if list[index_of_primary_stress - 1]\
                    != new_dict[word][index][index_2_of_primary_stress - 1]:

                    rhyming_words.append(word)
    
rhyming_words.sort()

for word in rhyming_words:

    print(word)
