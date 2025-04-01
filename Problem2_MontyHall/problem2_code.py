import random

def simulate_game(N, K, strategy):
    win_count = 0
    for _ in range(K):
        # Randomly place the gift behind one of the doors
        gift_position = random.randint(0, N - 1)

        # Player randomly chooses a door
        initial_choice = random.randint(0, N - 1)

        if strategy == "stay":
            # Strategy 1: Stay with the initial choice
            if initial_choice == gift_position:
                win_count += 1
        elif strategy == "switch":
            # Strategy 2: Switch to the remaining door that is not the initial choice
            if gift_position != initial_choice:
                win_count += 1

    return win_count / K  # Return the win probability

def evaluate_probabilities(n, k_values):
    # Print headers for the table
    print(f"\nEvaluations for {n} doors with different k values:")
    print(f"{'k':<10} {'Stay Prob':<15} {'Switch Prob':<15}")

    for k in k_values:
        # Calculate probabilities for both strategies
        win_probability_stay = simulate_game(n, k, "stay")
        win_probability_switch = simulate_game(n, k, "switch")

        # Print results for the current k value
        print(f"{k:<10} {win_probability_stay * 100:.2f}%           {win_probability_switch * 100:<5.2f}%")

def main():
    while True:
        N = int(input("Enter the number of doors (N): "))  # Number of doors
        choice = input(
            "Would you like to evaluate with standard K values (10, 100, 1000, 10000) or input a custom K? (Enter 'standard' or 'custom'): ").lower()

        if choice == 'standard':
            K_values = [10, 100, 1000, 10000]
            evaluate_probabilities(N, K_values)
        elif choice == 'custom':
            K = int(input("Enter the number of simulations (K): "))  # Number of simulations
            evaluate_probabilities(N, [K])
        else:
            print("Invalid input. Please enter 'standard' or 'custom'.")
            continue

        # Ask the user if they want to evaluate another scenario
        again = input("\nDo you want to evaluate another set of doors or K values? (yes/no): ").lower()
        if again != 'yes':
            break

if __name__ == "__main__":
    main()
