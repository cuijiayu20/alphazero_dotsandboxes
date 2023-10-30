# import Arena
# from MCTS import MCTS
# from othello.OthelloGame import OthelloGame
# from othello.OthelloPlayers import *
# from othello.pytorch.NNet import NNetWrapper as NNet
#
#
# import numpy as np
# from utils import *
#
# """
# use this script to play any two agents against each other, or play manually with
# any agent.
# """
#
# mini_othello = False  # Play in 6x6 instead of the normal 8x8.
# human_vs_cpu = True
#
# if mini_othello:
#     g = OthelloGame(6)
# else:
#     g = OthelloGame(8)
#
# # all players
# rp = RandomPlayer(g).play
# gp = GreedyOthelloPlayer(g).play
# hp = HumanOthelloPlayer(g).play
#
#
#
# # nnet players
# n1 = NNet(g)
# if mini_othello:
#     n1.load_checkpoint('./pretrained_models/othello/pytorch/','6x100x25_best.pth.tar')
# else:
#     n1.load_checkpoint('./pretrained_models/othello/pytorch/','8x8_100checkpoints_best.pth.tar')
# args1 = dotdict({'numMCTSSims': 50, 'cpuct':1.0})
# mcts1 = MCTS(g, n1, args1)
# n1p = lambda x: np.argmax(mcts1.getActionProb(x, temp=0))
#
# if human_vs_cpu:
#     player2 = hp
# else:
#     n2 = NNet(g)
#     n2.load_checkpoint('./pretrained_models/othello/pytorch/', '8x8_100checkpoints_best.pth.tar')
#     args2 = dotdict({'numMCTSSims': 50, 'cpuct': 1.0})
#     mcts2 = MCTS(g, n2, args2)
#     n2p = lambda x: np.argmax(mcts2.getActionProb(x, temp=0))
#
#     player2 = n2p  # Player 2 is neural network if it's cpu vs cpu.
#
# arena = Arena.Arena(n1p, player2, g, display=OthelloGame.display)
#
# print(arena.playGames(2, verbose=True))




import os
import numpy as np

import Arena
from MCTS import MCTS
from dotsandboxes.DotsAndBoxesGame import DotsAndBoxesGame
from dotsandboxes.DotsAndBoxesPlayers import HumanDotsAndBoxesPlayer, RandomPlayer, GreedyRandomPlayer
from dotsandboxes.Keras.NNet import NNetWrapper

from utils import dotdict

game = DotsAndBoxesGame(n=3)
hp1 = HumanDotsAndBoxesPlayer(game).play
hp2 = HumanDotsAndBoxesPlayer(game).play

rp1 = RandomPlayer(game).play
rp2 = RandomPlayer(game).play
grp1 = GreedyRandomPlayer(game).play
grp2 = GreedyRandomPlayer(game).play
numMCTSSims = 50

nnet1 = NNetWrapper(game)
nnet1.load_checkpoint(os.path.join('pretrained_models', 'dotsandboxes', 'keras', '3x3'), 'best.pth.tar')
args1 = dotdict({'numMCTSSims': numMCTSSims, 'cpuct': 1.0})
mcts1 = MCTS(game, nnet1, args1)
alphazero1 = lambda x: np.argmax(mcts1.getActionProb(x, temp=0))
nnet2 = NNetWrapper(game)
nnet2.load_checkpoint(os.path.join('pretrained_models', 'dotsandboxes', 'keras', '3x3'), 'best.pth.tar')
args2 = dotdict({'numMCTSSims': numMCTSSims, 'cpuct': 1.0})
mcts2 = MCTS(game, nnet2, args2)
alphazero2 = lambda x: np.argmax(mcts2.getActionProb(x, temp=0))


# Play Random vs Greedy Random
player1 = rp1
player2 = grp2
arena = Arena.Arena(player1, player2, game, display=DotsAndBoxesGame.display)
oneWon, twoWon, draws = arena.playGames(100, verbose=False)
print("\nRandom won {} games, Greedy Random won {} games".format(oneWon, twoWon))

