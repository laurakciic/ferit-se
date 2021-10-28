while True:
    player1 = input("Player1, enter your choice: ")
    player2 = input("Player2, enter your choice: ")


    if player1 == player2:
        print("Both choices are same!")
    elif player1 == 'rock':
        if player2 == 'scissors':
            print("Player1 wins!")
        if player2 == 'paper':
            print("Player2 wins!")
    elif player1 == 'scissors':
        if player2 == 'rock':
            print("Player2 wins!")
        if player2 == 'paper':
            print("Player2 wins!")
    elif player1 == 'paper':
        if player2 == 'rock':
            print("Player1 wins")
        if player2 == 'scissors':
            print("Player2 wins!")

    resume = input("\nType 'yes' to continue and 'no' to quit the game: ")
    if resume == "no":
        break