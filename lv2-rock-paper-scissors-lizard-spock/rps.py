def winner(player1, player2):
    if not check_inputs(player1, player2):
        return False

    if player1 == player2:
        return("draw")
    elif player1 == "rock":
        if player2 == "scissors":
            return("player1")
        if player2 == "paper":
            return("player2")
        if player2 == "lizard":
            return("player1")
        if player2 == "spock":
            return("player2")

    elif player1 == "scissors":
        if player2 == "rock":
            return("player2")
        if player2 == "paper":
            return("player1")
        if player2 == "lizard":
            return("player1")
        if player2 == "spock":
            return("player2")

    elif player1 == "paper":
        if player2 == "rock":
            return("player1")
        if player2 == "scissors":
            return("player2")
        if player2 == "lizard":
            return("player2")
        if player2 == "spock":
            return("player1")

    elif player1 == "lizard":
        if player2 == "rock":
            return("player2")
        if player2 == "paper":
            return("player1")
        if player2 == "scissors":
            return("player2")
        if player2 == "spock":
            return("player1")
    
    elif player1 == "spock":
        if player2 == "rock":
            return("player1")
        if player2 == "paper":
            return("player2")
        if player2 == "scissors":
            return("player1")
        if player2 == "lizard":
            return("player2")
    return False

def is_valid_input(inp):
    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    return inp in choices

def check_inputs(p1, p2):
    return is_valid_input(p1) and is_valid_input(p2)

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
    try:
        assert result == expected
    except AssertionError:
        print("expected: ", expected)
        print("result: ", result)
        raise # za traceback error poruku
    print("PASS")

def test_inputs(inp, expected):
    result = is_valid_input(inp)
    try:
        assert result == expected
    except AssertionError:
        print("expected: ", expected)
        print("result: ", result)
        raise # za traceback error poruku
    print("PASS")

def unit_tests():
    test_inputs("rock", True)
    test_inputs("paper", True)
    test_inputs("scissors", True)
    test_inputs("lizard", True)
    test_inputs("spock", True)
    test_inputs("pero", False)
    test_inputs("", False)
    test_inputs(8, False)

    run_test("rock", "paper", "player2")
    run_test("rock", "scissors", "player1")
    run_test("rock", "rock", "draw")
    run_test("rock", "lizard", "player1")
    run_test("rock", "spock", "player2")

    run_test("paper", "paper", "draw")
    run_test("paper", "rock", "player1")
    run_test("paper", "scissors", "player2")
    run_test("paper", "lizard", "player2")
    run_test("paper", "spock", "player1")

    run_test("scissors", "scissors", "draw")
    run_test("scissors", "rock", "player2")
    run_test("scissors", "paper", "player1")
    run_test("scissors", "lizard", "player1")
    run_test("scissors", "spock", "player2")

    run_test("lizard", "lizard", "draw")
    run_test("lizard", "rock", "player2")
    run_test("lizard", "paper", "player1")
    run_test("lizard", "scissors", "player2")
    run_test("lizard", "spock", "player1")

    run_test("spock", "spock", "draw")
    run_test("spock", "lizard", "player2")
    run_test("spock", "paper", "player2")
    run_test("spock", "rock", "player1")
    run_test("spock", "scissors", "player1")

    run_test("pero", "djuro", False)
    run_test("", "scissors", False)
    run_test("pero", "pero", False)
    

if __name__ == "__main__":
    # main()
    unit_tests()