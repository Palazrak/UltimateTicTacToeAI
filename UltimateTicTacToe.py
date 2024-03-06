# Made by GitHub user @Majo2103

import GameBoard
import Move
import UtttError
import GameMethods

# Constants representing the state values for the game.
X_STATE_VALUE = 1  # State value representing the 'X' player.
O_STATE_VALUE = 2  # State value representing the 'O' player.

class UltimateTicTacToe:
    @staticmethod
    def main():
        # Initialize the Ultimate Tic Tac Toe game.
        game = GameBoard.GameBoard()

        # Ask the user who should start the game.
        s = input("If you want the AI to make the first move, type 'AI'. If you want to make the first move, type 'ME': ")
        if s == 'AI': # IA starts.
            symbol = "X"  # IA plays as X.
            # Make the AI perform the first move, chosen here as the middle of the board.
            game.play(55)
        else: # Human starts.
            symbol = "O"  # Human plays as O.

        # Print the initial state of the game.
        print(game)

        game_over = False
        while not game_over:  # Continue playing until the game is over.
            # Human player's turn.
            flag = True
            while flag:
                print("It's your turn.")  
                play = input("Enter the square you want to play.: ")  
                flag = False
                try:
                    game.play(int(play))  # Attempt to make the entered move.
                    print(game)  # Print the game state after the move.
                    game_over = game.is_game_over()  # Check if the game is over.
                except UtttError.utttError as e:
                    print('Invalid move.')  # Invalid move.
                    flag = True  # Allow the player to make another move.
                if game_over:
                    break  # Exit the loop if the game is over.

            # AI's turn.
            if not game_over:
                print("AI's turn.")  # It's the AI's turn.
                ai_play = GameMethods.reverse_mapping(GameMethods.minimax(game, 5, True, symbol))  # AI calculates its move.
                if ai_play is not None:
                    game.play(ai_play)  # Make the AI's move.
                    print("AI's move:", ai_play)  # Print the AI's move.
                    print(game)  # Print the game state after the AI's move.
                    game_over = game.is_game_over()  # Check if the game is over.
                else:
                    print("The AI could not find a valid move.")

        # Determine the winner.
        if game.get_winner() == X_STATE_VALUE:
            ganador = "X"
        elif game.get_winner() == O_STATE_VALUE:
            ganador = "O"
        else:
            ganador = "None (Tie)"  # Nobody (tie).
        print("The game is over. Winner: ", ganador)  # The game is over.
        
# Run game
UltimateTicTacToe.main()