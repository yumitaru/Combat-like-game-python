from GameActors.GameActor import GameActor

class Command:
    def execute(self, actor: GameActor):
        raise NotImplementedError("Subclasses should implement this method.")