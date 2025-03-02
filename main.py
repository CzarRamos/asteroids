import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

# ============== START OF MAIN ======================== #

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    refresh_timer = pygame.time.Clock()
    dt = 0 # delta time

    # Constructing player groups
    Player.containers = (updateable, drawable)

    # Constructing asteroid groups
    Asteroid.containers = (asteroids_group, updateable, drawable)

    # Asteroid Field
    AsteroidField.containers = (updateable,)
    asteroid_field = AsteroidField()

    Shot.containers = (shots_group, updateable, drawable)

    # Constucting Player
    player_x_init = SCREEN_WIDTH / 2
    player_y_init = SCREEN_HEIGHT / 2
    player = Player(player_x_init, player_y_init)

    # infinite loop unless window is closed
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))

        updateable.update(dt)
        for object in asteroids_group:
            if object.is_colliding(player) == True:
                print("Game over!")
                exit()
            for shot in shots_group:
                if object.is_colliding(shot):
                    shot.kill()
                    object.split()

        for obj in drawable:
            obj.draw(screen)

        # player.update(dt)
        #player.draw(screen)
        pygame.display.flip()

        dt = refresh_timer.tick(60) / 1000

# ============== END OF MAIN ======================== #

if __name__ == "__main__":
    main()