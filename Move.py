# Made by GitHub user @mellamanelpoeta

# Constants representing the state values for the game.
X_STATE_VALUE = 1  # State value representing the 'X' player.
O_STATE_VALUE = 2  # State value representing the 'O' player.

class Move:
    def __init__(self, symbol: int, index: int):
        """
        Initializes a new instance of the Move class.

        Parameters:
        symbol (int): Represents the player making the move, using constants X_STATE_VALUE (1) or O_STATE_VALUE (2).
        index (int): The position (ranging from 0 to 80) on the ultimate tic-tac-toe board where the symbol will be placed.
        """
        self.symbol = symbol  # Store the player's symbol (X or O) as an integer (X_STATE_VALUE = 1 or O_STATE_VALUE = 2).
        self.index = index    # Store the board position for the move (int from 0 to 80).

    def __str__(self):
        """
        Returns a string representation of the Move instance, which is useful for debugging.

        The output will be in the format 'Move(symbol=X, index=index)' or 'Move(symbol=O, index=index)',
        where 'X' or 'O' corresponds to the player's symbol and 'index' is the position on the board.
        """
        output = '{cls}(symbol={symbol}, index={index})'  # Template for the output string.
        output = output.format(
            cls='Move',  # Class name
            symbol={X_STATE_VALUE: 'X', O_STATE_VALUE: 'O'}[self.symbol],  # Convert the symbol from int to string ('X' or 'O').
            index=self.index,  # Include the move index (board position).
        )
        return output  # Return the formatted string representation of the move.