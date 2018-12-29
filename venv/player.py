import pygame
from imagerect import SpriteSheet

class Player():
    def __init__(self, screen, pacfile):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.sprite = SpriteSheet(pacfile)

        self.index = 0
        self.direction = 0
        self.timer = 0
        self.image = self.sprite.image_get((32 * self.index, 32 * self.direction, 32, 32))
        self.rect = self.image.get_rect()

        self.x_velocity = -2
        self.y_velocity = 0

        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

    def update_player(self, maze):
        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity

        if self.rect.right <= self.screen_rect.left:
            self.rect.left = self.screen_rect.right - 3
        if self.rect.left >= self.screen_rect.right:
            self.rect.right = self.screen_rect.left + 3

        if self.move_right and self.can_move_right(maze):
            self.x_velocity = 2
            self.y_velocity = 0
            self.direction = 2
        if self.move_left and self.can_move_left(maze):
            self.x_velocity = -2
            self.y_velocity = 0
            self.direction = 0
        if self.move_up and self.can_move_up(maze):
            self.x_velocity = 0
            self.y_velocity = -2
            self.direction = 3
        if self.move_down and self.can_move_down(maze):
            self.x_velocity = 0
            self.y_velocity = 2
            self.direction = 1

        if not self.is_colliding(maze):
            if not self.x_velocity is 0 or not self.y_velocity is 0:
                if self.timer < 6:
                    self.timer += 1
                else:
                    self.index += 1
                    if self.index >= 4:
                        self.index = 0
                    self.image = self.sprite.image_get((32 * self.index, 32 * self.direction, 32, 32))
                    self.timer = 0
            else:
                self.index = 0
                self.image = self.sprite.image_get((32 * self.index, 32 * self.direction, 32, 32))
                self.timer = 0

    def show_player(self):
        self.screen.blit(self.image, self.rect)

    def can_move_right(self, maze):
        for brick in maze.bricks:
            if brick.rect.collidepoint((self.rect.right + 1, self.rect.top + 1)) or brick.rect.collidepoint((self.rect.right + 1, self.rect.bottom - 1)):
                return False
        return True

    def can_move_left(self, maze):
        for brick in maze.bricks:
            if brick.rect.collidepoint((self.rect.left - 1, self.rect.top + 1)) or brick.rect.collidepoint((self.rect.left - 1, self.rect.bottom - 1)):
                return False
        return True

    def can_move_up(self, maze):
        for brick in maze.bricks:
            if brick.rect.collidepoint((self.rect.right - 1, self.rect.top - 1)) or brick.rect.collidepoint((self.rect.left + 1, self.rect.top - 1)):
                return False
        return True

    def can_move_down(self, maze):
        for brick in maze.bricks:
            if brick.rect.collidepoint((self.rect.right - 1, self.rect.bottom + 1)) or brick.rect.collidepoint((self.rect.left + 1, self.rect.bottom + 1)):
                return False
        return True

    def is_colliding(self, maze):
        for brick in maze.bricks:
            if brick.rect.collidepoint((self.rect.left + 1, self.rect.bottom - 3)) or brick.rect.collidepoint((self.rect.left + 1, self.rect.top + 2)):
                self.x_velocity = 0
                self.rect.left = brick.rect.right
                return True
            if brick.rect.collidepoint((self.rect.right - 1, self.rect.bottom - 3)) or brick.rect.collidepoint((self.rect.right - 1, self.rect.top + 2)):
                self.x_velocity = 0
                self.rect.right = brick.rect.left
                return True
            if brick.rect.collidepoint((self.rect.left + 2, self.rect.top + 1)) or brick.rect.collidepoint((self.rect.right - 2, self.rect.top + 1)):
                self.y_velocity = 0
                self.rect.top = brick.rect.bottom
                return True
            if brick.rect.collidepoint((self.rect.left + 2, self.rect.bottom - 1)) or brick.rect.collidepoint((self.rect.right - 2, self.rect.bottom - 1)):
                self.y_velocity = 0
                self.rect.bottom = brick.rect.top
                return True
        return False