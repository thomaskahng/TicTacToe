from gameComponents import GameComponents
from random import randint

class HumanVsHuman:
    def __init__(self):
        # Are players ready
        self.ready_player1 = False
        self.ready_player2 = False

        # Store components of game and play the games once players are ready
        self.game = GameComponents(True)
        self.players_ready()
        self.play_game()

    def players_ready(self):
        while 69 == 69:
            # Ask if player 1 is ready
            if self.ready_player1 is False:
                input_1 = input("Player 1, are you ready (press Y if you're ready)? ")
                if str.upper(input_1) == 'Y':
                    self.ready_player1 = True

            # Ask if player 2 is ready
            if self.ready_player2 is False:
                input_2 = input("Player 2, are you ready (press Y if you're ready)? ")
                if str.upper(input_2) == 'Y':
                    self.ready_player2 = True

            # Both players are ready
            if self.ready_player1 is True and self.ready_player2 is True:
                break

    def play_game(self):
        while self.game.has_winner is False:
            # All squares selected and no winner, game is a draw
            if self.game.turns == 9:
                print("\nThe game is a draw!")
                break

            # Even iterations are player 1's turn, odd iterations are player 2's turn
            if self.game.turns % 2 == 0:
                self.game.whos_turn = "Player 1"
            else:
                self.game.whos_turn = "Player 2"

            try:
                # If space is not taken, evaluate space
                num_space = int(input(f"\n{self.game.whos_turn}'s turn (enter space): "))
                if len(self.game.spaces_taken[num_space]) == 0:
                    # Indicate who took that space and take a turn
                    self.game.spaces_taken[num_space] = self.game.whos_turn
                    self.game.turns += 1

                    # Put an O where necessary, print board, and see if someone won the game
                    if self.game.whos_turn == "Player 1":
                        self.game.put_space(num_space, 'O')
                        self.game.print_board()
                        self.game.evaluate_winner(self.game.whos_turn)

                    # Put an X where necessary, print board, and see if someone won the game
                    elif self.game.whos_turn == "Player 2":
                        self.game.put_space(num_space, 'X')
                        self.game.print_board()
                        self.game.evaluate_winner(self.game.whos_turn)

                # Space chosen is already taken
                elif len(self.game.spaces_taken[num_space]) > 0:
                    print("That space is already taken! Try again!")
                else:
                    print("Invalid space! Try again!")

            # Catch errors
            except ValueError as e:
                print("Invalid selection!")
            except IndexError as i:
                print("Invalid selection!")

