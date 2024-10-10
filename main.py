import pygame

from GameEngine import GameEngine
from InputHandler import InputHandler


# Main of the whole AGV Simulator, calls loop declared deeper into Simulation
def main():
    # pygame setup
    engine = GameEngine()
    engine.initWindow()
    engine.initClock()
    engine.initRunning()
    engine.initHandler()

    engine.run()


if __name__ == "__main__":
    main()