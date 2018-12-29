import pygame
from imagerect import SpriteSheet
from brick import Brick
from orb import Orb
from player import Player
from ghost import Ghost


class Maze:
    RED = 255, 0, 0
    BRICK_SIZE = 32

    def __init__(self, screen, mazefile, brickfile, orbfile, pacfile, ghostfile):
        self.screen = screen
        self.filename = mazefile
        with open(self.filename, 'r') as f:
            self.rows = f.readlines()

        self.wall = SpriteSheet(brickfile)
        self.individual_orb = SpriteSheet(orbfile)
        self.pacfile = pacfile
        self.ghostfile = ghostfile

        self.bricks = []
        self.orbs = []
        self.players = []
        self.ghosts = []
        self.sz = 32

        self.beaten = False
        self.reset= False
        self.player_hit = False
        self.countdown = 0

        self.build()

    def build(self):
        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                if col == 'a':
                    self.bricks.append(Brick(self.screen, self.wall.image_get((0, self.sz * 0, self.sz, self.sz)), ncol * self.sz, nrow * self.sz))
                elif col == 'b':
                    self.bricks.append(Brick(self.screen, self.wall.image_get((0, self.sz * 1, self.sz, self.sz)), ncol * self.sz, nrow * self.sz))
                elif col == 'c':
                    self.bricks.append(Brick(self.screen, self.wall.image_get((0, self.sz * 2, self.sz, self.sz)), ncol * self.sz, nrow * self.sz))
                elif col == 'd':
                    self.bricks.append(Brick(self.screen, self.wall.image_get((0, self.sz * 3, self.sz, self.sz)), ncol * self.sz, nrow * self.sz))
                elif col == 'e':
                    self.bricks.append(Brick(self.screen, self.wall.image_get((0, self.sz * 4, self.sz, self.sz)), ncol * self.sz, nrow * self.sz))
                elif col == 'f':
                    self.bricks.append(Brick(self.screen, self.wall.image_get((0, self.sz * 5, self.sz, self.sz)), ncol * self.sz, nrow * self.sz))
                elif col == 'g':
                    self.bricks.append(Brick(self.screen, self.wall.image_get((0, self.sz * 6, self.sz, self.sz)), ncol * self.sz, nrow * self.sz))
                elif col == 'h':
                    self.bricks.append(Brick(self.screen, self.wall.image_get((0, self.sz * 7, self.sz, self.sz)), ncol * self.sz, nrow * self.sz))
                elif col == 'i':
                    self.bricks.append(Brick(self.screen, self.wall.image_get((0, self.sz * 8, self.sz, self.sz)), ncol * self.sz, nrow * self.sz))
                elif col == 'j':
                    self.bricks.append(Brick(self.screen, self.wall.image_get((0, self.sz * 9, self.sz, self.sz)), ncol * self.sz, nrow * self.sz))
                elif col == 'k':
                    self.bricks.append(Brick(self.screen, self.wall.image_get((0, self.sz * 10, self.sz, self.sz)), ncol * self.sz, nrow * self.sz))
                elif col == 'l':
                    self.bricks.append(Brick(self.screen, self.wall.image_get((0, self.sz * 11, self.sz, self.sz)), ncol * self.sz, nrow * self.sz))
                elif col == 'm':
                    self.bricks.append(Brick(self.screen, self.wall.image_get((0, self.sz * 12, self.sz, self.sz)), ncol * self.sz, nrow * self.sz))
                elif col == 'n':
                    self.bricks.append(Brick(self.screen, self.wall.image_get((0, self.sz * 13, self.sz, self.sz)), ncol * self.sz, nrow * self.sz))
                elif col == 'o':
                    self.bricks.append(Brick(self.screen, self.wall.image_get((0, self.sz * 14, self.sz, self.sz)), ncol * self.sz, nrow * self.sz))
                elif col == 'p':
                    self.bricks.append(Brick(self.screen, self.wall.image_get((0, self.sz * 15, self.sz, self.sz)), ncol * self.sz, nrow * self.sz))
                elif col == 'q':
                    self.bricks.append(Brick(self.screen, self.wall.image_get((0, self.sz * 16, self.sz, self.sz)), ncol * self.sz, nrow * self.sz))
                elif col == 'r':
                    self.bricks.append(Brick(self.screen, self.wall.image_get((0, self.sz * 17, self.sz, self.sz)), ncol * self.sz, nrow * self.sz))
                elif col == 's':
                    self.bricks.append(Brick(self.screen, self.wall.image_get((0, self.sz * 18, self.sz, self.sz)), ncol * self.sz, nrow * self.sz))
                elif col == 'u':
                    self.bricks.append(Brick(self.screen, self.wall.image_get((0, self.sz * 19, self.sz, self.sz)), ncol * self.sz, nrow * self.sz))
                elif col == 'v':
                    self.bricks.append(Brick(self.screen, self.wall.image_get((0, self.sz * 20, self.sz, self.sz)), ncol * self.sz, nrow * self.sz))
                elif col == 'w':
                    self.bricks.append(Brick(self.screen, self.wall.image_get((0, self.sz * 21, self.sz, self.sz)), ncol * self.sz, nrow * self.sz))
                elif col == 'x':
                    self.bricks.append(Brick(self.screen, self.wall.image_get((0, self.sz * 22, self.sz, self.sz)), ncol * self.sz, nrow * self.sz))
                elif col == 'y':
                    self.bricks.append(Brick(self.screen, self.wall.image_get((0, self.sz * 23, self.sz, self.sz)), ncol * self.sz, nrow * self.sz))
                elif col == 'z':
                    self.bricks.append(Brick(self.screen, self.wall.image_get((0, self.sz * 24, self.sz, self.sz)), ncol * self.sz, nrow * self.sz))
                elif col == 't':
                    self.bricks.append(Brick(self.screen, self.wall.image_get((0, self.sz * 25, self.sz, self.sz)), ncol * self.sz, nrow * self.sz))
                elif col == ';' or col == '.':
                    self.orbs.append(Orb(self.screen, self.individual_orb.image_get((0, 0, 8, 8)), ncol * self.sz + 12, nrow * self.sz + 12))
                elif col == '@':
                    self.players.append(Player(self.screen, self.pacfile))
                    for player in self.players:
                        player.rect.x = ncol * self.sz + 16
                        player.rect.y = nrow * self.sz
                elif col == '!':
                    self.ghosts.append(Ghost(self.screen, self.ghostfile, ncol * self.sz, nrow * self.sz))

    def update_maze(self):
        for player in self.players:
            player.update_player(self)
            for ghost in self.ghosts:
                ghost.update_ghost(player, self)
        for orb in self.orbs:
            for player in self.players:
                if orb.is_colliding(player):
                    self.orbs.remove(orb)
        self.show_maze()
        if len(self.orbs) <= 0 or self.player_hit:
            self.reset = True
            self.ghosts.clear()
            self.players.clear()
        if self.reset:
            self.countdown += 1
        if self.countdown >= 120:
            self.beaten = True
            self.orbs.clear()
            self.bricks.clear()

    def show_maze(self):
        for brick in self.bricks:
            brick.show_brick()
        for orb in self.orbs:
            orb.show_orb()
        for player in self.players:
            player.show_player()
        for ghost in self.ghosts:
            ghost.show_ghost()