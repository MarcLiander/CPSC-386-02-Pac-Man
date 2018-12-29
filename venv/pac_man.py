import pygame
from maze import Maze
from eventloop import EventLoop


class Game:
    BLACK = 0, 0, 0

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((896, 992))
        pygame.display.set_caption("Hello")

        self.maze = Maze(self.screen, mazefile='Levels/text_maze.txt', brickfile='Images/square.png', orbfile='Images/orb.png', pacfile='Images/pac_man.png', ghostfile='Images/ghost.png')
        self.clock = pygame.time.Clock()

    def play(self):
        eloop = EventLoop(finished=False)

        while not eloop.finished:
            while not self.maze.beaten:
                eloop.check_events(self.maze)
                self.update_screen()
                self.clock.tick(60)
            self.maze.beaten = False
            self.maze.countdown = 0
            self.maze.reset = False
            self.maze.player_hit = False
            self.maze.build()

    def update_screen(self):
        self.screen.fill(Game.BLACK)
        self.maze.update_maze()
        pygame.display.flip()


game = Game()
game.play()