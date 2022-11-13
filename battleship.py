"""
    File: battleship.py
    Author: Ethan Huang
    Purpose: Mimics a one sided game of Battleship where Player One's board
        is formed from one input and another input is used as the guesses 
        of Player Two. Player One's board layout is formed and Player Two's
        decisions are simulated within the program.
    CSC 120 FA22 001
"""

import sys

class GridPos():
    """The GridPos class represents one specific coordinate on the board with
        its own unique x and y coordinates. It also contains a reference to a
        Ship object if there is one on the coordinate and stores a boolean
        that represents whether ornot Player Two has already guessed this
        coordinate already or not.
    """
    def __init__(self, x, y):
        """Initializes a GridPos object by taking two arguments, each of which
            represents the objects x and y coordinates, respecitvely.
        
        Parameters: x and y are both integers.
        
        Returns: None."""
        self._x = x
        self._y = y
        self._ship = None
        self._guessed = False

    def set_ship(self, ship):
        """Sets the ship attribute of a GridPos object to a reference of a
            Ship object.
            
        Parameters: ship is a reference to a Ship object.
        
        Returns: None."""
        self._ship = ship
    
    def got_guessed(self):
        """Sets the guessed attribute of a GridPos object to True to show
            that it has been guessed.
            
        Paramters: None.
        
        Returns: None."""
        self._guessed = True

    def x(self):
        """Getter method for GridPos objects x attribute."""
        return self._x
    
    def y(self):
        """Getter method for GridPos objects y attribute."""
        return self._y
    
    def ship(self):
        """Getter method for GridPos objects ship attribute."""
        return self._ship
    
    def guessed(self):
        """Getter method for GridPos objects guessed attribute."""
        return self._guessed
    
    def __str__(self):
        """Represents a GridPos object as a string by returning its
            coordinates and if there is a ship on it, the Ship object.
        
        Parameters: None.
        
        Returns: a string representation of a GridPos object."""
        return ("Coordinates: (" + str(self.x()) + ", " + str(self.y()) + ")" + "\n" + "Ship: " + str(self.ship()))

class Board():
    """The Board class represents a 10x10 board, on top of which the game of
        Battleship takes place."""
    def __init__(self):
        """Initializes a Board object as a 2D list and if the 2D list is
            viewed with each list on top of each other, the coordinate (0,0)
            will be in the bottom left and the coordinate (9,9) in the
            uppermost right.
            
        Parameters: None.
        
        Returns: None."""
        alist = []
        for num in range(10):
            alist2 = []
            for num2 in range(10):
                x = GridPos(num, num2)
                alist2.append(x)
            alist.append(alist2)
        self._board = alist[::-1]
        self._ships = None
    
    def set_ship_list(self, ship_list):
        """Sets the ships attribute of a Board object to a list of references
            to Ship objects.
            
        Parameters: ship_list is a list of Ship objects.
        
        Returns: None."""
        self._ships = ship_list
    
    def board(self):
        """Getter method for the board attribute of a Board object."""
        return self._board

    def ships(self):
        """Getter method for the ships attribute of a Board object."""
        return self._ships

    def __str__(self):
        """Represents a Board object as a string by printing out its list of
            references to Ship objects.
            
        Parameters: None.
        
        Returns: the string representation of the list of ship references
            within the Board object."""
        return str(self.ships())

    def show_board(self):
        """Prints out the whole board with empty spaces as a dot and
            any occupied spaces are represented by the ship that occupies that
            space.
        
        Parameters: None.
        
        Returns: A string representation of the board."""
        astring = ""
        for row in self.board():
            astring2 = ""
            for column in row:
                if column.ship() == None:
                    astring2 += "."
                elif column.ship() != None:
                    astring2 += column.ship().ship()
            astring2 += "\n"
            astring += astring2
        return astring

class Ship():
    """The Ship class represents a ship in Battleship. It holds the attributes
        ship, size, positions, and safe. Ship is the abbreviated name of the
        ship, size is the number of spaces the ship takes up, positions is the
        coordinate points on which the ship is on, and safe is the coordinate
        points on which the ship is on that haven't been hit yet."""
    def __init__(self, ship, size):
        """Initialies a ship object with two parameters, which are its name
            and size.
            
        Parameters: ship is a string representation of the abbreviation of the
            ship.
        size is the number of spaces that the ship takes up.
        
        Returns: None."""
        self._ship = ship
        self._size = size
        self._positions = []
        self._safe = []
    
    def size(self):
        """Getter method for the size attribute of a Ship object."""
        return self._size
    
    def ship(self):
        """Getter method for the ship attribute of a Ship object."""
        return self._ship
    
    def set_position(self, x, y):
        """Adds the coordinate point (x,y) to a Ship object's list of
            positions and its spaces that it hasn't been attacked at yet.
        
        Parameters: x is the x coordinate of the coordinate location.
            y is the y coordinate of the coordinate location.
            
        Returns: None."""
        self._positions.append((x, y))
        self._safe.append((x, y))

    def positions(self):
        """Getter method for the positions attribute of a Ship object."""
        return self._positions
    
    def safe(self):
        """Getter method for the safe attribute of a Ship object."""
        return self._safe
    
    def hit(self, x, y):
        """Searches through the safe attribute of a Ship object upon being hit
            and removes it from the safe list because it has been attacked.
        
        Parameters: x is the x coordinate that is hit.
            y is the y coordinate that is hit.
            
        Returns: None."""
        i = 0
        while i != len(self.safe()):
            if self.safe()[i] == (y, 9 - x):
                self.safe().pop(i)
                break
            i += 1

    def __str__(self):
        """Returns the string representation of a Ship object, which is
            the ship's name and its list of positions that it occupies.
            
        Parameters: None.
        
        Returns: None."""
        return (self.ship() + ": " + str(self.positions()))


