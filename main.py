from decouple import config
from player import Player
from game import Game

#my_money = config("MY_MONEY", cast=int)
my_money = 1000
player = Player(my_money)
game = Game(30, 2)
game.play(player)
