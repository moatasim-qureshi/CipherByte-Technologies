def play_game():
    def get_valid_number(player_name):
        while True:
            try:
                number = input(f"ENTER A 6 DIGIT NUMBER [{player_name.upper()}]: ")
                if len(number) != 6:
                    raise ValueError("Please enter a 6-digit number.")
                return number
            except ValueError as e:
                print(e)
                
    player_1_name = input("ENTER PLAYER 1 NAME: ").upper()
    player_2_name = input("ENTER PLAYER 2 NAME: ").upper()
    print()
    
    player_1_number = get_valid_number(player_1_name)
    print()

    player_2_guesses = input(f"START GUESSING [{player_2_name}]: ")

    player_1_tries = 0
    player_2_tries = 0

    if player_1_number == player_2_guesses:
        print("\n  -----GAME OVER--------\n")
        print(f"   {player_2_name} IS MASTERMIND\n" )
        return

    else:
        while True:
            if player_1_number == player_2_guesses:
                print("\n -------CONGRATS NUMBER GUESSED----------\n" )
                break
            player_2_tries += 1
            for i in range(len(player_1_number)):
                if player_1_number[i] == player_2_guesses[i]:
                    print(player_1_number[i],end=" ")
                else:
                    print("_",end=" ")

            player_2_guesses = input("  |   GUESS AND ALWAYS WRITE A FULL NUMBER: ")

    print(f"\n----YOUR TURN {player_2_name}----\n")

    player_2_number = get_valid_number(player_2_name)
    print()
    player_1_guesses = input(f"START GUESSING [{player_1_name}]: ")

    if player_2_number == player_1_guesses:
        print("\n  -----GAME OVER--------\n")
        print(f"   {player_1_name} IS MASTERMIND\n" )
        return

    else:
        while True:
            if player_2_number == player_1_guesses:
                print("\n -------CONGRATS NUMBER GUESSED----------\n" )
                break
            player_1_tries += 1

            for i in range(len(player_2_number)):
                if player_2_number[i] == player_1_guesses[i]:
                    print(player_2_number[i],end=" ")
                else:
                    print("_",end=" ")

            player_1_guesses = input("  |   GUESS AND ALWAYS WRITE A FULL NUMBER: ")
    
    print("RESULTS:")
    print(f'\n   {player_1_name} TRIES WERE {player_1_tries}')
    print(f'   {player_2_name} TRIES WERE {player_2_tries}')
    print(f"   SO,\n")

    if player_1_tries > player_2_tries:
        print(f"   ------{player_2_name} IS MASTERMIND------\n" )

    elif player_2_tries > player_1_tries:
        print(f"   -----{player_1_name} IS MASTERMIND------\n" )

    else:
        print("   -----GAME DRAW------\n")

play_game()
