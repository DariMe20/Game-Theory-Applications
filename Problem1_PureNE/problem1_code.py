import random
import time


def read_payoff_matrix(num_strategies, player, is_player2=False):
    """
    Reads the payoff matrix for a player. If it's for Player 2, the payoffs are read column-wise.
    """
    print(f"Enter the payoff matrix for {player} (each row represents the strategies for the other player):")
    matrix = []

    # For Player 2, we need to read payoffs column-wise
    if is_player2:
        for i in range(num_strategies):
            # Read the payoffs for Player 2's strategy i, separated by spaces
            row = list(map(int, input(
                f"Enter the payoffs for Player {player}'s strategy {i + 1}, separated by spaces: ").split()))
            # Ensure the number of payoffs matches the number of Player 1's strategies
            if len(row) != num_strategies:
                print(f"Error: You must enter {num_strategies} payoffs for each strategy.")
                return None
            matrix.append(row)
    else:
        # For Player 1, we read payoffs row-wise (as before)
        for i in range(num_strategies):
            # Read the payoffs for Player 1's strategy i, separated by spaces
            row = list(map(int, input(
                f"Enter the payoffs for Player {player}'s strategy {i + 1}, separated by spaces: ").split()))
            matrix.append(row)

    return matrix


# Function to generate a random payoff matrix
def generate_random_payoff_matrix(num_strategies1, num_strategies2):
    matrix = []
    for i in range(num_strategies1):
        row = [random.randint(0, 15) for _ in range(num_strategies2)]
        matrix.append(row)
    return matrix


# Function to find pure Nash Equilibrium
def find_pure_nash_equilibrium(player1_strategies, player2_strategies, payoffs_player1, payoffs_player2):
    pure_ne = []

    # Create to vectors that saves the best response for all the opposite player's strategies
    best_response_player1 = [None] * len(player2_strategies)
    best_response_player2 = [None] * len(player1_strategies)

    # Take Player 1 and calculate the best response to every Player 2 strategy
    for j in range(len(player2_strategies)):
        # The max payoff is the best payoff of strategy i for player 1 when player 2 plays strategy j
        max_payoff = max(payoffs_player1[i][j] for i in range(len(player1_strategies)))
        # I save the best response of player 1 in strategy with index j by searching the response that is equal to max
        best_response_player1[j] = {i for i in range(len(player1_strategies)) if payoffs_player1[i][j] == max_payoff}

    # Take Player 2 and calculate the best response to every Player 1 strategy
    for i in range(len(player1_strategies)):
        # The max payoff is the best payoff of strategy k for player 2 when player 1 plays strategy i
        max_payoff = max(payoffs_player2[i][k] for k in range(len(player2_strategies)))
        # Save the best response of player 2 in strategy with index i by searching the response that is equal to max
        best_response_player2[i] = {k for k in range(len(player2_strategies)) if payoffs_player2[i][k] == max_payoff}

    # Now I just need to iterate through every strategy and check if i and j are simultaneously in the best response array
    for i in range(len(player1_strategies)):
        for j in range(len(player2_strategies)):
            # First I check if strategy i is in the list of best responses for player 1 against player's 2 strategy j
            # Then I do the same with player 2
            # If strategy P1-Si is best against any P2-Sj and P2-Sj is best against P1-Si that means that no player would
            # gain a better payoff by unilaterally changing their strategy
            if i in best_response_player1[j] and j in best_response_player2[i]:
                pure_ne.append(
                    (player1_strategies[i], player2_strategies[j], payoffs_player1[i][j], payoffs_player2[j][i]))
    return pure_ne


# Main function to execute the game logic
def main():
    # Input: number of strategies for each player
    num_strategies_player1 = int(input("Enter the number of strategies for Player 1: "))
    num_strategies_player2 = int(input("Enter the number of strategies for Player 2: "))

    # Input: Manual or automatic (random) payoff matrix
    manual_input = input("Would you like to manually enter the payoffs? (YES/NO): ").strip().upper()

    # Read or generate payoff matrices
    if manual_input == "YES":
        payoffs_player1 = read_payoff_matrix(num_strategies_player1, "Player 1")
        payoffs_player2 = read_payoff_matrix(num_strategies_player2, "Player 2", is_player2=True)
    else:
        payoffs_player1 = generate_random_payoff_matrix(num_strategies_player1, num_strategies_player2)
        payoffs_player2 = generate_random_payoff_matrix(num_strategies_player2, num_strategies_player1)

    # Define strategy labels for clarity
    player1_strategies = [f"S{i + 1}" for i in range(num_strategies_player1)]
    player2_strategies = [f"S{i + 1}" for i in range(num_strategies_player2)]

    print("Payoffs Player 1:\n", payoffs_player1)
    print("Payoffs Player 2:\n", payoffs_player2)

    start_time = time.time()
    # Find Pure Nash Equilibrium
    pure_ne = find_pure_nash_equilibrium(player1_strategies, player2_strategies, payoffs_player1, payoffs_player2)
    end_time = time.time()
    # Output results
    if pure_ne:
        print("\nThe Pure Nash Equilibria are:")
        for ne in pure_ne:
            print(f"(P1-{ne[0]}, P2-{ne[1]} with payoffs ({ne[2]}, {ne[3]})\n")
    else:
        print("\nNo Pure Nash Equilibrium found.")

    execution_time = end_time - start_time
    print(f"Execution time was: {execution_time} seconds")


# Run the main function
if __name__ == "__main__":
    main()
