import pygame
from pygame.locals import *

import sys

RESOLUTION = (400, 300)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


class Ball:
    def __init__(self, col=BLACK, xPos=RESOLUTION[0] / 2, yPos=RESOLUTION[1] / 2, xVel=1, yVel=1, rad=15):
        self.color = col
        self.x = xPos
        self.y = yPos
        self.dx = xVel
        self.dy = yVel
        self.radius = rad
        self.type = "ball"

    def draw(self, surface):
        # needed to make int() conversion into tuple
        pygame.draw.circle(
            surface, self.color, (int(self.x), int(self.y)), self.radius)

    def update(self):
        # Make the object move
        self.x += self.dx
        self.y += self.dy

        # Keep the ball on the screen.
        if (self.x <= 0 or self.x >= RESOLUTION[0]):
            self.dx *= -1
        if (self.y <= 0 or self.y >= RESOLUTION[1]):
            self.dy *= -1


class Player:
    """Player as a circle that is controlled by the mouse."""

    def __init__(self, rad=20):
        self.x = 0
        self.y = 0
        self.radius = rad

    def draw(self, surface):
        pygame.draw.circle(
            surface, RED, (int(self.x), int(self.y)), self.radius)

    def update(self):
        # In every frame, check the location of the mouse
        # and set the players' objects’ location to that point.
        cord = pygame.mouse.get_pos()
        self.x = cord[0]
        self.y = cord[1]


class Game:
    """Make the game loop into a class."""

    def __init__(self):
        # Pygame needs to be initialized to use
        # certain features like text or sound.
        pygame.init()
        self.screen = pygame.display.set_mode(RESOLUTION)
        self.clock = pygame.time.Clock()
        self.gameObjects = []
        self.gameObjects.append(Ball(GREEN))
        self.gameObjects.append(Ball(BLACK,100))
        # Create a new player instance and add it to the list.
        self.gameObjects.append(Player())

    def handleEvents(self):
        # Handle events in a function.
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                # call sys.exit() after pygame.quit() to stop the program
                # so you can not change the surface after you have quit
                # pygame and not get the error
                sys.exit()

    def run(self):
        # Make the game loop a function.
        while True:
            # Call the event handling function every loop.
            self.handleEvents()
            
            # update all objects in the array every loop.
            for gameObj in self.gameObjects:
                gameObj.update()

            # Color the screen.
            self.screen.fill(WHITE)

            # draw all objects in the array every loop.
            for gameObj in self.gameObjects:
                gameObj.draw(self.screen)

            # Use Pygame’s clock to limit the frame rate to 60 fps.
            self.clock.tick(60)

            # Display the screen.
            pygame.display.flip()


Game().run()
