# to run source venv/bin/activate & export DISPLAY=localhost:0 & and use xlaunch desktop icon 

import pygame
from constants import *
from player import *


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updateable_group = pygame.sprite.Group()
    drawn_group = pygame.sprite.Group()
    Player.containers = (drawn_group, updateable_group)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    while True:
        for event in pygame.event.get(): #this checks if the user has exited the program and closes if they have
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        updateable_group.update(dt)
        for object in drawn_group:
            object.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()