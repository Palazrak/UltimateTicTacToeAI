# Made by GitHub users @Palazrak and @fridamarquezg

import GameBoard
import math

# Mapping from (row, column) positions in the ultimate tic-tac-toe board to their respective index in the game state array.
MAPPING = {
    # First subgame (top-left 3x3 grid)
    (1, 1): 0, (1, 2): 1, (1, 3): 2,
    (2, 1): 3, (2, 2): 4, (2, 3): 5,
    (3, 1): 6, (3, 2): 7, (3, 3): 8,

    # Second subgame (top-middle 3x3 grid)
    (1, 4): 9, (1, 5): 10, (1, 6): 11,
    (2, 4): 12, (2, 5): 13, (2, 6): 14,
    (3, 4): 15, (3, 5): 16, (3, 6): 17,

    # Third subgame (top-right 3x3 grid)
    (1,7):18, (1,8):19, (1,9):20,
    (2,7):21, (2,8):22, (2,9):23,
    (3,7):24, (3,8):25, (3,9):26,

    # Fourth subgame (middle-left 3x3 grid)
    (4,1):27, (4,2):28, (4,3):29,
    (5,1):30, (5,2):31, (5,3):32,
    (6,1):33, (6,2):34, (6,3):35,

    # Fifth subgame (center 3x3 grid)
    (4,4):36, (4,5):37, (4,6):38,
    (5,4):39, (5,5):40, (5,6):41,
    (6,4):42, (6,5):43, (6,6):44,

    # Sixth subgame (middle-rigth 3x3 grid)
    (4,7):45, (4,8):46, (4,9):47,
    (5,7):48, (5,8):49, (5,9):50,
    (6,7):51, (6,8):52, (6,9):53,

    # Seventh subgame (bottom-left 3x3 grid)
    (7,1):54, (7,2):55, (7,3):56,
    (8,1):57, (8,2):58, (8,3):59,
    (9,1):60, (9,2):61, (9,3):62,

    # Eighth subgame (bottom-middle 3x3 grid)
    (7,4):63, (7,5):64, (7,6):65,
    (8,4):66, (8,5):67, (8,6):68,
    (9,4):69, (9,5):70, (9,6):71,

    # Ninth subgame (bottom-right 3x3 grid)
    (7, 7): 72, (7, 8): 73, (7, 9): 74,
    (8, 7): 75, (8, 8): 76, (8, 9): 77,
    (9, 7): 78, (9, 8): 79, (9, 9): 80,
}
# Reverse mapping for converting back from indices to (row, column) positions.
REVERSE_MAPPING = {v: k for k, v in MAPPING.items()}  # Create a reverse mapping from index to (row, column).

def subgame_heuristic(new_game, symbol):
    ''' Evaluates the current subgame board based on the given symbol (X or O). 
        It calculates potential winning lines for the current player and the opponent.'''
    if new_game.state[91] != 9:  # Check if the game is constrained to a specific subgame.
        winning_lines_list = new_game.get_indexes_from_constraint()  # Get the winning lines for the constrained subgame.
        winning_lines = 0  # Initialize the count of potential winning lines for the current player.
        winning_lines_opponent = 0  # Initialize the count of potential winning lines for the opponent.

        # Calculate scores based on the current player's symbol.
        if symbol == 'X':
            for line in winning_lines_list:
                sum = 0
                for num in line:
                    sum += num  # Sum the values in the current line.
                if (sum == 2) & (2 not in line):  # Check for two 'X's and no 'O's.
                    winning_lines += 10  # Gives a positive value for each potential winning line for 'X'.
                elif (sum == 4) & (1 not in line):  # Check for two 'O's and no 'X's.
                    winning_lines_opponent -= 10  # Gives a negative value for each potential winning line for 'O'.
        else:  # If the current player is 'O'.
            for line in winning_lines_list:
                sum = 0
                for num in line:
                    sum += num  # Sum the values in the current line.
                if (sum == 4) & (1 not in line):  # Check for two 'O's and no 'X's.
                    winning_lines += 10  # Gives a positive value for each potential winning line for 'O'.
                elif (sum == 2) & (2 not in line):  # Check for two 'X's and no 'O's.
                    winning_lines_opponent -= 10  # Gives a negative value for each potential winning line for 'X'.

        result = winning_lines + winning_lines_opponent  # Calculate the subgame heuristic value.

    else:
        result = -80  # If the game is not constrained, return a default heuristic value.

    return result

