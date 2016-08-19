# Import files
try:
    import sys
    import pygame

    import constants
    import world

except ImportError, _err:
    print("couldn't load module. {0}".format(_err))
    sys.exit() 

def main():
    # Initialise Pygame
    pygame.init()

    screen_size = (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption(constants.WIN_CAPTION)

    FPSCLOCK = pygame.time.Clock()

    game_world = world.World()

    game_running = True
    while game_running:
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                game_running = False
 
            if event.type == pygame.KEYDOWN:
                # Quit Game
                if event.key == pygame.K_ESCAPE:
                    game_running = False

        game_world.update()

        # Draw
        game_world.draw()
        FPSCLOCK.tick(constants.FPS)
        pygame.display.update()

    # quit safely
    #game_world.save_game()
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()