import pygame
from InputHandler import InputHandler


# Main of the whole AGV Simulator, calls loop declared deeper into Simulation
def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    handler = InputHandler()

    rect = pygame.rect.Rect(640, 360, 60, 60)

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            handler.handle_input(event)

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        color = (255, 0, 0)
        # RENDER YOUR GAME HERE
        pygame.draw.rect(screen, color, rect)
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()

if __name__ == "__main__":
    main()