import threading

import numpy as np
import dotsandboxes.gui.global_var
from Arena import Arena
#from dotsandboxes.gui.main import GUI
import time

from dotsandboxes.gui import global_var


class RandomPlayer:
    def __init__(self, game):
        self.game = game

    def play(self, board):
        a = np.random.randint(self.game.getActionSize())
        valids = self.game.getValidMoves(board, 1)
        while valids[a]!=1:
            a = np.random.randint(self.game.getActionSize())
        return a


# Will play at random, unless there's a chance to score a square
class GreedyRandomPlayer:
    def __init__(self, game):
        self.game = game

    def play(self, board):
        valids = self.game.getValidMoves(board, 1)
        previous_score = board[0, -1]
        for action in np.nonzero(valids)[0]:
            new_board, _ = self.game.getNextState(board, 1, action)
            new_score = new_board[0, -1]
            if new_score > previous_score:
                return action
        a = np.random.randint(self.game.getActionSize())
        while valids[a]!=1:
            a = np.random.randint(self.game.getActionSize())
        return a

#
# class HumanDotsAndBoxesPlayer:
#     def __init__(self, game):
#         self.game = game
#
#     def play(self, board):
#         if board[2][-1] == 1:
#             # We have to pass
#             return self.game.getActionSize() - 1
#         valids = self.game.getValidMoves(board, 1)
#         while True:
#             print("Valid moves: {}".format(np.where(valids == True)[0]))
#             #a = int(input())
#             try:
#                 while not GUI.edge_number:  # Wait until GUI.edge_number is updated
#                     time.sleep(0.1)  # Wait for 100 milliseconds
#                 a = GUI.edge_number[-1]
#                 print("a:"+str(a))
#                 if valids[a]:
#                     return a
#             except ValueError:
#                 print("Invalid input. Please enter an integer.")

class HumanDotsAndBoxesPlayer:
    def __init__(self, game):
        self.game = game

    def play(self, board):
        if board[2][-1] == 1:
            # We have to pass
            return self.game.getActionSize() - 1
        valids = self.game.getValidMoves(board, 1)
        # event = threading.Event()  # Create a new event
        # t = threading.Thread(target=GUI.create_board, args=(Arena.action_copy[-1], event))
        # t.start()
        # event.wait()  # Wait for the event to be set

        while True:
            #print("Valid moves: {}".format(np.where(valids == True)[0]))
            try:
                while not global_var.edge_number:  # Wait until GUI.edge_number is updated
                    time.sleep(0.1)  # Wait for 100 milliseconds
                a = global_var.edge_number[-1]
                #print("a:"+str(a))
                if valids[a]:
                    return a
            except ValueError:
                pass
                #print("Invalid input. Please enter an integer.")
