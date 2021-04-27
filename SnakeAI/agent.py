import torch
import random
import numpy as np
from snake_game import SnakeGame, Direction, Point
from collections import deque
from model import LinearQNet, QTrainer
from helper import plot

MAX_MEMORY = 100_000
BATCH = 1000
LR = 0.001

class Agent:

    def __init__(self):
        self.nGames = 0
        self.epsilon = 0
        self.gamma = 0.9    
        self.memory = deque(maxlen=MAX_MEMORY)
        self.model = LinearQNet(11, 256, 3)
        self.trainer = QTrainer(self.model, lr=LR, gamma=self.gamma)

    def getState(self, game):
        head = game.snake[0]
        point_l = Point(head.x - 20, head.y)
        point_r = Point(head.x + 20, head.y)
        point_u = Point(head.x, head.y - 20)
        point_d = Point(head.x, head.y + 20)
        
        dir_l = game.direction == Direction.LEFT
        dir_r = game.direction == Direction.RIGHT
        dir_u = game.direction == Direction.UP
        dir_d = game.direction == Direction.DOWN

        state = [
            # Danger straight
            (dir_r and game.is_collision(point_r)) or 
            (dir_l and game.is_collision(point_l)) or 
            (dir_u and game.is_collision(point_u)) or 
            (dir_d and game.is_collision(point_d)),

            # Danger right
            (dir_u and game.is_collision(point_r)) or 
            (dir_d and game.is_collision(point_l)) or 
            (dir_l and game.is_collision(point_u)) or 
            (dir_r and game.is_collision(point_d)),

            # Danger left
            (dir_d and game.is_collision(point_r)) or 
            (dir_u and game.is_collision(point_l)) or 
            (dir_r and game.is_collision(point_u)) or 
            (dir_l and game.is_collision(point_d)),
            
            # Move direction
            dir_l,
            dir_r,
            dir_u,
            dir_d,
            
            # Food location 
            game.food.x < game.head.x,  # food left
            game.food.x > game.head.x,  # food right
            game.food.y < game.head.y,  # food up
            game.food.y > game.head.y  # food down
            ]

        return np.array(state, dtype=int)



    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def trainLong(self):
        if len(self.memory) > BATCH:
            miniSample = random.sample(self.memory, BATCH)
        else:
            miniSample = self.memory
        
        states, actions, rewards, next_states, dones = zip(*miniSample)
        self.trainer.trainStep(states, actions, rewards, next_states, dones)

    
    def trainShort(self, state, action, reward, next_state, done):
        self.trainer.trainStep(state, action, reward, next_state, done)

    def getAction(self, state):
        self.epsilon = 80 - self.nGames
        finalMove = [0, 0, 0]
        if random.randint(0, 200) < self.epsilon:
            move = random.randint(0, 2)
            finalMove[move] = 1
        else:
            state0 = torch.tensor(state, dtype=torch.float)
            prediction = self.model(state0)
            move = torch.argmax(prediction).item()
            finalMove[move] = 1
        return finalMove

def Train():
    plotScores = []
    plotMeanScored = []
    totalScore = 0
    record = 0
    agent = Agent()
    game = SnakeGame()
    while True:
        stateOld = agent.getState(game)
        finalMove = agent.getAction(stateOld)
        reward, done, score = game.play_step(finalMove)
        stateNew = agent.getState(game)
        agent.trainShort(stateOld, finalMove, reward, stateNew, done)
        agent.remember(stateOld, finalMove, reward, stateNew, done)

        if done:
            game.reset()
            agent.nGames += 1
            agent.trainLong()

            if score > record:
                record = score
                agent.model.save()
            
            print('Game', agent.nGames, 'Score', score, 'Record', record)

            plotScores.append(score)
            totalScore += score
            meanScore = totalScore / agent.nGames
            plotMeanScored.append(meanScore)
            plot(plotScores, plotMeanScored)

if __name__ == '__main__':
    Train()