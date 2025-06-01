import random


def get_payoffs(manual=True):
    """
    Read payoffs for a 2×2 game, explicitly indexed using (0,0), (0,1), etc.
    """
    A = [[0, 0], [0, 0]]
    B = [[0, 0], [0, 0]]

    if manual:
        print("Enter payoffs for each combination (strategy):")
        for i in range(2):
            for j in range(2):
                payoffs = list(
                    map(int, input(f"Player 1 and Player 2 at strategy ({i}, {j}) (format: P1 P2): ").split()))
                A[i][j] = payoffs[0]
                B[i][j] = payoffs[1]
    else:
        print("Random Payoffs:")
        print("Player 1 and Player 2:")
        for i in range(2):
            for j in range(2):
                A[i][j] = random.randint(0, 10000)
                B[i][j] = random.randint(0, 10000)
                print(f"({i}, {j}): Player 1 = {A[i][j]}, Player 2 = {B[i][j]}")

    return A, B


def compute_mixed_equilibrium(A, B):
    """
    Compute the mixed Nash equilibrium for a 2×2 game.
    """
    # Player 1 — solve for y (Player 2's mixing probability)
    a11, a12 = A[0][0], A[0][1]
    a21, a22 = A[1][0], A[1][1]

    numerator_y = a22 - a12
    denominator_y = (a11 - a21) - (a12 - a22)
    y = None
    if denominator_y != 0:
        y = numerator_y / denominator_y

    # Player 2 — solve for x (Player 1's mixing probability)
    b11, b21 = B[0][0], B[1][0]
    b12, b22 = B[0][1], B[1][1]

    numerator_x = b22 - b21
    denominator_x = (b11 - b12) - (b21 - b22)
    x = None
    if denominator_x != 0:
        x = numerator_x / denominator_x

    return x, y


def main():
    while True:
        choice = input("Do you want to enter payoffs manually? (YES/NO): ").strip().upper()
        manual = choice == "YES"

        A, B = get_payoffs(manual=manual)

        x, y = compute_mixed_equilibrium(A, B)

        if x is None or y is None:
            print("\nNo solution: at least one player has no incentive to mix.")
        elif not (0 < x < 1 and 0 < y < 1):
            print("\nNo fully mixed Nash equilibrium found (probabilities not strictly between 0 and 1).")
        else:
            print("\nFully Mixed Nash Equilibrium found:")
            print(f"Player 1:")
            print(f"  S1 with probability {round(x, 2)}, S2 with probability {round(1 - x, 2)}")
            print(f"Player 2:")
            print(f"  S1 with probability {round(y, 2)}, S2 with probability {round(1 - y, 2)}")

        cont = input("\nDo you want to run another game? (YES/NO): ").strip().upper()
        if cont != "YES":
            print("Exiting the program. Goodbye!...")
            break


if __name__ == "__main__":
    main()
