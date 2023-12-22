
# AI Player for use in Connect Four   

import random  
from play_game import *

class AIPlayer(Player):
    """ A player class that looks ahead a certain number of moves to intelligently
        makes its next move.  Subclass of Player
    """
    def __init__(self, checker, tiebreak, lookahead):
        """ a constructor for the AIPlayer class. Checker must be 'X' or 'O'.
            tiebreak determines how the AI will choose from tied-value columns.
            lookahead determines values for moves based on outcome.
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    # repr method for AIPlayer
    def __repr__(self):
        """ returns a string representation of the AIPlayer.  Shows checker, tiebreak type,
            and lookahead value.
        """
        s = 'Player ' + self.checker + ' '
        s += '(' + self.tiebreak + ', ' + str(self.lookahead) + ')'
        return s

    # max_score_column method
    def max_score_column(self, scores):
        """ takes a list of scores from each column and returns the index of the
            column with the maximum score.  If there is a tie, apply AIPlayer's
            tiebreak method to break the tie.
        """
        max_score = max(scores)
        score_indices = []
        # go through each score and create a new list with indices when score is
        # max_score
        for i in range(len(scores)):
            if scores[i] == max_score:
                score_indices += [i]

        # determine move based on tiebreak method
        if self.tiebreak == 'LEFT':
            return min(score_indices)
        elif self.tiebreak == 'RIGHT':
            return max(score_indices)
        else:
            return (random.choice(score_indices))

    # scores_for method
    def scores_for(self, board):
        """ takes a board object and determines the AIPlayer's scores for columns
            on the board with scores outlined as follows:
            -1 for full column
            0 for a column that will result in a loss at some point
            100 for a column that results as a win
            50 for a column that results in neither win or loss
        """
        scores = [50] * board.width

        for col in range(board.width):
            
            #base cases:
            #print('column', col, 'with lookahead', self.lookahead)
            if board.can_add_to(col) == False:
                scores[col] = -1
            # use is_win_for method to check if there is a winner
            elif board.is_win_for(self.checker):
                #print('Player wins in', self.lookahead, 'if he goes in col', col)
                scores[col] = 100
            elif board.is_win_for(self.opponent_checker()):
                #print('Opponent wins in', self.lookahead, 'if he goes in col', col)
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            # recursive case: try col, add checker to it, create opponent with
            # self.lookahead - 1, create opp_scores list, find scores[col], then
            # remove the checker
           
            else:
                board.add_checker(self.checker, col)
                #print(board)
                # create an opponent with opposite checker,
                # same tiebreak, and lookahead - 1
                #print('creating AIPlayer with lookahead', self.lookahead - 1)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, \
                (self.lookahead - 1))
                # recursively call opponent scores
                opp_scores = opponent.scores_for(board)
                scores[col] = 100 - max(opp_scores)
                #print(self.checker,'opp_scores for lookahead',col, self.lookahead, 'is', \
                      #opp_scores[col], 'my score', scores[col])
                #print(board)
                board.remove_checker(col)

        return scores
                
        #next_move method
    def next_move(self, board):
        """ overrides inherited next_move.  Return AI player's judgment of its
                best possible move.
        """
        self.num_moves += 1
        return self.max_score_column(self.scores_for(board))
        

    
