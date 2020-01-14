import pygame
from pygame.locals import *

import sys

resolution = (400, 300)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)


class Ball:
    def __init__(self, xPos=resolution[0] / 2, yPos=resolution[1] / 2, xVel=1, yVel=1, rad=15):
        self.x = xPos
        self.y = yPos
        self.dx = xVel
        self.dy = yVel
        self.radius = rad
        self.type = "ball"

    def draw(self, surface):
        # needed to make int() conversion into tuple
        pygame.draw.circle(
            surface, black, (int(self.x), int(self.y)), self.radius)

    def update(self):
        # Make the object move
        self.x += self.dx
        self.y += self.dy

        # Keep the ball on the screen.
        if (self.x <= 0 or self.x >= resolution[0]):
            self.dx *= -1
        if (self.y <= 0 or self.y >= resolution[1]):
            self.dy *= -1


# Make the game loop into a class
class Game:
    def __init__(self):
        # Pygame needs to be initialized to use
        # certain features like text or sound.
        pygame.init()
        self.screen = pygame.display.set_mode(resolution)
        self.clock = pygame.time.Clock()
        self.gameObjects = []
        self.gameObjects.append(Ball())
        self.gameObjects.append(Ball(100))

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
            self.screen.fill(white)

            # draw all objects in the array every loop.
            for gameObj in self.gameObjects:
                gameObj.draw(self.screen)

            # Use Pygame’s clock to limit the frame rate to 60 fps.
            self.clock.tick(60)

            # Display the screen.
            pygame.display.flip()


Game().run()
