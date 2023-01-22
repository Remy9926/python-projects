"""
    Takes two integers and creates a list of lists (grid) of the
        specified length and width and prints the elements of each list as
        comma-separated values.
"""

import random

def init():

    """Takes two integers; assigns them to the variables grid_size and
    seed_value, respectively; and generates a seed based off of the
    value of seed_value.

    Parameters: This function does not take any parameters.

    Returns: The value of variable grid_size.

    Pre-condition: The inputs of grid_size and seed_value are integers.

    Post-condition: The return value is an integer."""

    grid_size = int(input())
    seed_value = input()
    random.seed(seed_value)

    return grid_size

def make_grid(grid_size):

    """Utilizes the seed to randomly select 1 letter of the alphabet at a
    time to create a list of lists of length and width grid_size.

    Parameters: grid_size is the length and width of the list of lists
    (grid).

    Returns: A newly created list of lists (grid).

    Pre-condition: grid_size is an integer.

    Post-condition: The return value is a list of lists."""

    string = "abcdefghijklmnopqrstuvwxyz"
    new_grid = []

    for num in range(grid_size):
        
        counter = 0
        temp_grid = []
        
        while counter != grid_size:
            temp_grid.append(string[random.randint(0, 25)])
            counter += 1
        
        new_grid.append(temp_grid)
        temp_grid = []
    
    return new_grid

def print_grid(grid):

    """Takes a list of lists and prints out the elements of each individual
    list as comma-separated values.

    Parameters: grid is a list of lists.

    Returns: The elements of grid printed out as comma-separated values.

    Pre-condition: grid is a list of lists.

    Post-condition: The return value is the elements of grid printed out."""

    for list in grid:

        new_string = ""

        for index in range(len(list)):

            if index != len(list) - 1:

                new_string += list[index] + ","
            
            else:

                new_string += list[index]
                print(new_string)

def main():

    """Utilizes the functions init, make_grid, and print_grid in order
    to print out the elements of a randomly created list of lists.

    Parameters: None.

    Returns: None.

    Pre-condition: The functions init, make_grid, and print_grid exist
    and these functions' parameters are input properly.

    Post-condition: Comma-separated values printed out."""

    print_grid(make_grid(init()))

main()
