import pygame
from pygame.locals import *

import sys
from random import random

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

    def update(self, gameObjects):
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
        self.type = "player"
        self.gameOver = False

    def draw(self, surface):
        pygame.draw.circle(
            surface, RED, (int(self.x), int(self.y)), self.radius)

    def update(self, gameObjects):
        # In every frame, check the location of the mouse
        # and set the players' objects’ location to that point.
        cord = pygame.mouse.get_pos()
        self.x = cord[0]
        self.y = cord[1]

        # Check for collisions between the player and balls.
        for gameObj in gameObjects:
            if gameObj.type == "ball":
                # End the game if the player gets "hit
                # (x2-x1)^2 + (y1-y2)^2 <= (r1+r2)^2
                # meaning the distance between the center points is less than the sum of the radii.
                if (gameObj.x - self.x) ** 2 + (gameObj.y - self.y)**2 <= (gameObj.radius + self.radius)**2:
                    # how the game ends -  will freeze everything in place
                    self.gameOver = True


class GameController:
    """Game controllers are responsible for "running" the game.
    The controller will periodically add another ball to the screen 
    to make the game harder."""

    def __init__(self, interval=5):
        self.inter = interval
        self.next = pygame.time.get_ticks() + (2 * 1000)
        self.type = "game controller"
        # Adding a Score
        self.score = 0
        self.scoreText = pygame.font.Font(None, 20)

    def update(self, gameObjects):
        """Check how much time has passed since the time a ball was added or from the start of the game"""
        # If the time is more than the interval you'll reset the time and add a ball.
        if self.next < pygame.time.get_ticks():
            self.next = pygame.time.get_ticks() + (self.inter * 1000)
            # Give the balls random velocities.
            gameObjects.append(Ball(BLACK, xVel=random()*2, yVel=random()*2))
            self.score += 1

    def draw(self, screen):
        # Since it is a game object, the main loop will try to draw it
        screen.blit(self.scoreText.render(
            str(self.score), True, BLACK), (5, 5))


class Game:
    """Make the game loop into a class.
    Responsible for drawing and updating all our objects"""

    def __init__(self):
        # Pygame needs to be initialized to use
        # certain features like text or sound.
        pygame.init()
        self.screen = pygame.display.set_mode(RESOLUTION)
        self.clock = pygame.time.Clock()
        self.gameObjects = []
        # The game should now spawn a ball every five seconds.
        self.gameObjects.append(GameController())
        # Create a new player instance and add it to the list.
        self.gameObjects.append(Player())
        self.gameOver = False

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

            # When gameOver is set, stop updating objects
            if not self.gameOver:
                # update all objects in the array every loop.
                for gameObj in self.gameObjects:
                    gameObj.update(self.gameObjects)
                    if gameObj.type == "player":
                        self.gameOver = gameObj.gameOver

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
