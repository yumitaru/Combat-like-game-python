import pygame

from Commands.Command import Command
from GameActors.GameActor import GameActor

        ##### COMPLETE GO BACKWARDS FUNC ########
class CommandBackward(Command):
    def __init__(self):
        self.key = pygame.K_s

    def execute(self, actor: GameActor, event: pygame.event.Event):
        # self.goBackward()
        if event.key == self.key:
            print("S")