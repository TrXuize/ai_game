from .constants import RED, WHITE, SQUARE_SIZE, GREY, A, B, E, F, G, X, Y, W, V, U
import pygame
# AB XY 上下左右動兩格 吃AB XY get higher score
class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, pic, color, level):
        self.row = row
        self.col = col
        self.pic = pic
        self.color = color
        self.level = level

        self.x = 0
        self.y = 0
        self.clac_pos()

    def clac_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def draw(self, win):
        if self.pic == 'A':
            win.blit(A, (self.x - A.get_width()//2, self.y - A.get_height()//2))
        elif self.pic == 'B':
            win.blit(B, (self.x - B.get_width()//2, self.y - B.get_height()//2))
        elif self.pic == 'E':
            win.blit(E, (self.x - E.get_width()//2, self.y - E.get_height()//2))
        elif self.pic == 'F':
            win.blit(F, (self.x - F.get_width()//2, self.y - F.get_height()//2))
        elif self.pic == 'G':
            win.blit(G, (self.x - G.get_width()//2, self.y - G.get_height()//2))
        elif self.pic == 'X':
            win.blit(X, (self.x - X.get_width()//2, self.y - X.get_height()//2))
        elif self.pic == 'Y':
            win.blit(Y, (self.x - Y.get_width()//2, self.y - Y.get_height()//2))
        elif self.pic == 'W':
            win.blit(W, (self.x - W.get_width()//2, self.y - W.get_height()//2))
        elif self.pic == 'V':
            win.blit(V, (self.x - V.get_width()//2, self.y - V.get_height()//2))
        elif self.pic == 'U':
            win.blit(U, (self.x - U.get_width()//2, self.y - U.get_height()//2))
    def move(self, row, col):
        self.row = row
        self.col = col
        self.clac_pos()
 

    def __repr__(self):
        return str(self.color)