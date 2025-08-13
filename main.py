#Players enter their name and choose their color
from Othello_engine import Othello
from color import Color
from Players import Player


game= Othello()
while True:
    game.player_turns(Color.BLACK)
    game.playerb.placepawn(game.board)
    game.player_turns(Color.WHITE)
    game.playerw.placepawn(game.board)

print(game.playerb.name)

 