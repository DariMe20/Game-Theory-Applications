# Game Theory Applications

This repository contains multiple algorithms and simulations for solving game-theoretic problems. The code implements solutions for various game-theory-based challenges, including determining Pure Nash Equilibrium, evaluating strategies in decision games, and solving extensive-form games using backward induction. 

The repository includes the following problems and solutions:

### 1. **Pure Nash Equilibrium in Normal-Form Games (Problem 1)**  
   - **Objective**: To create an algorithm that identifies Pure Nash Equilibrium (Pure NE) for a 2-player normal-form game.
   - **Details**: The algorithm checks for the existence of Pure NE and returns all the Pure NEs for a given game setup. It can be tested using both manually entered payoffs or randomly generated payoffs.
   - **Features**: 
     - Input: Number of strategies for each player, choice of manually inputting payoffs or generating them randomly.
     - Output: All Pure Nash Equilibrium for the defined game.
   - **Example Results**:
     - Prisoner’s Dilemma, Matching Pennies, and other scenarios with random and manually set payoffs.

### 2. **The Monty Hall Problem (Problem 2)**  
   - **Objective**: To simulate the Monty Hall game for different numbers of doors and evaluate the winning probabilities for two strategies: staying with the initial choice and switching to another door.
   - **Details**: The game is simulated for various values of `N` (number of doors) and `K` (number of repetitions). The win probability is calculated for both strategies.
   - **Features**: 
     - Input: Number of doors (N) and number of repetitions (K).
     - Output: Probability of winning for both strategies.
   - **Example Results**:  
     - For `N = 3` doors, probabilities evolve from 20% (Stay) and 70% (Switch) for 10 repetitions to 33.15% (Stay) and 66.80% (Switch) for 10,000 repetitions.

### 3. **Sub-game Perfect Nash Equilibrium (SPNE) in a Bargaining Game (Problem 3)**  
   - **Objective**: To analyze a simple bargaining game between two players involving dividing $10, determining the subgame perfect Nash equilibrium (SPNE), and identifying non-SPNE Nash equilibrium.
   - **Details**: The game involves Player 1 proposing a division, and Player 2 either accepting or rejecting it. The SPNE is found using backward induction.


### 4. **Backward Induction for Extensive-Form Games (Problem 4)**  
   - **Objective**: To solve general extensive-form games by backward induction to find the Subgame Perfect Nash Equilibrium (SPNE) and determine when the game will end.
   - **Details**: The game alternates between two players, each deciding whether to stop or continue at each round. The payoffs are given as a sequence of choices, and the SPNE is computed.
   - **Features**: 
     - Input: Number of rounds and player payoffs.
     - Output: The round at which the game ends, which player stops, and the corresponding payoffs.

### Repository Features:
- **Executable Code**: Ready-to-run Python code for all game-theory problems.
- **Customizable Parameters**: Users can change game parameters, such as the number of strategies, rounds, and player payoffs.
- **Randomization**: Some problems include randomization options for generating payoffs.

For full access to the code, documentation, and example tests, please check the [GitHub repository](https://github.com/DariMe20/Game-Theory-Applications).
