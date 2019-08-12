import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False
is_blue = True

clock = pygame.time.Clock()

IMAGE = pygame.image.load('bird.png')
bird = pygame.transform.scale(IMAGE, (50, 50))

class Sprite:
    def __init__(self):
        self.x = 50
        self.y = 300
        self.width = 30
        self.height = 30
        self.color = (0, 128, 255)
    def draw(self, x, y):
        screen.blit(bird,(x,y))

    def falldown(self):
        if (self.y < 570):
            self.y += 3

    def goUp(self):
        '''for i in range(10):
            self.draw(self.x,self.y)
            self.y-=2'''
        self.y -= 13

class Obstacle:
    def __init__(self):
        self.x = 800
        self.topy = 0
        self.height = random.randrange(100, 300)
        self.width = 30
        self.bottomy = self.height + 200
        self.color = (0, 255, 0)
    def draw(self):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.topy, self.width, self.height))
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.bottomy, self.width, 600 - self.bottomy))
    def move(self):
        self.x -= 4

    def collide(self,sprite):
        return ((sprite.x + 2*sprite.width > self.x) and ((sprite.y <= self.topy + self.height) or (sprite.y > self.bottomy)))
    def reset(self):
        self.x = 800
        self.height = random.randrange(100, 300)
        self.bottomy = self.height + 200

sprite = Sprite()
obstacle = Obstacle()
obstacle1 = Obstacle()
obstacle1.x = 1200
while not done and not (obstacle.collide(sprite) or obstacle1.collide(sprite)):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #if (x + 30 >= topx and x <= topx + 30 and (y < height or y + 30 > bottomy)):
    #    print(x, y, topx, bottomy, )
    #    break

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        if (sprite.y > 0):
            # y -= 20
            sprite.goUp()
            # if pressed[pygame.K_DOWN]: y += 3
    # if pressed[pygame.K_LEFT]: x -= 3
    # if pressed[pygame.K_RIGHT]: x += 3i
    sprite.falldown()
    screen.fill((0, 0, 0))
    if(obstacle1.x < 0):
        obstacle1.reset()
    if (obstacle.x < 0):
        obstacle.reset()
    sprite.draw(sprite.x, sprite.y)
    obstacle1.move()
    obstacle1.draw()
    obstacle.move()
    obstacle.draw()



    pygame.display.flip()
    clock.tick(60)
pygame.quit()
