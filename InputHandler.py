import pygame

from Commands.CommandBackward import CommandBackward
from Commands.CommandFire import CommandFire
from Commands.CommandForward import CommandForward
from Commands.CommandLeft import CommandLeft
from Commands.CommandRight import CommandRight
from GameActors.GameActor import GameActor


class InputHandler:
    def __init__(self):
        self.forward = CommandForward()
        self.left = CommandLeft()
        self.backward = CommandBackward()
        self.right = CommandRight()
        self.fire = CommandFire()

    def handle_input(self, event: pygame.event.Event, actor: GameActor):
        ####### ADD EXECUTE TO KEYS########
        if event.type == pygame.KEYDOWN:
            self.forward.execute(actor, event)
            self.left.execute(actor, event)
            self.backward.execute(actor, event)
            self.right.execute(actor, event)
            self.fire.execute(actor, event)
