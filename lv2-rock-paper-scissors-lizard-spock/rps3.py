def winner(player1, player2, player3):
    if not check_inputs(player1, player2, player3):
        return False

    p1Points = p2Points = p3Points = 0
    if player1 == player2 == player3:
        return("draw")
    elif player1 == "rock":
        if player2 == "rock":
            pass
        if player2 == "scissors":
            p1Points += 1
        if player2 == "paper":
            p2Points += 1
        if player2 == "lizard":
            p1Points += 1
        if player2 == "spock":
            p2Points += 1
        if player3 == "rock":
            pass
        if player3 == "scissors":
            p1Points += 1
        if player3 == "paper":
            p3Points += 1
        if player3 == "lizard":
            p1Points += 1
        if player3 == "spock":
            p3Points += 1

    elif player1 == "scissors":
        if player2 == "scissors":
            pass
        if player2 == "rock":
            p2Points += 1
        if player2 == "paper":
            p1Points += 1
        if player2 == "lizard":
            p1Points += 1
        if player2 == "spock":
            p2Points += 1
        if player3 == "scissors":
            pass
        if player3 == "scissors":
            p1Points += 1
        if player3 == "paper":
            p3Points += 1
        if player3 == "lizard":
            p1Points += 1
        if player3 == "spock":
            p3Points += 1

    elif player1 == "paper":
        if player2 == "paper":
            pass
        if player2 == "rock":
            p1Points += 1
        if player2 == "scissors":
            p2Points += 1
        if player2 == "lizard":
            p2Points += 1
        if player2 == "spock":
            p1Points += 1
        if player3 == "paper":
            pass
        if player3 == "scissors":
            p1Points += 1
        if player3 == "rock":
            p1Points += 1
        if player3 == "lizard":
            p3Points += 1
        if player3 == "spock":
            p3Points += 1

    elif player1 == "lizard":
        if player2 == "lizard":
            pass
        if player2 == "rock":
            p2Points += 1
        if player2 == "paper":
            p1Points += 1
        if player2 == "scissors":
            p2Points += 1
        if player2 == "spock":
            p1Points += 1
        if player3 == "lizard":
            pass
        if player3 == "scissors":
            p3Points += 1
        if player3 == "paper":
            p1Points += 1
        if player3 == "lizard":
            pass
        if player3 == "spock":
            p1Points += 1
    
    elif player1 == "spock":
        if player2 == "spock":
            pass
        if player2 == "rock":
            p1Points += 1
        if player2 == "paper":
            p2Points += 1
        if player2 == "scissors":
            p1Points += 1
        if player2 == "lizard":
            p2Points += 1
        if player3 == "spock":
            pass
        if player3 == "scissors":
            p1Points += 1
        if player3 == "paper":
            p3Points += 1
        if player3 == "lizard":
            p1Points += 1
        if player3 == "spock":
            p3Points += 1

    if player2 == "rock":
        if player3 == "rock":
            pass    
        if player3 == "scissors":
            p2Points += 1
        if player3 == "paper":
            p3Points += 1
        if player3 == "lizard":
            p2Points += 1
        if player3 == "spock":
            p3Points += 1

    elif player2 == "paper":
        if player3 == "paper":
            pass
        if player3 == "scissors":
            p3Points += 1
        if player3 == "rock":
            p2Points += 1
        if player3 == "lizard":
            p3Points += 1
        if player3 == "spock":
            p2Points += 1

    elif player2 == "scissors":
        if player3 == "scissors":
            pass
        if player3 == "paper":
            p2Points += 1
        if player3 == "rock":
            p3Points += 1
        if player3 == "lizard":
            p2Points += 1
        if player3 == "spock":
            p3Points += 1

    elif player2 == "lizard":
        if player3 == "lizard":
            pass
        if player3 == "paper":
            p2Points += 1
        if player3 == "rock":
            p3Points += 1
        if player3 == "scissors":
            p3Points += 1
        if player3 == "spock":
            p2Points += 1
    
    elif player2 == "spock":
        if player3 == "spock":
            pass
        if player3 == "paper":
            p3Points += 1
        if player3 == "rock":
            p2Points += 1
        if player3 == "lizard":
            p3Points += 1
        if player3 == "scissors":
            p2Points += 1
    
    print("P1:" + str(p1Points), "P2:" + str(p2Points), "P3:" + str(p3Points))
    if p1Points == p2Points == p3Points:
        return ("draw")
    elif (p1Points == p2Points) > p3Points:
        return ("Player1 and Player2 share 1st place.")
    elif (p1Points == p3Points) > p2Points:
        return ("Player1 and Player3 share 1st place.")
    elif (p2Points == p3Points) > p1Points:
        return ("Player2 and Player3 share 1st place.")
    allPoints = (p1Points, p2Points, p3Points)
    win =  max(allPoints)
    if win == p1Points:
        return ("player1")
    elif win == p2Points:
        return ("player2")
    elif win == p3Points:
        return ("player3")

    return False

def is_valid_input(inp):
    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    return inp in choices

def check_inputs(p1, p2, p3):
    return is_valid_input(p1) and is_valid_input(p2) and is_valid_input(p3)

def main():
    while True:
        player1 = input("Player1, enter your choice: ")
        player2 = input("Player2, enter your choice: ")
        player3 = input("Player3, enter your choice: ")
        if check_inputs(player1, player2, player3):
            result = winner(player1, player2, player3)
        else:
            print("Wrong typo, try again.")
            continue
        
        print(result)

        resume = input("\nType 'yes' to continue and 'no' to quit the game: ")
        if resume == "no":
            break

def run_test(player1, player2, player3, expected):
    print(player1, "vs.", player2, "vs.", player3)
    result = winner(player1, player2, player3)
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

    run_test("rock", "rock", "rock", "draw")
    run_test("paper", "paper", "paper", "draw")
    run_test("scissors", "scissors", "scissors", "draw")
    run_test("lizard", "lizard", "lizard", "draw")
    run_test("spock", "spock", "spock", "draw")

    run_test("lizard", "spock", "scissors", "draw")     
    run_test("rock", "paper", "lizard", "draw")
    run_test("scissors", "paper", "spock", "draw")

    run_test("paper", "paper", "rock", "Player1 and Player2 share 1st place.")
    run_test("paper", "rock", "paper", "Player1 and Player3 share 1st place.")
    run_test("paper", "rock", "rock", "player1")
    run_test("rock", "paper", "rock", "player2")
    run_test("rock", "paper", "paper", "Player2 and Player3 share 1st place.")
    run_test("rock", "paper", "rock", "player2")
    run_test("rock", "rock", "paper", "player3")

    run_test("rock", "lizard", "scissors", "player1")
    run_test("paper", "scissors", "lizard", "player2")
    run_test("scissors", "spock", "rock", "player2")

    run_test("scissors", "spock", "slizard", False)
    run_test("pero", "djuro", "spock", False)
    run_test("", "scissors", "", False)
    run_test("pero", "pero", "lizard", False)
    run_test("", "", "", False)

if __name__ == "__main__":
    # main()
    unit_tests()