def macrogame_winning_lines(new_game, symbol):
    ''' Evaluates the entire board (macrogame) based on the given symbol (X or O).
        It calculates potential winning lines for the current player and the opponent.'''
    
    # Define all possible winning lines in the macrogame (supergame).
    winning_lines_list = [[new_game.state[81], new_game.state[82], new_game.state[83]],
                            [new_game.state[84], new_game.state[85], new_game.state[86]],
                            [new_game.state[87], new_game.state[88], new_game.state[89]],
                            [new_game.state[81], new_game.state[84], new_game.state[87]],
                            [new_game.state[82], new_game.state[85], new_game.state[88]],
                            [new_game.state[83], new_game.state[86], new_game.state[89]],
                            [new_game.state[81], new_game.state[85], new_game.state[89]],
                            [new_game.state[83], new_game.state[85], new_game.state[87]]]
    
    winning_lines = 0  # Initialize the count of potential winning lines for the current player.
    winning_lines_opponent = 0  # Initialize the count of potential winning lines for the opponent.

    # Calculate scores based on the current player's symbol.
    if symbol == 'X':
        for line in winning_lines_list:
            sum = 0
            for num in line:
                sum += num  # Sum the values in the current line.
            if (sum == 2) & (2 not in line):  # Check for two 'X's and no 'O's.
                winning_lines += 25  # Gives a positive value for each potential winning line for 'X'.
            elif (sum == 4) & (1 not in line):  # Check for two 'O's and no 'X's.
                winning_lines_opponent -= 25  # Gives a negative value for each potential winning line for 'O'.
    else:  # If the current player is 'O'.
        for line in winning_lines_list:
            sum = 0
            for num in line:
                sum += num  # Sum the values in the current line.
            if (sum == 4) & (1 not in line):  # Check for two 'O's and no 'X's.
                winning_lines += 25  # Gives a positive value for each potential winning line for 'O'.
            elif (sum == 2) & (2 not in line):  # Check for two 'X's and no 'O's.
                winning_lines_opponent -= 25  # Gives a negative value for each potential winning line for 'X'.

    result = winning_lines + winning_lines_opponent  # Calculate the macrogame heuristic value.

    return result


def macrogame_heuristic(new_game, symbol):
    # Defines piece values based on the player.
    if symbol == 'X':
        my_value = 1
        opponent_value = 2
    else:
        my_value = 2
        opponent_value = 1

    # If the overall game result is still undecided, calculate score based on board positions.
    if new_game.state[92] == 0:  # Game is ongoing.
        macrogame_state = new_game.state[81:90]  # Get the state of the macrogame (results of subgames).

        # Define positions for corners, middles, and the center.
        corners = [0, 2, 6, 8]
        middles = [1, 3, 5, 7]
        center = 4

        # Initialize total score.
        score = 0

        # Check corners.
        for i in corners:
            if macrogame_state[i] == my_value:
                score += 30  # Favorable position for the player.
            elif macrogame_state[i] == opponent_value:
                score -= 30  # Unfavorable position for the player.

        # Check the center.
        if macrogame_state[center] == my_value:
            score += 50  # The center is highly valued.
        elif macrogame_state[center] == opponent_value:
            score -= 50

        # Check middles.
        for i in middles:
            if macrogame_state[i] == my_value:
                score += 10  # Middles have lower value compared to corners and the center.
            elif macrogame_state[i] == opponent_value:
                score -= 10

    # If the game is already won by the player, assign an infinitely high score.
    elif new_game.state[92] == my_value:
        score = math.inf
    
    # If the game is lost, assign an infinitely low score.
    else:
        score = -math.inf

    return score

