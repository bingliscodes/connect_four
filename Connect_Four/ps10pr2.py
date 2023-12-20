#
# ps10pr2.py  (Problem Set 10, Problem 2)
#
# A Connect-Four Player class   
#

from ps10pr1 import Board

# write your class below

class Player:
    """ represents a player of the connect for game.
    """

    # constructor for Player class
    def __init__(self, checker):
        """ the constructor for a new Player object with attributes checker which
            represents the gamepiece, and num_moves, which stores how many moves
            the player as made, initialized at 0.
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0

    # repr method for Player
    def __repr__(self):
        """ string representation of a player object which indicates the checker
            a player is using.
        """
        return 'Player ' + self.checker

    # opponent_checker method
    def opponent_checker(self):
        """ returns a 1 char string that represents the checker of the Player's
            opponent.
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'

    # next_move method
    def next_move(self, board):
        """ returns the column where Player wants to make the next move.
            Asks user to enter a column where the user wants to play.  If invalid
            column is given, it asks again.
        """
        while True:
            column = int(input('Enter a column: '))
            if column < 0 or column > board.width - 1 or \
               board.can_add_to(column) == False:
                print('Try again!')
            else:
                self.num_moves += 1
                return column
        
            
