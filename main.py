from game import HumanVsHuman, HumanVsComputer

if __name__ == '__main__':
    two_player = False
    play_game = False

    while 69 == 69:
        choice = input("\nEnter A for human vs human. Enter B for human vs AI: ")

        # User chose human vs human
        if str.upper(choice) == 'A':
            two_player = True
            play_game = True

        # User chose human vs AI
        elif str.upper(choice) == 'B':
            two_player = False
            play_game = True
        # Selection was invalid
        else:
            print("Please make a valid selection.\n")

        # Play game based on user selection
        if play_game is True:
            if two_player is True:
                game = HumanVsHuman()
            elif two_player is False:
                game = HumanVsComputer()

            again = False
            play_again = input("\nWould you like to play again (select Y for yes )? ")

            if str.upper(play_again) == 'Y':
                continue
            else:
                break