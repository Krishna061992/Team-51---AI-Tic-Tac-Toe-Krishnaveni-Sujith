class Game():
    bd_values = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    def board(self):
        count = 0
        for i in range(3):
            print("|",end = " ")
            for j in range(3):
                print(self.bd_values[i+j+count], "|",end = " "),
            count +=2
            print("\n____________")

    def gameState(self):
        agents = ["Agent1","Agent2"]
        subsequent_value = ' '
        for i in range(9):
            if(i%2==0):
                selectedAgent = Agent1
                subsequent_value = 'X'
            else:
                selectedAgent = Agent2
                subsequent_value ='O'
            print(selectedAgent + " Agent! Placed it's " + subsequent_value + " at:")
            self.board()
            print("\n")
            if subsequent_value == 'X':
                if selectedAgent == "QLearning":
                    idx = self.QLMove(game)
                else:
                    idx = finalMove(game, selectedAgent)
            else:
                if selectedAgent == "QLearning":
                    idx = self.QLMove(game)
                else:
                    idx = finalMove(game, selectedAgent)
            if self.bd_values[idx] == " ":
                self.bd_values[idx] = subsequent_value
                if self.gameOver() == 'X':
                    self.board()
                    print("Fantastic news! We've got a winner. Congratulations! " + Agent1)
                    break
                elif self.gameOver() == 'O':
                    self.board()
                    print("Fantastic news! We've got a winner. Congratulations! "+ Agent2)
                    break
                elif self.gameOver() == 0:
                    self.board()
                    print("Oh no! Regrettably, we do not have a winner.")
                    break
                else:
                    continue

    def placeAgent(self, position, currentAgent):
        player = None
        if(currentAgent == " "):
            self.bd_values[position] = " "
        else:
            if (currentAgent == Agent1):
                player = 'X'
            else:
                player = 'O'
            self.bd_values[position] = player

    def isGameOverTemp(self,memory, currentAgent):
        if(currentAgent == Agent1):
            if self.gameOverTemp(memory) == 'X':
                return 1
            elif self.gameOverTemp(memory) == 'O':
                return -1
            elif self.gameOverTemp(memory) == 0:
                return 0
            else:
                return -10
        elif(currentAgent == Agent2):
            if self.gameOverTemp(memory) == 'X':
                return -1
            elif self.gameOverTemp(memory) == 'O':
                return 1
            elif self.gameOverTemp(memory) == 0:
                return 0
            else:
                return -10


    def gameOverTemp(self, memory):
        if (memory.bd_values[0] == memory.bd_values[1] == memory.bd_values[2] != " "):
            return memory.bd_values[2]
        elif (memory.bd_values[3] == memory.bd_values[4] == memory.bd_values[5] != " "):
            return memory.bd_values[5]
        elif (memory.bd_values[6] == memory.bd_values[7] == memory.bd_values[8] != " "):
            return memory.bd_values[8]
        elif (memory.bd_values[0] == memory.bd_values[3] == memory.bd_values[6] != " "):
            return memory.bd_values[6]
        elif (memory.bd_values[1] == memory.bd_values[4] == memory.bd_values[7] != " "):
            return memory.bd_values[7]
        elif (memory.bd_values[2] == memory.bd_values[5] == memory.bd_values[8] != " "):
            return memory.bd_values[8]
        elif (memory.bd_values[0] == memory.bd_values[4] == memory.bd_values[8] != " "):
            return memory.bd_values[8]
        elif (memory.bd_values[2] == memory.bd_values[4] == memory.bd_values[6] != " "):
            return memory.bd_values[6]
        else:
            for i in range(0,9):
                if(memory.bd_values[i] == " "):
                    return 1
            return 0

    def gameOver(self):
        if (self.bd_values[0] == self.bd_values[1] == self.bd_values[2] != " "):
            return self.bd_values[2]
        elif (self.bd_values[3] == self.bd_values[4] == self.bd_values[5] != " "):
            return self.bd_values[5]
        elif (self.bd_values[6] == self.bd_values[7] == self.bd_values[8] != " "):
            return self.bd_values[8]
        elif (self.bd_values[0] == self.bd_values[3] == self.bd_values[6] != " "):
            return self.bd_values[6]
        elif (self.bd_values[1] == self.bd_values[4] == self.bd_values[7] != " "):
            return self.bd_values[7]
        elif (self.bd_values[2] == self.bd_values[5] == self.bd_values[8] != " "):
            return self.bd_values[8]
        elif (self.bd_values[0] == self.bd_values[4] == self.bd_values[8] != " "):
            return self.bd_values[8]
        elif (self.bd_values[2] == self.bd_values[4] == self.bd_values[6] != " "):
            return self.bd_values[6]
        else:
            flag = False
            for i in range(0,9):
                if(self.bd_values[i] == " "):
                    flag = True
                else:
                    continue
            if(flag==True):
                return 1
            else:
                return 0
    def positionsLeft(self):
        positionLeft = []
        for i in range(len(self.bd_values)):
            if self.bd_values[i] == " ":
                positionLeft.append(int(i))
        return positionLeft

    def minimax(self, memory, currentAgent):
        '''
        
The Minimax algorithm determines the optimal move to achieve victory in the game
        '''
        if memory.isGameOverTemp(memory, currentAgent)== -1 or memory.isGameOverTemp(memory, currentAgent) == 1 or memory.isGameOverTemp(memory, currentAgent) == 0:
            return memory.isGameOverTemp(memory, currentAgent)
        else:
            maxValue = 0
            if currentAgent == "Minimax":
                for move in memory.positionsLeft():
                    memory.placeAgent(move, currentAgent)
                    newValue = self.minimax(memory, getOpponent(currentAgent))
                    memory.placeAgent(move, " ")
                    if (newValue > maxValue):
                        maxValue = newValue
                return maxValue
            else:
                for move in memory.positionsLeft():
                    memory.placeAgent(move, currentAgent)
                    newValue = self.minimax(memory, getOpponent(currentAgent))
                    memory.placeAgent(move, " ")
                    if (newValue < maxValue):
                        maxValue = newValue
                return maxValue

    def alphabeta(self, memory, currentAgent, alpha, beta):
        '''
        The Alpha-Beta Pruning Minimax algorithm is employed to strategically identify the optimal move leading towards securing a win in the game.
        '''
        if memory.isGameOverTemp(memory, currentAgent)== -1 or memory.isGameOverTemp(memory, currentAgent) == 1 or memory.isGameOverTemp(memory, currentAgent) == 0:
            return memory.isGameOverTemp(memory, currentAgent)
        else:
            maxValue = 0
            if currentAgent == "Alphabeta_Minimax":
                for move in memory.positionsLeft():
                    memory.placeAgent(move, currentAgent)
                    newValue = self.alphabeta(memory, getOpponent(currentAgent), alpha, beta)
                    memory.placeAgent(move, " ")
                    if (newValue > maxValue):
                        maxValue = newValue
                    if (maxValue > beta):
                        return maxValue
                    else:
                        alpha = max(alpha, maxValue)
                return maxValue
            else:
                for move in memory.positionsLeft():
                    memory.placeAgent(move, currentAgent)
                    newValue = self.alphabeta(memory, getOpponent(currentAgent), alpha, beta)
                    memory.placeAgent(move, " ")
                    if (newValue < maxValue):
                        maxValue = newValue
                    if (maxValue < alpha):
                        return maxValue
                    else:
                        beta = min(beta, maxValue)
                return maxValue

    def expectimax(self, memory, currentAgent):
        '''
        
The Minimax algorithm facilitates the selection of the most optimal move to advance towards winning the game.
        '''
        if memory.isGameOverTemp(memory, currentAgent)== -1 or memory.isGameOverTemp(memory, currentAgent) == 1 or memory.isGameOverTemp(memory, currentAgent) == 0:
            return memory.isGameOverTemp(memory, currentAgent)
        else:
            maxValue = 0
            if currentAgent == "Expectimax":
                for move in memory.positionsLeft():
                    memory.placeAgent(move, currentAgent)
                    newValue = self.expectimax(memory, getOpponent(currentAgent))
                    memory.placeAgent(move, " ")
                    if (newValue > maxValue):
                        maxValue = newValue
                return maxValue
            else:
                nodes = len(memory.positionsLeft())
                probability = 1/nodes
                expectiValue = 0
                for move in memory.positionsLeft():
                    memory.placeAgent(move, currentAgent)
                    newValue = self.expectimax(memory, getOpponent(currentAgent))
                    memory.placeAgent(move, " ")
                    expectiValue = expectiValue + (newValue * probability)
                return expectiValue

    def qLearning(self, board, QKey):
        """ If there are two consecutive elements, and the third is available, seize the opportunity. """
        # Verify for victories along the diagonal
        diagLeft = [self.bd_values[0], self.bd_values[4], self.bd_values[8]]
        diagRight = [self.bd_values[2], self.bd_values[4], self.bd_values[6]]
        if diagLeft.count(" ") == 1 and diagLeft.count(QKey) == 2:
            idx = diagLeft.index(" ")
            if idx == 0:
                return 0
            elif idx == 1:
                return 4
            else:
                return 8
        elif diagRight.count(" ") == 1 and diagRight.count(QKey) == 2:
            idx = diagRight.index(" ")
            if idx == 0:
                return 2
            elif idx == 1:
                return 4
            else:
                return 6
        for i in range(3):
            count = 0
            rows = [self.bd_values[count], self.bd_values[count+1], self.bd_values[count+2]]
            if rows.count(" ") == 1 and rows.count(QKey) == 2:
                idx = rows.index(" ")
                if idx == 0:
                    return count
                elif idx == 1:
                    return count+1
                else:
                    return count+2
            count = count + 3

        for j in range(3):
            count = 0
            cols = [self.bd_values[count], self.bd_values[count+3], self.bd_values[count+6]]
            if cols.count(" ") == 1 and cols.count(QKey) == 2:
                idx = cols.index(" ")
                if idx == 0:
                    return count
                elif idx == 1:
                    return count+3
                else:
                    return count+6
            count = count + 1
        return None

    def counterMove(self, board, enemyKey):
        """ 
Prevent the opponent from winning by blocking their available victory path. """
        return self.qLearning(board, enemyKey)



    def pickcenter(self, board):
        """ Select the center if it is unoccupied. """
        if self.bd_values[4] == " ":
            return 4
        return None

    def pickcorner(self, board, enemyKey):

        corner = [self.bd_values[0],self.bd_values[2],self.bd_values[6],self.bd_values[8]]
        if corner.count(" ") == 4:
            return random.choice(corner)
        else:
            if self.bd_values[0] == enemyKey and self.bd_values[8] == " ":
                return 8
            elif self.bd_values[2] == enemyKey and self.bd_values[6] == " ":
                return 6
            elif self.bd_values[8] == enemyKey and self.bd_values[0] == " ":
                return 0
            elif self.bd_values[6] == enemyKey and self.bd_values[2] == " ":
                return 2
        return None

    def diamondSide(self, board):
        """ Pick an empty side. """
        diamond = [self.bd_values[1], self.bd_values[3], self.bd_values[5], self.bd_values[7]]
        if diamond.count(" ") == 4:
            return random.choice(diamond)
        else:
            count = 1
            for i in range(0,3):
                if(diamond[i] == " "):
                    return count
                count = count + 2
        return None


    def QLMove(self, board):
        """
        
Specify the instructed action for the Q-Learning agent
        """
        if(Agent1 == "QLearning"):
            QKey = 'X'
            enemyKey = 'O'
        elif(Agent2 == "QLearning"):
            QKey = 'O'
            enemyKey = 'X'
        # Opt for a random selection with a specified probability to introduce variability, preventing a predictable pattern where the teacher consistently emerges victorious.
        if random.random() > 0.9:
            return random.choice(game.positionsLeft())
        # Follow optimal strategy
        if(self.qLearning(board,QKey) != None and self.qLearning(board,QKey) != ' '):
            return self.qLearning(board,QKey)
        elif(self.counterMove(board, enemyKey) != None and self.counterMove(board, enemyKey) != ' '):
            return self.counterMove(board, enemyKey)
        elif(self.pickcenter(board) != None and self.pickcenter(board) != ' '):
            return self.pickcenter(board)
        elif(self.pickcorner(board, enemyKey) != None and self.pickcorner(board, enemyKey) != ' '):
            return self.pickcorner(board, enemyKey)
        elif(self.diamondSide(board) != None and self.diamondSide(board) != ' '):
            return self.diamondSide(board)
        else:
            return random.choice(game.positionsLeft())

