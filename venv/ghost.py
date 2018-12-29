import pygame
from imagerect import SpriteSheet

class Ghost():
    def __init__(self, screen, ghostfile, x, y):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.sprite = SpriteSheet(ghostfile)

        self.index = 0
        self.timer = 0
        self.image = self.sprite.image_get((32 * self.index, 0, 32, 32))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.x_velocity = 0
        self.y_velocity = 0

    def update_ghost(self, player, maze):
        self.is_colliding(maze)
        self.collide_player(player, maze)

        if (self.x_velocity is 0 and self.y_velocity is 0) or (self.check_junction(maze)):
            if abs(player.rect.centerx - self.rect.centerx) <= abs(player.rect.centery - self.rect.centery) and player.rect.centerx - self.rect.centerx != 0:
                if player.rect.centerx - self.rect.centerx > 0:
                    if self.can_move_right(maze):
                        self.x_velocity = 2
                        self.y_velocity = 0
                    elif self.can_move_up(maze):
                        self.y_velocity = -2
                        self.x_velocity = 0
                    elif self.can_move_down(maze):
                        self.y_velocity = 2
                        self.x_velocity = 0
                    elif self.can_move_left(maze):
                        self.x_velocity = -2
                        self.y_velocity = 0
                else:
                    if self.can_move_left(maze):
                        self.x_velocity = -2
                        self.y_velocity = 0
                    elif self.can_move_up(maze):
                        self.y_velocity = -2
                        self.x_velocity = 0
                    elif self.can_move_down(maze):
                        self.y_velocity = 2
                        self.x_velocity = 0
                    elif self.can_move_right(maze):
                        self.x_velocity = 2
                        self.y_velocity = 0
            else:
                if player.rect.centery - self.rect.centery < 0:
                    if self.can_move_up(maze):
                        self.y_velocity = -2
                        self.x_velocity = 0
                    elif self.can_move_right(maze):
                        self.x_velocity = 2
                        self.y_velocity = 0
                    elif self.can_move_left(maze):
                        self.x_velocity = -2
                        self.y_velocity = 0
                    elif self.can_move_down(maze):
                        self.y_velocity = 2
                        self.x_velocity = 0
                elif player.rect.centery - self.rect.centery == 0:
                    if player.rect.centerx - self.rect.centerx >= 0:
                        if self.can_move_right(maze):
                            self.x_velocity = 2
                            self.y_velocity = 0
                        elif self.can_move_up(maze):
                            self.y_velocity = -2
                            self.x_velocity = 0
                        elif self.can_move_down(maze):
                            self.y_velocity = 2
                            self.x_velocity = 0
                        elif self.can_move_left(maze):
                            self.x_velocity = -2
                            self.y_velocity = 0
                    else:
                        if self.can_move_left(maze):
                            self.x_velocity = -2
                            self.y_velocity = 0
                        elif self.can_move_up(maze):
                            self.y_velocity = -2
                            self.x_velocity = 0
                        elif self.can_move_down(maze):
                            self.y_velocity = 2
                            self.x_velocity = 0
                        elif self.can_move_right(maze):
                            self.x_velocity = 2
                            self.y_velocity = 0
                else:
                    if self.can_move_down(maze):
                        self.y_velocity = 2
                        self.x_velocity = 0
                    elif self.can_move_right(maze):
                        self.x_velocity = 2
                        self.y_velocity = 0
                    elif self.can_move_left(maze):
                        self.x_velocity = -2
                        self.y_velocity = 0
                    elif self.can_move_up(maze):
                        self.y_velocity = -2
                        self.x_velocity = 0

        if self.rect.right <= self.screen_rect.left:
            self.rect.left = self.screen_rect.right - 6
        if self.rect.left >= self.screen_rect.right:
            self.rect.right = self.screen_rect.left + 6

        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity

        if self.timer < 6:
            self.timer += 1
        else:
            self.index += 1
            if self.index >= 8:
                self.index = 0
            self.image = self.sprite.image_get((32 * self.index, 0, 32, 32))
            self.timer = 0

    def show_ghost(self):
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

    def check_junction(self, maze):
        if self.can_move_up(maze) and self.can_move_down(maze) and self.can_move_right(maze):
            return True
        elif self.can_move_up(maze) and self.can_move_down(maze) and self.can_move_left(maze):
            return True
        elif self.can_move_right(maze) and self.can_move_down(maze) and self.can_move_left(maze):
            return True
        elif self.can_move_right(maze) and self.can_move_up(maze) and self.can_move_left(maze):
            return True
        else:
            return False

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

    def collide_player(self, player, maze):
        if player.rect.collidepoint((self.rect.right, self.rect.top)) or player.rect.collidepoint((self.rect.right, self.rect.bottom)) or player.rect.collidepoint((self.rect.left, self.rect.top)) or player.rect.collidepoint((self.rect.left, self.rect.bottom)):
            maze.player_hit = True