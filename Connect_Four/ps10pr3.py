#
# ps10pr3.py  (Problem Set 10, Problem 3)
#
# Playing the game    
#

from ps10pr1 import Board
from ps10pr2 import Player
import random
    
def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(player1, board) == True:
            return board

        if process_move(player2, board) == True:
            return board

# part 1: process_move
def process_move(player, board):
    """ responsible for processing a single move by specified player on specified
        board.
    """
    print(player, "'s turn")
    next_move_col = player.next_move(board)
    board.add_checker(player.checker, next_move_col)
    print()
    print(board)
    if board.is_win_for(player.checker) == True:
        print(player, 'wins in', player.num_moves, 'moves.', '\nCongratulations!')
        return True
    elif board.is_full():
        print("It's a tie!")
        return True
    else:
        return False
    
    
# RandomPlayer class
class RandomPlayer(Player):
    """ an unintelligent computer player.  Chooses moves at random.
        Subclass of Player
    """
    # use inherited __init__ and __repr__
    
    # next_move method for RandomPlayer
    def next_move(self, board):
        """ choose at random from columns that are not yet full and returns
            index of that random column.  +1 to num_moves as well
        """
        poss = []
        # check to see if each column is full using board.can_add_to
        for col in range(board.width):
            # if it is not full, add to list of possibilities
            if board.can_add_to(col) == True:
                poss += [col]
        self.num_moves += 1
        return (random.choice(poss))
            
        
        
