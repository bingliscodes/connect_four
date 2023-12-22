## Connect 4 Board class ##

class Board:
    """ the class that represents the board in a connect 4 game between a human
        and a computer
    """
    # the constructor for the board class
    def __init__(self, height, width):
        """ initializes dimensions of the board
            parameters: height- stores number of rows
            width- stores number of columns
            slots- stores a 2D list with height rows and width columns used to store
            current contents of the board a slot will have an empty char: ' ', an
            'X', or an 'O'
        """
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]

    # the string representation for a Board object
    def __repr__(self):
        """ returns a string representation of the Board object using '|' and the
            previously specified characters
        """
        s = ''         # begin with an empty string

        # add one row of slots at a time
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        s += '-' * 2* self.width + '-'
        s += '\n'   #newline at below the hyphens
        s += ' '    #formatting numbers
        for col in range(self.width):
            s += str(col) + ' '

        return s

    # add_checker method
    def add_checker(self, checker, col):
        """ adds the designated checker to the designated column as far down as
            allowed by the board
        """
        # make sure that it is a valid input to not corrupt the board
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)
        row = 0
        # loop until it hits the bottom
        while self.slots[row][col] == ' ' and row < self.height - 1:
            #print('row is', row, 'col is', col)
            row += 1
        # if there is a checker already, back up one
        if self.slots[row][col] != ' ':
            row -= 1
        self.slots[row][col] = checker

    # reset method
    def reset(self):
        self.slots = [[' '] * self.width for row in range(self.height)]

    # add_checkers method
    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
        checkers in those columns of the called Board object, 
        starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    # can_add_to method
    def can_add_to(self, col):
        """ returns True if checker placement is valid, otherwise returns False
        """
        if col < 0 or col > self.width - 1:
            return False
        elif self.slots[0][col] != ' ':
            return False
        
        return True

    # is_full method
    def is_full(self):
        """ returns True if Board is completely full, false if otherwise
        """
        for col in range(self.width):
            if self.can_add_to(col) == True:
                return False
        return True

    # remove_checker method
    def remove_checker(self, col):
        """ removes the top checker from column col of Board.  Does nothing if
            column is empty
        """
        row = 0
        while self.slots[row][col] == ' ' and row < self.height - 1:
            row += 1

        self.slots[row][col] = ' '

 

    # is_win_for method
    def is_win_for(self, checker):
        """ returns True if there are four consecutive slots with checker.  Returns
            False if otherwise
        """
        assert(checker == 'X' or checker == 'O')
        if self.is_vertical_win(checker) == True or \
           self.is_horizontal_win(checker) == True or \
           self.is_diagonal_win_left(checker) == True or \
           self.is_diagonal_win_right(checker) == True:
            return True
        else:
            return False

    
   # helper functions for is_win_for
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False

    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker.
        """
        for col in range(self.width):
            for row in range(self.height - 3):
                # check if the next for rows in this column have the specified
                # checker
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True
        return False

    def is_diagonal_win_left(self, checker):
        """ Checks for a diagonal win going left to right
        """
        if self.height < 4:
            return False
        for row in range(self.height - 2, self.height):
            for col in range(self.width - 3):
                #print('row is', row, 'col is', col)
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                    
                    return True
                
        return False

    def is_diagonal_win_right(self, checker):
        """ Checks for a diagonal win going right to left
        """
        if self.height < 4:
            return False
        for row in range(self.height - 2, self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                    self.slots[row - 1][col - 1] == checker and \
                    self.slots[row - 2][col - 2] == checker and \
                    self.slots[row - 3][col - 3] == checker:
                    return True
        return False

    
                
