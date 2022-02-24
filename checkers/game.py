import pygame
from .constants import RED, WHITE, BLUE, SQUARE_SIZE
from .board import Board

class Game:
    def __init__(self, win):
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.win = win
        self.level = 0
        self.vaild_moves = []

    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def get_row_col_from_mouse(pos):
        x, y = pos
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        return row, col

    # set checkers click button -> start
    #def _init(self): # set checker K_KP_ENTER
    #    for event in pygame.event.get():

    
    def select(self, row, col):
        if self.selected:   # 若已選好, 又按空白格則動，選的格子不能有隊友
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        piece = self.board.get_piece(row, col)

        if piece != 0 and piece.color == self.turn: # 選要動的棋
            self.selected = piece
            self.vaild_moves, eat = self.board.get_vaild_move(self.selected)
            return True
        
        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        
        if self.selected and piece == 0 and (row, col) in self.vaild_moves:
            self.board.move(self.selected, row, col)
            self.change_turn()
        elif self.selected and (row, col) in self.vaild_moves and piece.color != self.turn:   # 吃   
            remove_piece = self.board.get_piece(row, col)
            self.board.remove(remove_piece) 
            self.board.move(self.selected, row, col)
            self.change_turn()
        else:
            return False
        
        return True

    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.change_turn()

    def change_turn(self):
        self.vaild_moves = []
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED
    
    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)