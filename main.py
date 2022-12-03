from classes import Game, Grid

game = Game()

game.draw()
while True:
    game.move()
    game.draw()
