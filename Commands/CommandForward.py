from Commands.Command import Command
from GameActors.GameActor import GameActor

        ##### COMPLETE GO FORWARD FUNC ########
class CommandForward(Command):
    def execute(self, actor: GameActor):
        # self.goForward()
        print("W")