def getOpponent(selectedAgent):
    if selectedAgent == Agent1:
        return Agent2
    else:
        return Agent1

def finalMove(game, selectedAgent):
    primeValue = 0
    primeMove = []
    for move in game.positionsLeft():
        game.placeAgent(move, selectedAgent)
        if(selectedAgent == "Minimax"):
            newValue = game.minimax(game, getOpponent(selectedAgent))
        elif(selectedAgent == "Alphabeta_Minimax"):
            newValue = game.alphabeta(game, getOpponent(selectedAgent), -1000, 1000)
        elif(selectedAgent == "Expectimax"):
            newValue = game.expectimax(game, getOpponent(selectedAgent))
        game.placeAgent(move, " ")
        if newValue >= primeValue:
            primeValue = newValue
            primeMove.append(move)
    print("Move",primeMove)
    if(len(primeMove) == 0):
        return random.choice(game.positionsLeft())
    else:
        return random.choice(primeMove)


if __name__ == "__main__":
    import random
    import math
    game = Game()
    game.board()
    print("Please Select Agent1 from following:")
    agentSelection = {1: 'Minimax', 2:'Alphabeta_Minimax', 3:'Expectimax', 4:'QLearning'}
    print(agentSelection)
    Value_1 = int(input("Please Enter your choice of Agent1:"))
    Agent1 = agentSelection.get(Value_1)
    print(Agent1)
    del agentSelection[Value_1]
    print(agentSelection)
    Value_2 = int(input("Please Enter your choice of Agent2:"))
    Agent2 = agentSelection.get(Value_2)
    print(Agent2)
    game.gameState()
