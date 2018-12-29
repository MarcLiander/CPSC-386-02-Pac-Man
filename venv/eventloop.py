import pygame
import sys


class EventLoop:
    def __init__(self, finished):
        self.finished = finished

    def check_events(self, maze):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event, maze)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event, maze)

    def check_keydown_events(self, event, maze):
        for player in maze.players:
            if event.key == pygame.K_RIGHT:
                player.move_right = True
                player.move_left = False
                player.move_up = False
                player.move_down = False
            if event.key == pygame.K_LEFT:
                player.move_right = False
                player.move_left = True
                player.move_up = False
                player.move_down = False
            if event.key == pygame.K_UP:
                player.move_right = False
                player.move_left = False
                player.move_up = True
                player.move_down = False
            if event.key == pygame.K_DOWN:
                player.move_right = False
                player.move_left = False
                player.move_up = False
                player.move_down = True
        if event.key == pygame.K_q:
            sys.exit()

    def check_keyup_events(self, event, maze):
        for player in maze.players:
            if event.key == pygame.K_RIGHT:
                player.move_right = False
            if event.key == pygame.K_LEFT:
               player.move_left = False
            if event.key == pygame.K_UP:
                player.move_up = False
            if event.key == pygame.K_DOWN:
                player.move_down = False
