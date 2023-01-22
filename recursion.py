"""
    Take a single line of input that is supposed to represent a
        street and use recursion to print out an ASCII rendering of the
        street.
"""

def get_heights(x, alist):
    """Takes a list of the ASCII representations of street objects and
        a list and appends the heights of each representation to the list.
    
    Parameters: x is a list of ASCII representations of the street objects.
        alist is an empty list that will have the heights appended to.
    
    Returns: A list containing all the heights of the street objects."""
    if x == []:
        return alist
    else:
        if x[0][0] == "p":
            alist.append(int(5))
            return get_heights(x[1:], alist)
        elif x[0][0] == "e":
            alist.append(int(1))
            return get_heights(x[1:], alist)
        else:
            y = x[0].split(":", 1)
            y = y[1].split(",")[1]
            alist.append(int(y))
            return get_heights(x[1:], alist)
    return alist

def get_width(x):
    """Takes a list of the ASCII representations of different street objects,
        and finds the total width of all the objects combined.
    
    Parameters: x is a list of ASCII representations of street objects.

    Returns: The sum of the widths of each street object."""
    if x == []:
        return 0
    else:
        y = x[0].split(":", 1)
        return int(y[1].split(",")[0]) + get_width(x[1:])

def get_max_height(x):
    """Takes a list and returns the greatest value in the list.
    
    Parameters: x is a list of integers.
    
    Returns: A number that represents the greatest number in the list."""
    if x == []:
        return 0
    else:
        if x[0] > get_max_height(x[1:]):
            return x[0]
        else:
            return get_max_height(x[1:])

def build_building(width, height, brick, astring, height2):
    """Creates a building street object with a specified width, height, and
        brick recursively. Each step adds the row to an empty string, and if
        the maximum height is greater than the height of the building,
        additional whitespaces are added to the string.
        
    Parameters: width is the width of the building.

        height is the height of the building.

        brick is the string that the building is made up of.

        astring is an empty string that will be returned.

        height2 is the maximum height of all the objects in the original
            string representation of the street objects.
        
        Returns: A building street object representation."""
    if height != height2:
        astring += " " * width + "\n"
        return build_building(width, height, brick, astring, height2 - 1)
    else:
        if height == 1:
            astring += (brick * width)
            return astring
        else:
            astring += (brick * width + "\n")
            return \
                build_building(width, height - 1, brick, astring, height2 - 1)

def build_park(width, foliage, num, astring, height):
    """Creates a park street object by taking in the width, its foliage,
        and the height (num). Each recursive step adds to an empty string and
        if the height of the park is less than the maximum height of all
        street objects, then additional whitespaces are added to the string.
        
        Parameters: width is an integer that represents the width of the park.
        
            foliage is the string that the tree leaves of the park consist of.
            
            num is the number 5, which is the height of any park.
            
            astring is an empty string that will be returned.
            
            height is the maximum height of all objects in the original string
                representation of the street.
        
        Returns: A park street object representation."""
    if height != num:
        astring += " " * width + "\n"
        return build_park(width, foliage, num, astring, height - 1)
    else:
        half = width // 2
        if num == 1:
            astring += ((" " * half) + "|" + (" " * half))
            return astring
        if num == 2:
            astring += ((" " * half) + "|" + (" " * half) + "\n")
            return build_park(width, foliage, num - 1, astring, height - 1)
        if num == 3:
            astring += \
                (" " * (half - 2)) + (foliage * 5) + (" " * (half - 2)) + "\n"
            return build_park(width, foliage, num - 1, astring, height - 1)
        if num == 4:
            astring += \
                (" " * (half - 1)) + (foliage * 3) + (" " * (half - 1) + "\n")
            return build_park(width, foliage, num - 1, astring, height - 1)
        else:
            astring += ((" " * half) + foliage + (" " * half) + "\n")
            return build_park(width, foliage, num - 1, astring, height - 1)

