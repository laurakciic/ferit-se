def winner(player1, player2):
    if player1 == player2:
        return("draw")
    elif player1 == "rock":
        if player2 == "scissors":
            return("player1")
        if player2 == "paper":
            return("player2")
    elif player1 == "scissors":
        if player2 == "rock":
            return("player2")
        if player2 == "paper":
            return("player1")
    elif player1 == "paper":
        if player2 == "rock":
            return("player1")
        if player2 == "scissors":
            return("player2")
    return None

def check_inputs(p1, p2):
    choices = ["rock", "paper", "scissors"]
    if p1 in choices and p2 in choices:
        return True
    else:
        return False

def main():
    while True:
        player1 = input("Player1, enter your choice: ")
        player2 = input("Player2, enter your choice: ")
        if check_inputs(player1, player2):
            result = winner(player1, player2)
        else:
            print("Wrong typo, try again ")
            continue
        
        print(result)

        resume = input("\nType 'yes' to continue and 'no' to quit the game: ")
        if resume == "no":
            break

def run_test(player1, player2, expected):
    print(player1, "vs.", player2)
    result = winner(player1, player2)
    assert result == expected
    print("PASS")

def unit_tests():
    run_test("rock", "paper", "player2")
    run_test("rock", "scissors", "player1")
    run_test("rock", "rock", "draw")
    run_test("paper", "paper", "draw")
    run_test("paper", "rock", "player1")
    run_test("paper", "scissors", "player2")
    run_test("scissors", "scissors", "draw")
    run_test("scissors", "rock", "player2")
    run_test("scissors", "paper", "player1")

if __name__ == "__main__":
    # main()
    unit_tests()