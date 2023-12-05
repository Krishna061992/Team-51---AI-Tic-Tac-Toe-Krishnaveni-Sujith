### TicTacToe - AI Final project

### Implementation of Multiple Tic Tac Toe Agents in a Tournament setting

#### Introduction:
Tic Tac Toe, a game for two players on a square grid, follows the principles of a zero-sum game, where Player 1's victory corresponds to Player 2's defeat. Traditionally, players take turns marking the grid with either X or O. Player 1 is designated the X key, while Player 2 is assigned the O key. A player secures victory by successfully placing their key in all the cells of a row, column, or diagonal.

#### Algorithms used:
We have created four Agents to play against each other.

#### 1. Minimax Agent
#### 2. Alpha beta Minimax Agent
#### 3. Expectimax Agent
#### 4. Q-Learning Agent

### Minimax Algorithm:

Minimax stands as a backtracking algorithm extensively employed in decision-making and game theory, particularly in two-player zero-sum games, to determine the most optimal move. In the representation of the Minimax tree, each node corresponds to a game state resulting from a specific action. The tree consists of recursive layers of maximizer and minimizer nodes, where the maximizer aims to maximize the player's outcome, and the minimizer seeks to minimize the player's potential gains.

### Alpha Beta Minimax Algorithm:
This closely resembles the Minimax algorithm, with a key distinction. In this variant, the algorithm determines the specific child nodes or game states to explore further before determining the optimal value. This selection process relies on alpha and beta values, where alpha represents the best value for the maximizer, and beta represents the best value for the minimizer.

### Expectimax Algorithm:
This method bears resemblance to Minimax, but it incorporates a chance node alongside the minimizer. Unlike Minimax, which presupposes optimal play from the opponent, this algorithm introduces a chance node that reflects the average of all available nodes, representing the expected utility. The underlying assumption is that the opponent's next move is influenced by chance rather than consistently optimal choices.

### Q-Learning Algorithm:
Q-Learning is a reinforcement-based algorithm designed for situations where the agent initially lacks knowledge about the environment. Through a process of playing a few games and receiving rewards, the agent gradually learns about the environment. The rewards help the agent discern which moves are advantageous and which are not. It is essential to train this agent with the game environment before participating in tournaments against other players.

### Instructions to run code:
On Windows, press Win + R, type cmd, and press Enter.
On macOS or Linux, open a terminal.
cd path\to\your\script
## C:\Users\Krishna\Desktop\Tictactoe\AI_FinalProject_Tic-Tac-Toe>
python your_script.py
## python tictactoe.py
#### Run the file multiagent_tictactoe.py
#### Enter agent1 and agent2 as shown in the console and see how the agents play.
#### Execute the process multiple times and assess performance across various agents to determine which one demonstrates superior gameplay..
#### Make sure you select 2 different agents for Tic-Tac-Toe game.


