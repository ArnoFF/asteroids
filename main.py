import pygame
from constants import *
from player import Player

def main():
    # print starting message
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    # initialize pygame
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0

    # instantiate Player
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # game loop start
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)
        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
