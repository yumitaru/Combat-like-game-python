import pygame

from GameActors.GameActor import GameActor

class Command:
    def execute(self, actor: GameActor, event: pygame.event.Event):
        raise NotImplementedError("Subclasses should implement this method.")