def placement_error(line):
    """Checks if a ship is placed horizontally or vertically. If not, returns
        an error message and stops the program.
    
    Parameters: line is the line in the input file in which the error occurs.
    
    Returns: None."""
    print("ERROR: ship not horizontal or vertical:" + line)
    sys.exit()

def out_of_bounds_error(line):
    """Checks if a ship is placed out of bounds. If so, returns
        an error message and stops the program.
    
    Parameters: line is the line in the input file in which the error occurs.
    
    Returns: None."""
    print("ERROR: ship out-of-bounds: " + line)
    sys.exit()

def overlapping_error(line):
    """Checks if a ship is placed over another. If so, returns
        an error message and stops the program.
    
    Parameters: line is the line in the input file in which the error occurs.
    
    Returns: None."""
    print("ERROR: overlapping ship: " + line)
    sys.exit()

def fleet_error():
    """Checks if there are 5 ships on the board. If not, returns
        an error message and stops the program.
    
    Parameters: None.
    
    Returns: None."""
    print("ERROR: fleet composition incorrect")
    sys.exit()

def ship_size_error(line):
    """Checks if a ship is of the right size. If not, returns
        an error message and stops the program.
    
    Parameters: line is the line in the input file in which the error occurs.
    
    Returns: None."""
    print("ERROR: incorrect ship size: " + line)
    sys.exit()

def illegal_guess():
    """Checks if a guess made is illegal or not. If so, returns
        an error message.
    
    Parameters: None.
    
    Returns: None."""
    print("illegal guess")

def create_ship_x(ship, val1, val2, misc_val):
    """Creates a Ship object and adds coordinates to its position attribute
        list based on the values that are passed through as arguments. The y
        coordinate of the ship's positions are all different.
        
    Parameters: ship is the name of the Ship object that is going to be
        created.
    val1 is the y coordinate of one of its edges.
    val2 is the y coordinate of its other edge.
    misc_val is the constant x coordinate of the ship.
    
    Returns: A reference to the new Ship object that is created."""
    if val1 < val2:
        new_ship = Ship(ship, val2 - val1 + 1)
        for num in range(val1, val2 + 1):
            new_ship.set_position(misc_val, num)
    if val1 > val2:
        new_ship = Ship(ship, val1 - val2 + 1)
        for num in range(val2, val1 + 1):
            new_ship.set_position(misc_val, num)
    return new_ship

def create_ship_y(ship, val1, val2, misc_val):
    """Creates a Ship object and adds coordinates to its position attribute
        list based on the values that are passed through as arguments. The x
        coordinate of the ship's positions are all different.
        
    Parameters: ship is the name of the Ship object that is going to be
        created.
    val1 is the x coordinate of one of its edges.
    val2 is the x coordinate of its other edge.
    misc_val is the constant y coordinate of the ship.
    
    Returns: A reference to the new Ship object that is created."""
    if val1 < val2:
        new_ship = Ship(ship, val2 - val1 + 1)
        for num in range(val1, val2 + 1):
            new_ship.set_position(num, misc_val)
    if val1 > val2:
        new_ship = Ship(ship, val1 - val2 + 1)
        for num in range(val2, val1 + 1):
            new_ship.set_position(num, misc_val)
    return new_ship

def miss(board, x_coord, y_coord):
    """If Player Two's attack is a miss, the function will print out miss, and
        set the GridPos object's guessed attribute to True if the coordinate
        has not been guessed yet. If the coordinate has been guessed before,
        the function will print miss (again).
    
    Parameters: board is the Board object that Player Two is attacking.
    x_coord is the x coordinate that Player Two is attacking.
    y_coord is the y coordinate that Player Two is attacking.
    
    Returns: None."""
    if board[x_coord][y_coord].guessed() == False:
        print("miss")
        board[x_coord][y_coord].got_guessed()
    elif board[x_coord][y_coord].guessed() == True:
        print("miss (again)")

