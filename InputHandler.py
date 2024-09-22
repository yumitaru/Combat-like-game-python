import pygame

from Commands.CommandBackward import CommandBackward
from Commands.CommandFire import CommandFire
from Commands.CommandForward import CommandForward
from Commands.CommandLeft import CommandLeft
from Commands.CommandRight import CommandRight


class InputHandler:
    def __init__(self):
        self.buttonW_ = CommandForward
        self.buttonA_ = CommandLeft
        self.buttonS_ = CommandBackward
        self.buttonD_ = CommandRight
        self.buttonSpace_ = CommandFire

    def handle_input(self, event: pygame.event.Event):


        ####### ADD EXECUTE TO KEYS########
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                #self.buttonW_.execute()
                print("w")
            elif event.key == pygame.K_a:
                #self.buttonA_.execute()
                print("a")
            elif event.key == pygame.K_s:
                #self.buttonS_.execute()
                print("s")
            elif event.key == pygame.K_d:
                #self.buttonD_.execute()
                print("d")
            elif event.key == pygame.K_SPACE:
                #self.buttonSpace_.execute()
                print("space")