def game_heuristic(new_game, symbol):
    ''' Combines various heuristic evaluations for the current game state.
        Returns the sum of the values obtained by each heuristic function. 
        The macrogame_heuristic value is halved to prioritize the value obtained in the other functions'''
    return subgame_heuristic(new_game, symbol) + macrogame_heuristic(new_game, symbol)/2 + macrogame_winning_lines(new_game, symbol)

def reverse_mapping(index):
    ''' Converts a game state index back to its matrix index form.
        This function is useful for translating internal game indices (used in the minimax algorithm).'''
    
    if index in REVERSE_MAPPING:
        # If the index exists in the reverse mapping dictionary, retrieve the (row, col) tuple.
        row, col = REVERSE_MAPPING[index]
        # Convert the (row, col) coordinates back to a single matrix index.
        # This is typically in the form 'rowcol' (e.g., row 3, column 4 becomes 34).
        return row * 10 + col
    else:
        # If the index does not exist in the reverse mapping (meaning it's not valid),
        # return None to indicate that no valid matrix position corresponds to this index.
        return None


def _minimax(game, total_depth, current_depth, turn, symbol):
    ''' Minimax algorithm implementation for the game. It evaluates possible moves and chooses the best one.
        'game' is the current game state, 'profundidad_total' is the total depth, 'profundidad_actual' is the current depth,
        'turn' indicates whose turn it is (True for AI, False for opponent), and 'ficha' is the piece type ('X' or 'O').'''

    global optimal_move  # Use a global variable to store the best move.

    # Base case: if the current depth is zero or the game is over, return the heuristic value of the board.
    if current_depth == 0 or game.is_game_over():
        return game_heuristic(game, symbol)
        
    # Get all possible legal moves for the current game state.
    frontier = game._get_legal_indexes().copy()

    if turn:  # AI's turn.
        best_value = -math.inf  # Initialize the best value as negative infinity.
        for possible_move in frontier:
            # Create a new game state by copying the current one and making a move.
            new_game = GameBoard.GameBoard(state=game.state.copy())
            new_game.play(reverse_mapping(possible_move))  # Make the move in the copied game state.
            # Recursively call the minimax function for the opponent's turn.
            heuristic_value = _minimax(new_game, total_depth, current_depth - 1, False, symbol)
            # Update the best value and optimal move if the current heuristic value is better.
            if best_value <= heuristic_value:
                if current_depth == total_depth:  # Update the optimal move only at the top level of recursion.
                    optimal_move = possible_move
                best_value = heuristic_value
        return best_value
    else:  # Opponent's turn.
        best_value = math.inf  # Initialize the best value as infinity.
        for possible_move in frontier:
            # Similar process as above, but for the opponent's move.
            new_game = GameBoard.GameBoard(state=game.state.copy())
            new_game.play(reverse_mapping(possible_move))
            # Recursively call the minimax function for the AI's turn.
            heuristic_value = _minimax(new_game, total_depth, current_depth - 1, True, symbol)
            # Update the best value if the current heuristic value is better.
            if best_value > heuristic_value:
                best_value = heuristic_value
        return best_value

def minimax(game, profundidad, turn, symbol):
    ''' Public function to start the minimax algorithm.
        'game' is the Ultimate Tic Tac Toe game instance, 'profundidad' is the depth for the algorithm,
        'turn' indicates whose turn it is, and 'ficha' represents the piece type.'''
    global optimal_move
    optimal_move = None  # Reset the optimal move before starting.
    _minimax(game, profundidad, profundidad, turn, symbol)  # Start the recursive minimax process.
    return optimal_move  # Return the optimal move after the minimax process is complete.