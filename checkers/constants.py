import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

A = pygame.transform.scale(pygame.image.load('pic/A.png'), (45, 25))
B = pygame.transform.scale(pygame.image.load('pic/B.png'), (45, 25))
E = pygame.transform.scale(pygame.image.load('pic/E.png'), (45, 25))
F = pygame.transform.scale(pygame.image.load('pic/F.png'), (45, 25))
G = pygame.transform.scale(pygame.image.load('pic/G.png'), (45, 25))
U = pygame.transform.scale(pygame.image.load('pic/U.png'), (45, 25))
V = pygame.transform.scale(pygame.image.load('pic/V.png'), (45, 25))
W = pygame.transform.scale(pygame.image.load('pic/W.png'), (45, 25))
X = pygame.transform.scale(pygame.image.load('pic/X.png'), (45, 25))
Y = pygame.transform.scale(pygame.image.load('pic/Y.png'), (45, 25))