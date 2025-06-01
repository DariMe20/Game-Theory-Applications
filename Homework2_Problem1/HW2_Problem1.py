import itertools
import random


def get_game_data():
    n = int(input("Enter number of players (max 10): "))
    assert 1 < n <= 10, "Number of players must be between 2 and 10."

    strategy_counts = []
    for i in range(n):
        count = int(input(f"Enter number of strategies for Player {i + 1}: "))
        strategy_counts.append(count)

    manual = input("Do you want to enter payoffs manually? (YES/NO): ").strip().upper() == "YES"
    payoff_tensor = {}

    # Generate all possible strategy matrix_cells
    matrix_cells = list(itertools.product(*[range(c) for c in strategy_counts]))

    for matrix_cell in matrix_cells:
        if manual:
            payoffs = list(
                map(int, input(f"Enter payoffs for matrix_cell {matrix_cell} (space-separated, {n} values): ").split()))
        else:
            payoffs = [random.randint(0, 15) for _ in range(n)]
        payoff_tensor[matrix_cell] = payoffs

    return n, strategy_counts, payoff_tensor


def is_best_response(matrix_cell, player, strategy_counts, payoff_tensor):
    """
    Check if the strategy of 'player' in 'matrix_cell' is the best response.
    """
    current_payoff = payoff_tensor[matrix_cell][player]
    other_players = list(matrix_cell)
    best_payoff = current_payoff

    for s in range(strategy_counts[player]):
        if s == matrix_cell[player]:
            continue
        test_matrix_cell = tuple(other_players[:player] + [s] + other_players[player + 1:])
        if payoff_tensor[test_matrix_cell][player] > best_payoff:
            return False
    return True


def find_pure_nash_equilibrium(n, strategy_counts, payoff_tensor):
    equilibrium = []
    matrix_cells = payoff_tensor.keys()

    for matrix_cell in matrix_cells:
        if all(is_best_response(matrix_cell, player, strategy_counts, payoff_tensor) for player in range(n)):
            equilibrium.append((matrix_cell, payoff_tensor[matrix_cell]))
    return equilibrium


def main():
    while True:
        n, strategy_counts, payoff_tensor = get_game_data()

        equilibrium = find_pure_nash_equilibrium(n, strategy_counts, payoff_tensor)

        if equilibrium:
            print("\nPure Nash equilibrium:")
            for matrix_cell, payoffs in equilibrium:
                strategies = ', '.join(f"P{i + 1}-S{s + 1}" for i, s in enumerate(matrix_cell))
                print(f"({strategies}) with payoffs {tuple(payoffs)}")
        else:
            print("No pure Nash equilibrium found.")

        cont = input("\nDo you want to run another game? (YES/NO): ").strip().upper()
        if cont != "YES":
            print("Exiting the program. Goodbye!...")
            break


if __name__ == "__main__":
    main()