def hit(board, x_coord, y_coord, ships_sunk):
    """If Player Two's attack hits a ship, the function will first check if
        the coordinate has been attacked before. If so, it wil print out
        hig (again). Otherwise, it will make the GridPos object's guessed
        attribute True and if the ship is not sunk it will print out hit. If
        the ship is sunk, it will print out that the ship has been sunk.
        
    Parameters: board is the Board object that Player Two is attacking.
    x_coord is the x coordinate that Player Two is attacking.
    y_coord is the y coordinate that Player Two is attacking.
    ships_sunk is the total number of ships that Player Two has sunk.
    
    Returns: The number of ships that Player Two has sunk so far."""
    if board[x_coord][y_coord].guessed() == False:
        board[x_coord][y_coord].got_guessed()
        board[x_coord][y_coord].ship().hit(x_coord, y_coord)
        if board[x_coord][y_coord].ship().safe() == []:
            print("{} sunk".format(board[x_coord][y_coord].ship().ship()))
            ships_sunk += 1
        elif board[x_coord][y_coord].ship().safe() != []:
            print("hit")
    elif board[x_coord][y_coord].guessed() == True:
        print("hit (again)")
    return ships_sunk

def game_over():
    """Prints a game over message when all 5 of Player One's ships have been sunk
        by Player Two and quits the program.
    
    Parameters: None.
    
    Returns: None."""
    print("all ships sunk: game over")
    sys.exit()

def check_for_overlapping_x(board, new_ship, line):
    """Checks to see if a coordinate point on the board is already occupied
        or not.
    
    Parameters: board is the board that the Ship objects are placed on.
        new_ship is a new Ship object that has just been made.
        line is the line on which the Ship object was created.
    
    Returns: The line that an overlapping error occurs. If there is none,
        then the function returns False."""
    for position in new_ship.positions():
            if board[9 - position[1]][position[0]].ship() != None:
                return line
            board[9 - position[1]][position[0]].set_ship(new_ship)
    return False

def check_for_overlapping_y(board, new_ship, line):
    """Checks to see if a coordinate point on the board is already occupied
        or not.
    
    Parameters: board is the board that the Ship objects are placed on.
        new_ship is a new Ship object that has just been made.
        line is the line on which the Ship object was created.
    
    Returns: The line that an overlapping error occurs. If there is none,
        then the function returns False."""
    for position in new_ship.positions():
            if board[9 - position[1]][position[0]].ship() != None:
                return line
            board[9 - position[1]][position[0]].set_ship(new_ship)
    return False

def main():
    out_of_bounds = False
    bad_placement = False
    overlapping = False
    incorrect_ship_size = False

    placement = open(input(), "r")
    guesses = open(input(), "r")
    x = Board()
    ship_dict = {
        "A": 5,
        "B": 4,
        "S": 3,
        "D": 3,
        "P": 2
        }
    list_of_ships = []
    
    for line in placement:
        new_ship = None
        split_line = line.split()
        if split_line[1] != split_line[3] and split_line[2] != split_line[4]:
            bad_placement = line

        elif int(split_line[1]) not in range(10) or int(split_line[2]) not in range(10) or \
            int(split_line[3]) not in range(10) or int(split_line[4]) not in range(10):
            out_of_bounds = line
        
        elif split_line[1] != split_line[3]:
            new_ship = create_ship_y(split_line[0], int(split_line[1]), int(split_line[3]), int(split_line[2]))
            overlapping = check_for_overlapping_y(x.board(), new_ship, line)
        
        elif split_line[2] != split_line[4]:
            new_ship = create_ship_x(split_line[0], int(split_line[2]), int(split_line[4]), int(split_line[1]))
            overlapping = check_for_overlapping_x(x.board(), new_ship, line)

        list_of_ships.append(new_ship)
        
        if new_ship != None and new_ship.size() != ship_dict[new_ship.ship().upper()]:
            incorrect_ship_size = line
        
    if len(list_of_ships) != 5:
        fleet_error()
    if out_of_bounds != False:
        out_of_bounds_error(out_of_bounds)
    if bad_placement != False:
        placement_error(line)
    if overlapping != False:
        overlapping_error(line)
    if incorrect_ship_size != False:
        ship_size_error(line)

    print(x.show_board())

    ships_sunk = 0
    for line in guesses:
        line = line.split()
        x_coord = int(line[0])
        y_coord = int(line[1])
        if x_coord not in range(10) or y_coord not in range(10):
            illegal_guess()

        elif x.board()[9 - y_coord][x_coord].ship() == None:
            miss(x.board(), x_coord, y_coord)

        elif x.board()[9 - y_coord][x_coord].ship() != None:
            ships_sunk = hit(x.board(), 9 - y_coord, x_coord, ships_sunk)
        
        if ships_sunk == 5:
            game_over()
    
main()