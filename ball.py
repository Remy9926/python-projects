"""
    Takes a file of basketball team school names, their conferences,
        and their wins and losses and returns the conferences with the highest
        average win ratios.
"""

class Team():
    def __init__(self, line):
        """Initializes a Team object that contains the attributes _line,
            which is the line that will be processed. _name is the name of
            the team, _wins is the number of wins the team has, _losses
            is the number of losses the team has, _conf is the conference that
            the team is in, and _win_ratio is the win ratio of the team.
        
        Parameters: line is a string representing a team, its conference, and
            wins and losses.
        
        Returns: None."""

        self._line = line
        self._name = None
        self._wins = None
        self._losses = None
        self.process_line(self._line)

    def name(self):
        return self._name

    def conf(self):
        return self._conf

    def win_ratio(self):
        return self._win_ratio

    def __str__(self):
        """When a Team object is printed out it returns the team's name
            and its win ratio.
            
        Parameters: None.
        
        Returns: The name and win ratio of a Team object."""

        return "{} : {}".format(self._name, str(self._win_ratio))
    
    def process_line(self, line):
        """Takes the line attribute of a Team object and processes the line
            by assigning parts of it to different attributes of that a Team
            object would contain.
        
        Parameters: line is the line that is going to be processed, which
            is usually the line attribute of a Team object.
            
        Returns: None."""

        i = 0
        if line[0] in "123456789":
            i = 1
        for i in range(1, len(line) + 1):
            if line[-i] == "(":
                index = len(line) - i + 1
                break
        remaining = line[index - 1:].strip(" ")
        self._name = line[:index - 1].strip(" ")
        for i in range(len(remaining)):
            if remaining[i] == ")":
                index = i
                break
        self._conf = remaining[: i + 1]
        remaining = remaining[i + 1:].strip(" \t\n")
        empty_string = ""
        for i in range(len(remaining)):
            if remaining[i] in "1234567890":
                empty_string += remaining[i]
            else:
                self._wins = int(empty_string)
                index = i
                break
        self._losses = remaining[i:].strip("\t ")
        self._win_ratio = \
            int(self._wins) / (int(self._wins) + int(self._losses))

class Conference():
    def __init__(self, conf):
        """Initializes a Conference object and gives a _name attribute,
            which is the name of the conference and a _list attribute, which
            is the list of schools in that conference.
        
        Parameters: conf is the name of the conference.
        
        Returns: None."""

        self._name = conf
        self._list = []

    def __contains__(self, team):
        """Checks to see whether or not a specific Team is in a given
            conference.
        
        Parameters: team is a Team object, which will be checked to see
            if that team is in the conference.

        Returns: A boolean value of whether or not the team's name is in the
            conference."""

        return team._name in self._list

    def name(self):
        """A getter method for the name of a conference object.
        
        Parameteres: None.
        
        Returns: None."""

        return self._name

    def add(self, team):
        """Adds a Team object to the list of the conference that the team
            belongs to.
            
        Parameters: team is a Team object.
        
        Returns: None."""

        self._list.append(team)

    def win_ratio_avg(self):
        """Calculates the average win ratio of all the schools within a given
            conference.
        
        Parameters: None.
        
        Returns: The win ratio of all schools within the conference."""

        total = 0
        for team in self._list:
            total += team._win_ratio
        self._win_ratio_avg = total / len(self._list)
        return self._win_ratio_avg

    def __str__(self):
        """Prints out a Conference object's name and its average win ratio.
        
        Parameters: None.
        
        Returns: The name of a conference and its average win ratio."""

        self._win_ratio_avg = self.win_ratio_avg()
        return "{} : {}".format(self._name, str(self._win_ratio_avg))

class ConferenceSet():
    def __init__(self):
        """Initializes a ConferenceSet object with a dictionary to store all
            the conference names as keys and their corresponding objects as
            values.
        
        Parameters: None.
        
        Returns: None."""

        self._dict = {}

    def add(self, team):
        """Takes a Team object and checks whether or not the conference is
            in the ConferenceSet object's dictionary or not. If not it adds
            the conference name as a key with a Conferenfce object as the
            value and adds the team to the Conference object's list
            
        Parameters: team is a Team object.
        
        Returns: None."""

        if team._conf not in self._dict:
            self._dict[team._conf] = Conference(team._conf)
        self._dict[team._conf]._list.append(team)

    def best(self):
        """Calculates the win ratio of all the conferences and searches for
            the teams in each conference with the highest win ratio and prints
            them out.
            
        Parameters: None.
        
        Returns: None."""

        for conf in self._dict:
            self._dict[conf].win_ratio_avg()
        highest_win_ratio = 0
        for conf in self._dict:
            if self._dict[conf]._win_ratio_avg > highest_win_ratio:
                highest_win_ratio = self._dict[conf]._win_ratio_avg
        for conf in sorted(self._dict):
            if self._dict[conf]._win_ratio_avg == highest_win_ratio:
                print("{} : {}".format(conf.strip("()"), highest_win_ratio))


def main():
    conference_set = ConferenceSet()
    for line in open(input(), "r"):
        if line[0] != "#":
            x = Team(line)
            conference_set.add(x)
    conference_set.best()

main()
