class GameComponents:
    def __init__(self, two_player):
        # Store tic tac toe board and spaces taken
        self.spaces = ["   |", "   |", "   \n-----------\n", "   |", "   |", "   \n-----------\n",
                       "   |", "   |", "   "]
        self.spaces_taken = ["", "", "", "", "", "", "", "", ""]

        # Store number of turns, who's turn, and if someone won the game
        self.turns = 0
        self.whos_turn = ""
        self.has_winner = False
        self.rules(two_player)

    def rules(self, two_player):
        # Rules for 2 player
        if two_player is True:
            print("\nWelcome to the human vs. human version of Tic Tac Toe.")
            print("Here two players will play, where Player 1 is O and Player 2 is X.")

        # Rules for human vs AI
        elif two_player is False:
            print("\nWelcome to the human vs. AI version of Tic Tac Toe.")
            print("Here the human will play as O and AI will play as X.")

        # General rules apply to all
        print("The top row's left, middle, and right spaces can be selected with 0, 1, and 2.")
        print("The middle row's left, middle, and right spaces can be selected with 3, 4, and 5.")
        print("The bottom row's left, middle, and right spaces can be selected with 6, 7, and 8.")
        print("Good luck and may the best win!\n")

    def put_space(self, num_space, char_to_put):
        if num_space == 2 or num_space == 5:
            self.spaces[num_space] = f" {char_to_put} \n-----------\n"
        elif num_space == 8:
            self.spaces[num_space] = f" {char_to_put} "
        else:
            self.spaces[num_space] = f" {char_to_put} |"

    def evaluate_winner(self, player):
        # First row
        if self.spaces_taken[0] == player and self.spaces_taken[1] == player and self.spaces_taken[2] == player:
            print(f"\n{player} is the winner!")
            self.has_winner = True

        # Middle row
        elif self.spaces_taken[3] == player and self.spaces_taken[4] == player and self.spaces_taken[5] == player:
            print(f"\n{player} is the winner!")
            self.has_winner = True

        # Bottom row
        elif self.spaces_taken[6] == player and self.spaces_taken[7] == player and self.spaces_taken[8] == player:
            print(f"\n{player} is the winner!")
            self.has_winner = True

        # First column
        elif self.spaces_taken[0] == player and self.spaces_taken[3] == player and self.spaces_taken[6] == player:
            print(f"\n{player} is the winner!")
            self.has_winner = True

        # Middle column
        elif self.spaces_taken[1] == player and self.spaces_taken[4] == player and self.spaces_taken[7] == player:
            print(f"\n{player} is the winner!")
            self.has_winner = True

        # Last column
        elif self.spaces_taken[2] == player and self.spaces_taken[5] == player and self.spaces_taken[8] == player:
            print(f"\n{player} is the winner!")
            self.has_winner = True

        # Top left to bottom right diagonal
        elif self.spaces_taken[0] == player and self.spaces_taken[4] == player and self.spaces_taken[8] == player:
            print(f"\n{player} is the winner!")
            self.has_winner = True

        # Top right to bottom left diagonal
        elif self.spaces_taken[2] == player and self.spaces_taken[4] == player and self.spaces_taken[6] == player:
            print(f"\n{player} is the winner!")
            self.has_winner = True

    # Print the board
    def print_board(self):
        for i in range(0, len(self.spaces)):
            print(self.spaces[i], end="")