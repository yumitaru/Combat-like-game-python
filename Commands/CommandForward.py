import pygame

from Commands.Command import Command
from GameActors.GameActor import GameActor

        ##### COMPLETE GO FORWARD FUNC ########
class CommandForward(Command):
    def __init__(self):
        self.key = pygame.K_w
    def execute(self, actor: GameActor, event: pygame.event.Event):
        # self.goForward()
        if event.key == self.key:
            print("W")
            actor.move()