class HumanVsComputer:
    def __init__(self):
        # See if human is ready
        self.ready_human = False
        self.computer_took_turn = False

        # Play game once human is ready
        self.game = GameComponents(True)
        self.human_ready()
        self.play_game()

    def human_ready(self):
        while self.ready_human is False:
            input_human = input("Human are you ready (press Y if you're ready)? ")
            # Ask if human is ready
            if str.upper(input_human) == 'Y':
                self.ready_human = True

    def play_game(self):
        while self.game.has_winner is False:
            # All squares selected and no winner, game is a draw
            if self.game.turns == 9:
                print("\nThe game is a draw!")
                break

            # Even iterations are human's turn, odd iterations are computer's turn
            if self.game.turns % 2 == 0:
                self.game.whos_turn = "Human"

                try:
                    # If space is not taken, evaluate space and put in board
                    num_space = int(input(f"\n{self.game.whos_turn}'s turn (enter space): "))
                    if len(self.game.spaces_taken[num_space]) == 0:
                        self.put_in_board(num_space, 'O')

                    # Space chosen is already taken
                    elif len(self.game.spaces_taken[num_space]) > 0:
                        print("That space is already taken! Try again!")

                    # Selection is invalid
                    else:
                        print("Invalid selection!")

                # Catch errors
                except ValueError as e:
                    print("Invalid selection!")
                except IndexError as i:
                    print("Invalid selection!")
            else:
                # Computer's turn (reset whether turn was took)
                self.game.whos_turn = "Computer"
                self.computer_took_turn = False
                print("\nThis is computer's selection: ")

                # If move number 1 (computer's first move)
                if self.game.turns == 1:
                    # Take middle if possible (put in board at the end)
                    if len(self.game.spaces_taken[4]) == 0:
                        self.put_in_board(4, 'X')

                    # Else, randomly pick another space (put in board at the end)
                    else:
                        rand = randint(0, 3)
                        if rand == 0:
                            self.put_in_board(0, 'X')
                        elif rand == 1:
                            self.put_in_board(2, 'X')
                        elif rand == 2:
                            self.put_in_board(6, 'X')
                        elif rand == 3:
                            self.put_in_board(8, 'X')

                else:
                    # Try to chase win
                    if self.computer_took_turn is False:
                        self.block_or_chase_win("Chase")

                    # If computer hasn't took turn yet, block possible player's win
                    if self.computer_took_turn is False:
                        self.block_or_chase_win("Block")

                    # If computer hasn't took turn, prevent win on diagonal
                    if self.computer_took_turn is False:
                        self.prevent_diagonal()

                    # If no win to chase or win to block, make a sequence
                    if self.computer_took_turn is False:
                        self.make_sequence()

    def prevent_diagonal(self):
        # If top right to bottom left is X,O,X
        if self.game.spaces_taken[2] == "Human" and self.game.spaces_taken[4] == "Computer" and self.game.spaces_taken[6] == "Human":
            # Take top middle space
            if self.game.spaces_taken[1] == "":
                self.put_in_board(1, 'X')
                self.computer_took_turn = True

            # Take middle left space
            elif self.game.spaces_taken[3] == "":
                self.put_in_board(3, 'X')
                self.computer_took_turn = True

            # Take middle right space
            elif self.game.spaces_taken[5] == "":
                self.put_in_board(5, 'X')
                self.computer_took_turn = True

            # Take bottom middle space
            elif self.game.spaces_taken[7] == "":
                self.put_in_board(7, 'X')
                self.computer_took_turn = True

        # If top left to bottom right is X,O,X
        elif self.game.spaces_taken[0] == "Human" and self.game.spaces_taken[4] == "Computer" and self.game.spaces_taken[8] == "Human":
            # Take top middle space
            if self.game.spaces_taken[1] == "":
                self.put_in_board(1, 'X')
                self.computer_took_turn = True

            # Take middle left space
            elif self.game.spaces_taken[3] == "":
                self.put_in_board(3, 'X')
                self.computer_took_turn = True

            # Take middle right space
            elif self.game.spaces_taken[5] == "":
                self.put_in_board(5, 'X')
                self.computer_took_turn = True

            # Take bottom middle space
            elif self.game.spaces_taken[7] == "":
                self.put_in_board(7, 'X')
                self.computer_took_turn = True

    def make_sequence(self):
        # Anything adjacent to top left
        if self.game.spaces_taken[0] == "Computer" and self.game.spaces_taken[1] == "":
            self.put_in_board(1, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[0] == "Computer" and self.game.spaces_taken[3] == "":
            self.put_in_board(3, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[0] == "Computer" and self.game.spaces_taken[4] == "":
            self.put_in_board(4, 'X')
            self.computer_took_turn = True

        # Anything adjacent to top middle
        elif self.game.spaces_taken[1] == "Computer" and self.game.spaces_taken[0] == "":
            self.put_in_board(0, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[1] == "Computer" and self.game.spaces_taken[2] == "":
            self.put_in_board(2, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[1] == "Computer" and self.game.spaces_taken[4] == "":
            self.put_in_board(4, 'X')
            self.computer_took_turn = True

        # Anything adjacent to top right
        elif self.game.spaces_taken[2] == "Computer" and self.game.spaces_taken[1] == "":
            self.put_in_board(1, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[2] == "Computer" and self.game.spaces_taken[4] == "":
            self.put_in_board(4, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[2] == "Computer" and self.game.spaces_taken[5] == "":
            self.put_in_board(5, 'X')
            self.computer_took_turn = True

        # Anything adjacent to middle left
        elif self.game.spaces_taken[3] == "Computer" and self.game.spaces_taken[0] == "":
            self.put_in_board(0, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[3] == "Computer" and self.game.spaces_taken[4] == "":
            self.put_in_board(4, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[3] == "Computer" and self.game.spaces_taken[6] == "":
            self.put_in_board(6, 'X')
            self.computer_took_turn = True

        # Anything adjacent to middle middle
        elif self.game.spaces_taken[4] == "Computer" and self.game.spaces_taken[0] == "":
            self.put_in_board(0, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[4] == "Computer" and self.game.spaces_taken[1] == "":
            self.put_in_board(1, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[4] == "Computer" and self.game.spaces_taken[2] == "":
            self.put_in_board(2, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[4] == "Computer" and self.game.spaces_taken[3] == "":
            self.put_in_board(3, 'X')
            self.computer_took_turn = True

        # Anything adjacent to middle middle
        elif self.game.spaces_taken[4] == "Computer" and self.game.spaces_taken[5] == "":
            self.put_in_board(5, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[4] == "Computer" and self.game.spaces_taken[6] == "":
            self.put_in_board(6, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[4] == "Computer" and self.game.spaces_taken[7] == "":
            self.put_in_board(7, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[4] == "Computer" and self.game.spaces_taken[8] == "":
            self.put_in_board(8, 'X')
            self.computer_took_turn = True

        # Anything adjacent to middle right
        elif self.game.spaces_taken[5] == "Computer" and self.game.spaces_taken[2] == "":
            self.put_in_board(2, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[5] == "Computer" and self.game.spaces_taken[4] == "":
            self.put_in_board(4, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[5] == "Computer" and self.game.spaces_taken[8] == "":
            self.put_in_board(8, 'X')
            self.computer_took_turn = True

        # Anything adjacent to bottom left
        elif self.game.spaces_taken[6] == "Computer" and self.game.spaces_taken[3] == "":
            self.put_in_board(3, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[6] == "Computer" and self.game.spaces_taken[4] == "":
            self.put_in_board(4, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[6] == "Computer" and self.game.spaces_taken[7] == "":
            self.put_in_board(7, 'X')
            self.computer_took_turn = True

        # Anything adjacent to bottom middle
        elif self.game.spaces_taken[7] == "Computer" and self.game.spaces_taken[4] == "":
            self.put_in_board(4, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[7] == "Computer" and self.game.spaces_taken[6] == "":
            self.put_in_board(6, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[7] == "Computer" and self.game.spaces_taken[8] == "":
            self.put_in_board(8, 'X')
            self.computer_took_turn = True

        # Anything adjacent to bottom right
        elif self.game.spaces_taken[8] == "Computer" and self.game.spaces_taken[4] == "":
            self.put_in_board(4, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[8] == "Computer" and self.game.spaces_taken[5] == "":
            self.put_in_board(5, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[8] == "Computer" and self.game.spaces_taken[7] == "":
            self.put_in_board(7, 'X')
            self.computer_took_turn = True
        else:
            pass

    def block_or_chase_win(self, block_or_chase):
        if block_or_chase == "Block":
            exec = "Human"
        else:
            exec = "Computer"

        # Block top row space from winning or chase the win
        if self.game.spaces_taken[0] == exec and self.game.spaces_taken[1] == exec and self.game.spaces_taken[2] == "":
            self.put_in_board(2, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[0] == exec and self.game.spaces_taken[1] == "" and self.game.spaces_taken[2] == exec:
            self.put_in_board(1, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[0] == "" and self.game.spaces_taken[1] == exec and self.game.spaces_taken[2] == exec:
            self.put_in_board(0, 'X')
            self.computer_took_turn = True

        # Block middle row space from winning or chase the win
        elif self.game.spaces_taken[3] == exec and self.game.spaces_taken[4] == exec and self.game.spaces_taken[5] == "":
            self.put_in_board(5, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[3] == exec and self.game.spaces_taken[4] == "" and self.game.spaces_taken[5] == exec:
            self.put_in_board(4, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[3] == "" and self.game.spaces_taken[4] == exec and self.game.spaces_taken[5] == exec:
            self.put_in_board(3, 'X')
            self.computer_took_turn = True

        # Block bottom row space from winning or chase the win
        elif self.game.spaces_taken[6] == exec and self.game.spaces_taken[7] == exec and self.game.spaces_taken[8] == "":
            self.put_in_board(8, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[6] == exec and self.game.spaces_taken[7] == "" and self.game.spaces_taken[8] == exec:
            self.put_in_board(7, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[6] == "" and self.game.spaces_taken[7] == exec and self.game.spaces_taken[8] == exec:
            self.put_in_board(6, 'X')
            self.computer_took_turn = True

        # Block left column space from winning or chase the win
        elif self.game.spaces_taken[0] == exec and self.game.spaces_taken[3] == exec and self.game.spaces_taken[6] == "":
            self.put_in_board(6, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[0] == exec and self.game.spaces_taken[3] == "" and self.game.spaces_taken[6] == exec:
            self.put_in_board(3, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[0] == "" and self.game.spaces_taken[3] == exec and self.game.spaces_taken[6] == exec:
            self.put_in_board(0, 'X')
            self.computer_took_turn = True

        # Block middle column space from winning or chase the win
        elif self.game.spaces_taken[1] == exec and self.game.spaces_taken[4] == exec and self.game.spaces_taken[7] == "":
            self.put_in_board(7, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[1] == exec and self.game.spaces_taken[4] == "" and self.game.spaces_taken[7] == exec:
            self.put_in_board(4, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[1] == "" and self.game.spaces_taken[4] == exec and self.game.spaces_taken[7] == exec:
            self.put_in_board(1, 'X')
            self.computer_took_turn = True

        # Block right column space from winning or chase the win
        elif self.game.spaces_taken[2] == exec and self.game.spaces_taken[5] == exec and self.game.spaces_taken[8] == "":
            self.put_in_board(8, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[2] == exec and self.game.spaces_taken[5] == "" and self.game.spaces_taken[8] == exec:
            self.put_in_board(5, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[2] == "" and self.game.spaces_taken[5] == exec and self.game.spaces_taken[8] == exec:
            self.put_in_board(2, 'X')
            self.computer_took_turn = True

        # Block top left to bottom right diagonal space from winning or chase the win
        elif self.game.spaces_taken[0] == exec and self.game.spaces_taken[4] == exec and self.game.spaces_taken[8] == "":
            self.put_in_board(8, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[0] == exec and self.game.spaces_taken[4] == "" and self.game.spaces_taken[8] == exec:
            self.put_in_board(4, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[0] == "" and self.game.spaces_taken[4] == exec and self.game.spaces_taken[8] == exec:
            self.put_in_board(0, 'X')
            self.computer_took_turn = True

        # Block top right to bottom left diagonal space from winning or chase the win
        elif self.game.spaces_taken[2] == exec and self.game.spaces_taken[4] == exec and self.game.spaces_taken[6] == "":
            self.put_in_board(6, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[2] == exec and self.game.spaces_taken[4] == "" and self.game.spaces_taken[6] == exec:
            self.put_in_board(4, 'X')
            self.computer_took_turn = True
        elif self.game.spaces_taken[2] == "" and self.game.spaces_taken[4] == exec and self.game.spaces_taken[6] == exec:
            self.put_in_board(2, 'X')
            self.computer_took_turn = True
        else:
            pass

    def put_in_board(self, put_in_space, to_put):
        # Indicate who took that space and take a turn
        self.game.spaces_taken[put_in_space] = self.game.whos_turn
        self.game.turns += 1

        # Put an X where necessary, print board, and see if someone won the game
        self.game.put_space(put_in_space, to_put)
        self.game.print_board()
        self.game.evaluate_winner(self.game.whos_turn)