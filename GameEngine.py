import pygame

from InputHandler import InputHandler
from GameActors.Tank import Tank


class GameEngine:
    def __init__(self):
        self.screen = None
        self.clock = None
        self.running = None
        self.inputHandler = None
        self.tank = None
    def initWindow(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.tank = Tank()
    def initHandler(self):
        self.inputHandler = InputHandler()
    def initClock(self):
        self.clock = pygame.time.Clock()
    def initRunning(self):
        self.running = True
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.inputHandler.handle_input(event, self.tank)
    def render(self):
        self.screen.fill("purple")

        self.tank.draw(self.screen)
        # RENDER YOUR GAME HERE
        # pygame.draw.rect(self.screen, color)
        # flip() the display to put your work on screen
        pygame.display.flip()

        # self.clock.tick(60)  # limits FPS to 60
    def quit(self):
        pygame.quit()
    def run(self):
        while self.running:
            self.update()
            self.render()
        self.quit()
