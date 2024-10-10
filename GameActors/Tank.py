import pygame
from GameActor import GameActor


class Tank(GameActor):
    def __init__(self):
        self.color = (255, 0, 0)
        self.width = 60
        self.height = 60
        self.position = float(640, 360)
        self.rect = pygame.rect.Rect(640, 360, 60, 60)
        self.buttonSpace_ = None