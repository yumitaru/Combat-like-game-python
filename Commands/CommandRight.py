import pygame

from Commands.Command import Command
from GameActors.GameActor import GameActor


        ##### COMPLETE ROTATE RIGHT FUNC ########
class CommandRight(Command):
    def __init__(self):
        self.key = pygame.K_d
    def execute(self, actor: GameActor, event: pygame.event.Event):
        # self.rotateRight()
        if event.key == self.key:
            print("D")