import random


# Function to simulate a general game with backward induction
def backward_induction(n, L, R):
    """
    Parameters:
    n (int): number of rounds (even, 2k)
    L (list): list of player 1's payoffs for each leaf (length 2k)
    R (list): list of player 2's payoffs for each leaf (length 2k)
    """
    round_payoffs = []  # To store round-wise payoffs for visualization

    # Start by considering the leaf nodes (final payoffs)
    payoffs_player_1 = L
    payoffs_player_2 = R

    # To store the optimal strategy (stop or continue) for each player at each round
    decisions_player1 = []
    decisions_player2 = []

    for round_num in range(n - 1, -1, -1):
        if round_num % 2 != 0:  # Player 1's turn
            # Player 1's decision: Stop or Continue
            current_round_payoff = payoffs_player_1[round_num]
            previous_round_payoff = payoffs_player_1[round_num - 1]

            if current_round_payoff > previous_round_payoff:  # Player 1 prefers to continue
                decisions_player1.append('continue')
            else:  # Player 1 prefers to stop
                decisions_player1.append('stop')

        else:  # Player 2's turn
            # Player 2's decision: Stop or Continue
            current_round_payoff = payoffs_player_2[round_num]
            previous_round_payoff = payoffs_player_2[round_num - 1]

            if current_round_payoff > previous_round_payoff:  # Player 2 prefers to continue
                decisions_player1.append('continue')
            else:  # Player 2 prefers to stop
                decisions_player2.append('stop')

    decisions_player1.reverse()
    decisions_player2.reverse()

    # Output the results
    # print(f"\nDecisions lists for each round: \n Player1: {decisions_player1},\n Player2: {decisions_player2}")
    for i in range(n):
        if decisions_player1[i] == "stop":
            # Player 1 stop first
            print(f"Game ends at round {i + 1} by Player 1. Payoffs are ({payoffs_player_1[i], payoffs_player_2[i]}")
            break
        if decisions_player2[i] == "stop":
            if i < n:
                print(
                    f"Game ends at round {i + 2} by Player 2. Payoffs are ({payoffs_player_1[i + 1], payoffs_player_2[i + 1]}")
                break
            else:
                print(
                    f"Game ends at round {i + 2} by Player 2. Payoffs are ({payoffs_player_1[n], payoffs_player_2[n]}")
                break


# Function to input the payoffs manually or randomly
def get_payoffs(n):
    L = []
    R = []

    option = input("Do you want to enter payoffs manually or use random values? (manual/random): ").strip().lower()

    if option == "manual":
        for i in range(n):
            print(f"Round {i + 1}:")
            p1 = int(input(f"Payoff Player 1: "))
            p2 = int(input(f"Payoff Player 2: "))
            L.append(p1)
            R.append(p2)

    elif option == "random":
        L = [random.randint(1, 10) for _ in range(n)]
        R = [random.randint(1, 10) for _ in range(n)]
        print("Random payoffs generated:")
        print("Player 1's payoffs (L):", L)
        print("Player 2's payoffs (R):", R)
    else:
        print("Invalid input! Please choose 'manual' or 'random'.")
        return get_payoffs(n)

    return L, R


# Main function
def main():
    # Ensure n is even
    while True:
        try:
            n = int(input("Enter the number of rounds (n, even number): "))
            if n % 2 != 0:
                print("The number of rounds must be even. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a valid number for n.")

    # Get the payoffs (manual or random)
    L, R = get_payoffs(n)

    # Run backward induction algorithm
    backward_induction(n, L, R)

    # Wait for the user to press Enter before closing
    input("Press Enter to exit...")


# Run the program
if __name__ == "__main__":
    main()
