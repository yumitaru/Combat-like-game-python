import pygame
from GameActors.GameActor import GameActor


class Tank(GameActor):
    def __init__(self):
        self.color = (255, 0, 0)
        self.width = 60
        self.height = 60
        self.positionX = 640
        self.positionY = 360
        self.rect = pygame.rect.Rect(self.positionX, self.positionY, 60, 60)
        self.buttonSpace_ = None
    def draw(self, screen: pygame.display):
        pygame.draw.rect(screen, self.color, self.rect, 0)
    def move(self):
        self.rect.move_ip(10,10)