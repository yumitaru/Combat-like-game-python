import pygame

from Commands.Command import Command
from GameActors.GameActor import GameActor

        ##### COMPLETE FIRE FUNC ########
class CommandFire(Command):
    def __init__(self):
        self.key = pygame.K_SPACE
    def execute(self, actor: GameActor, event: pygame.event.Event):
        # self.fire()
        if event.key == self.key:
            print("Space")