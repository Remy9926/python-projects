"""
    Takes a file with dates and creates a Date object for each unique
        date in its canonical form with the canonical date as an attribute as
        well as a list of events that took place on that date as another
        attribute. The object is then placed into a DateSet object that
        contains a dictionary with the canonical date as keys and Date
        objects as values.
"""

class Date:
    def __init__(self, date, event):
        """Instantiates a Date object with the parameters date and event.
            uses the canonical version of date as the object's date attribute
            and has a list of events that occurred on that date.
        
        Parameters: date is the canonical representation of the date as a
            string.
            event is a string that represents the name of an event.
        
        Returns: None."""
        self.date = canonicalize_date(date)
        self.event = []
        self.add_event(event)

    def add_event(self, event):
        """Appends an event to a Date objects list.
        
        Parameters: event is the string that gets appended to the list.
        
        Returns: None."""
        self.event.append(event)

    def __str__(self):
        """Returns the Date object's canonical date as well as the list of
            events that occurred on that date.
        
        Parameters: None.
        
        Returns: The canonical date with a colon followed by the list of
            events that occurred on that date."""
        return ("{}: {}".format(self.date, self.event))
    
    def __eq__(self, other):
        """When comparing two Date objects using the == operator, returns
            whether or not the canonical date of both events are the same
        
        Parameters: other is the other Date object that is getting compared to
        
        Returns: A boolean value of whether or not the two objets share the
            same canonical date."""
        return self.date == other.date

    def get_date(self):
        # getter method for the date attribute for a Date object.
        return self.date
    
    def get_event(self):
        # getter method for the event attribute for a Date object.
        return self.event

class DateSet:
    def __init__(self):
        """Instantiates a DateSet object and creates a dict attribute for it,
        which is a dictionary.
        
        Parameters: None.
        
        Returns: None."""
        self.dict = {}
    
    def add_date(self, date, event):
        """Instantiates a Date object and adds it to the DateSet's dictionary.
            the key is the canonical date and the value is a Date object
            who's date attribute is the canonical date.
            
        Parameters: date is a date in canonical form.
            event is a string that represents an event.
            
        Returns: None."""
        if date not in self.dict:
            self.dict[date] = Date(date, event)
        else:
            self.dict[date].add_event(event)

    def __str__(self):
        """ Returns the DateSet's dict attribute as a string
        
        Parameters: None.
        
        Returns: String representation of a DateSet object's dictionary."""
        return str(self.dict)


def canonicalize_date(date):
    """Takes a date representation and turns it into its canonical version.
    
    Parameters: date is a string that represents a date.
    
    Returns: A string that represents the inputted date in canonical form."""
    dict = {"Jan" : 1,
    "Feb" : 2,
    "Mar" : 3,
    "Apr" : 4,
    "May" : 5,
    "Jun" : 6,
    "Jul" : 7,
    "Aug" : 8,
    "Sep" : 9,
    "Oct" : 10,
    "Nov" : 11,
    "Dec" : 12}
    
    if "-" in date:
        mm = date.split("-")[1]
        dd = date.split("-")[2]
        yyyy = date.split("-")[0]

    elif "/" in date:
        mm = date.split("/")[0]
        dd = date.split("/")[1]
        yyyy = date.split("/")[2]
    
    elif " " in date:
        mm = dict[date.split(" ")[0]]
        dd = date.split(" ")[1]
        yyyy = date.split(" ")[2]
        
    return "{:d}-{:d}-{:d}".format( int(yyyy), int(mm), int(dd))

def main():
    
    dateset_object = DateSet()
    read_file = open(input(), "r")
    for line in read_file:
        if line[0] == "I":
            rest_of_line = line[1:].strip(" \n")
            rest_of_line = rest_of_line.split(":", 1)
            date = canonicalize_date(rest_of_line[0].strip(" "))
            event = rest_of_line[1].strip(" \t")
            dateset_object.add_date(date, event)
        
        elif line[0] == "R":
            date_canonical = canonicalize_date(line[1:].strip(" \n"))
            if date_canonical in dateset_object.dict:
                for event in sorted(dateset_object.dict[date_canonical].event):
                    print("{}: {}".format(date_canonical, event))

        else:
            print("Error - Illegal operation.")

main()