def build_empty_lot(width, trash, astring, height):
    """Creates an empty lot street object with the given width and trash. Each
        recursive step adds to an empty string. If the height of the empty lot
        is less than the maximum height of the street, then additional
        whitespace is added to the string.
        
    Parameters: width is the width of the empty lot.
        
        trash is the string that is repeated in the empty lot.
        
        astring is the string that will be returned.
        
        height is the maximum height of all objects in the original string
            representation of the street.
    
    Returns: An empty lot street object representation."""
    if height > 1:
        astring += " " * width + "\n"
        return build_empty_lot(width, trash, astring, height - 1)
    else:
        if width < len(trash):
            astring += trash[0:width]
            return astring
        else:
            astring += trash
            return build_empty_lot(width - len(trash), trash, astring, height)

def process_empty_lot(empty_lot):
    """Processes an empty lot string representation by converting any
        underscores in it into empty spaces.
        
    Parameters: empty_lot is a string representation of an empty lot.
    
    Returns: The processed empty lot street object string."""
    if empty_lot == "":
        return ""
    else:
        if empty_lot[0] == "_":
            return " " + process_empty_lot(empty_lot[1:])
        else:
            return empty_lot[0] + process_empty_lot(empty_lot[1:])

def run_through_list(alist, alist2, height):
    """Iterates through a list of the string representations of different
        street objects and appends the corresponding street object into
        an empty list.
    
    Parameters: alist is a list of string representations of street objects.
    
        alist2 is an empty list that will be appended to.
        
        height is the maximum height of the street so that the street objects
            can be created while knowing the maximum height."""
    if alist == []:
        return alist2
    else:
        x = alist[0].split(":", 1)
        y = x[1].split(",")
        if x[0] == "b":
            alist2.append(build_building \
                (int(y[0]), int(y[1]), y[2], "", height))
            return run_through_list(alist[1:], alist2, height)
        elif x[0] == "p":
            alist2.append(build_park(int(y[0]), y[1], 5, "", height))
            return run_through_list(alist[1:], alist2, height)
        else:
            alist2.append(process_empty_lot \
                (build_empty_lot(int(y[0]), y[1], "", height)))
            return run_through_list(alist[1:], alist2, height)

def create_grid(alist, alist2):
    """Takes a list of ASCII renderings of the street objects and splits up 
        each street object by an indented line to get each row of the object.
        
    Parameters: alist is a list of the ASCII renderings of different street
        objects.
    
        alist2 is the a list of lists containing a list of each street
            object's rows.
        
    Returns: A list of lists of each street object's rows."""
    if alist == []:
        return alist2
    else:
        alist2.append(alist[0].split("\n"))
        return create_grid(alist[1:], alist2)

def get_col(alist, num):
    """Takes a list of lists and returns the concatenation of all elements
        at the num index of each list.
    
    Parameters: alist is a list of lists.
    
    num is an integer that is representative of the nth index of a list of
        lists.
    
    Returns: A string that represents the concatenation of all elements at the
        num index of each list in the list of lists."""
    if alist == []:
        return ""
    else:
        return alist[0][num] + get_col(alist[1:], num)

def iterate_through_list(alist, astring, num):
    """Iterate through each column per row in a list of a lists to get the
        concatenation of all items in that row and add it to an empty string
        row by row.
        
    Parameters: alist is a list of lists that represent the different street
        objects on the street.
    
    astring is an empty string that is added to and returned.
    
    num is the maximum height of street representation.
    
    Returns: The final representation of the street including being surrounded
        by a border."""
    if num == 1:
        astring += "|" + get_col(alist, -num) + "|"
        return astring
    else:
        astring += "|" + get_col(alist, -num) + "|" + "\n"
        return iterate_through_list(alist, astring, num - 1)


def main():
    x = input("Street: ")
    x = x.split()
    height = get_max_height(get_heights(x, [])) + 1
    width = get_width(x)
    print("+" + ("-" * width) + "+")
    listy = run_through_list(x, [], height)
    listy = create_grid(listy, [])
    print(iterate_through_list(listy, "", height))
    print("+" + ("-" * width) + "+")

main()
