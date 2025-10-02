import pygame
from constants import *
from player import Player

def main():
    # Game initilization
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    # Game Loop
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Update game state
        updatable.update(dt)

        screen.fill("black")
        
        # Draw Game objects
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        # Frame Rate: 60
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
