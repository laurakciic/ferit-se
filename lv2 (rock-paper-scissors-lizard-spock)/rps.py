def winner(player1, player2):
    if player1 == player2:
        return("Both choices are same!")
    elif player1 == 'rock':
        if player2 == 'scissors':
            return("Player1 wins!")
        if player2 == 'paper':
            return("Player2 wins!")
    elif player1 == 'scissors':
        if player2 == 'rock':
            return("Player2 wins!")
        if player2 == 'paper':
            return("Player2 wins!")
    elif player1 == 'paper':
        if player2 == 'rock':
            return("Player1 wins")
        if player2 == 'scissors':
            return("Player2 wins!")
    return None

def main():
    while True:
        player1 = input("Player1, enter your choice: ")
        player2 = input("Player2, enter your choice: ")

        result = winner(player1, player2)
        print(result)

        resume = input("\nType 'yes' to continue and 'no' to quit the game: ")
        if resume == "no":
            break

if __name__ == "__main__":
    main()