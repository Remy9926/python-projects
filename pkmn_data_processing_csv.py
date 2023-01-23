"""
    Takes a CSV file that contains Pokemon and their stats and
        computes the total average of each stat per Pokemon type and
        answers queries about these averages.
"""


def establish_dictionaries(x, dict_of_pkmn, dict_of_types):

    """Takes the Pokemon in a CSV file and computes the averages of each stat
    for each type of Pokemon.
    Parameters: x is the CSV file that contains the Pokemon and their stats.
        dict_of_pkmn is a dictionary that will include each Pokemon as keys
        and their corresponding stats as values.
        dict_of_types is a dictionary that has the Pokemon types as keys and
        the values are a dictionary of the Pokemon that match the type and
        the values of the second dictionary are the corresponding Pokemon's
        stats.
    Returns: None.
    """

    empty_string = ""

    for line in x:
        
        pkmn_name = ""
        counter = 0
        
        if line[0] != "#":
            
            for char in line:

                if counter == 1:
                        
                    if char != ",":

                        pkmn_name += char

                    if char == ",":

                        counter += 1
                        dict_of_pkmn[pkmn_name] = {}
                
                elif counter == 2:
                    
                    if char != ",":

                        empty_string += char
                    
                    if char == ",":

                        counter += 1
                        dict_of_pkmn[pkmn_name]["type"] = empty_string
                        empty_string = ""
                
                elif counter == 3:

                    if char != ",":

                        empty_string += char
                    
                    if char == ",":

                        counter += 1
                        dict_of_pkmn[pkmn_name]["type 2"] = empty_string
                        empty_string = ""

                elif counter == 4:

                    if char != ",":

                        empty_string += char
                    
                    if char == ",":

                        counter += 1
                        dict_of_pkmn[pkmn_name]["total"] = int(empty_string)
                        empty_string = ""

                elif counter == 5:

                    if char != ",":

                        empty_string += char
                    
                    if char == ",":

                        counter += 1
                        dict_of_pkmn[pkmn_name]["hp"] = int(empty_string)
                        empty_string = ""

                elif counter == 6:

                    if char != ",":

                        empty_string += char
                    
                    if char == ",":

                        counter += 1
                        dict_of_pkmn[pkmn_name]["attack"] = int(empty_string)
                        empty_string = ""
                
                elif counter == 7:

                    if char != ",":

                        empty_string += char
                    
                    if char == ",":

                        counter += 1
                        dict_of_pkmn[pkmn_name]["defense"] = int(empty_string)
                        empty_string = ""

                elif counter == 8:

                    if char != ",":

                        empty_string += char
                    
                    if char == ",":

                        counter += 1
                        dict_of_pkmn[pkmn_name]["specialattack"]\
                            = int(empty_string)
                        empty_string = ""
                
                elif counter == 9:

                    if char != ",":

                        empty_string += char
                    
                    if char == ",":

                        counter += 1
                        dict_of_pkmn[pkmn_name]["specialdefense"]\
                            = int(empty_string)
                        empty_string = ""

                elif counter == 10:

                    if char != ",":

                        empty_string += char
                    
                    if char == ",":

                        counter += 1
                        dict_of_pkmn[pkmn_name]["speed"] = int(empty_string)
                        empty_string = ""

                elif counter == 11:

                    if char != ",":

                        empty_string += char
                    
                    if char == ",":

                        counter += 1
                        dict_of_pkmn[pkmn_name]["generation"]\
                            = int(empty_string)
                        empty_string = ""
                
                elif counter == 12:

                    if char != ",":

                        empty_string += char

                    if char == line[len(line) - 1]:

                        counter += 1
                        dict_of_pkmn[pkmn_name]["legendary"]\
                            = empty_string.strip("\n")
                        empty_string = ""

                elif char == ",":

                    counter += 1

    for pkmn in dict_of_pkmn:

        if dict_of_pkmn[pkmn]["type"] not in dict_of_types:

            dict_of_types[dict_of_pkmn[pkmn]["type"]] = {}
        
        dict_of_types[dict_of_pkmn[pkmn]["type"]][pkmn] = dict_of_pkmn[pkmn]


    for type in dict_of_types:

        number_of_mons = 0
        sum_of_total = 0
        sum_of_hp = 0
        sum_of_attack = 0
        sum_of_defense = 0
        sum_of_specialattack = 0
        sum_of_specialdefense = 0
        sum_of_speed = 0

        for pkmn in dict_of_types[type]:

            sum_of_total += dict_of_types[type][pkmn]["total"]
            sum_of_hp += dict_of_types[type][pkmn]["hp"]
            sum_of_attack += dict_of_types[type][pkmn]["attack"]
            sum_of_defense += dict_of_types[type][pkmn]["defense"]
            sum_of_specialattack +=\
                dict_of_types[type][pkmn]["specialattack"]
            sum_of_specialdefense +=\
                dict_of_types[type][pkmn]["specialdefense"]
            sum_of_speed += dict_of_types[type][pkmn]["speed"]
            number_of_mons += 1

        dict_of_types[type]["avg_total"] = sum_of_total / number_of_mons
        dict_of_types[type]["avg_hp"] = sum_of_hp / number_of_mons
        dict_of_types[type]["avg_attack"]\
            = sum_of_attack / number_of_mons
        dict_of_types[type]["avg_defense"]\
            = sum_of_defense / number_of_mons
        dict_of_types[type]["avg_specialattack"]\
            = sum_of_specialattack / number_of_mons
        dict_of_types[type]["avg_specialdefense"]\
            = sum_of_specialdefense / number_of_mons
        dict_of_types[type]["avg_speed"] = sum_of_speed / number_of_mons

x = input()
dict_of_pkmn = {}
dict_of_types = {}
x = open(x, "r")
user_input = None

establish_dictionaries(x, dict_of_pkmn, dict_of_types)

x.close()

while user_input != "":

    user_input = input()
    a_string = "avg_"

    if user_input.lower() == "total"\
        or user_input.lower() == "hp"\
            or user_input.lower() == "attack"\
                or user_input.lower() == "defense"\
                    or user_input.lower() == "specialattack"\
                        or user_input.lower() == "specialdefense"\
                            or user_input.lower() == "speed":
        
        max_average = None
        a_string += user_input.lower()
        
        for type in dict_of_types:
            
            if max_average == None or dict_of_types[type][a_string]\
                > max_average:

                max_average = dict_of_types[type][a_string]
                a_list = []
                a_list.append(type)
            
            elif dict_of_types[type][a_string] == max_average:
                a_list.append(type)

        a_list.sort()
        
        for pokemon_type in a_list:

            print("{}: {}".format(pokemon_type, max_average))
            print(dict_of_types)
