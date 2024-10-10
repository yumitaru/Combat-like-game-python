import pygame

from Commands.Command import Command
from GameActors.GameActor import GameActor

        ##### COMPLETE ROTATE LEFT FUNC ########
class CommandLeft(Command):
    def __init__(self):
        self.key = pygame.K_a
    def execute(self, actor: GameActor, event: pygame.event.Event):
        # self.rotateLeft()
        if event.key == self.key:
            print("A")