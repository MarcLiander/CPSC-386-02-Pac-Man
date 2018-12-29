import pygame

class Orb():
    def __init__(self, screen, image, x, y):
        self.screen = screen
        self.image = image
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def is_colliding(self, player):
        if player.rect.collidepoint((self.rect.right, self.rect.top)) or player.rect.collidepoint((self.rect.right, self.rect.bottom)) or player.rect.collidepoint((self.rect.left, self.rect.top)) or player.rect.collidepoint((self.rect.left, self.rect.bottom)):
            return True
        return False

    def show_orb(self):
        self.screen.blit(self.image, self.rect)