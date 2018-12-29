import pygame

class Brick():
    def __init__(self, screen, image, x, y):
        self.screen = screen
        self.image = image
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def show_brick(self):
        self.screen.blit(self.image, self.rect)