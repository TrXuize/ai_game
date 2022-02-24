import pygame
from .constants import BLACK, ROWS, COLS, RED, SQUARE_SIZE, WHITE
from .piece import Piece
class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = 5
        self.white_left = 5
        self.red_two_left = 2
        self.white_two_left = 2
        self.create_board()
    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def evaluate(self):
        return self.white_left - self.red_left + self.red_two_left*0.5 + self.white_two_left*0.5

    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces

    def move(self, piece, row, col):
        # swap
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row,col)

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        pic = ['A', 'B', 'E', 'F', 'G', 'X', 'Y', 'W', 'V', 'U']
        for row in range(ROWS):
            self.board.append([])

            for col in range(COLS):
                if (row == 0 or row == 7) and col < 5:
                    if (row == 0):
                        if(pic[col] == 'A' or pic[col] == 'B'):
                            self.board[row].append(Piece(row, col, pic[col], WHITE, 2))
                        else:
                            self.board[row].append(Piece(row, col, pic[col], WHITE, 1))
                    else:
                        if(pic[col+5] == 'X' or pic[col+5] == 'Y'):
                            self.board[row].append(Piece(row, col, pic[col+5], RED, 2))
                        else:
                            self.board[row].append(Piece(row, col, pic[col+5], RED, 1))
                else:
                    self.board[row].append(0)

    def checker_level(self, piece, row, col):
        return piece.level

    def remove(self, piece):
        self.board[piece.row][piece.col] = 0
        if piece.color == RED:
            self.red_left -= 1
        elif piece.color == WHITE:
            self.white_left -= 1
        
    def get_vaild_move(self, piece):
        moves = []
        eat = []
        if piece.level == 2:
            if piece.row - 1 < 0:   # 最上,只能往下
                moves.append((piece.row+1, piece.col))
                moves.append((piece.row+2, piece.col))
            elif piece.row - 2 < 0:  # 第二row, 可上一格
                moves.append((piece.row-1, piece.col))
                moves.append((piece.row+1, piece.col))
                moves.append((piece.row+2, piece.col))
            elif piece.row + 1 > 7: # 最下,只能上
                moves.append((piece.row-1, piece.col))
                moves.append((piece.row-2, piece.col))
            elif piece.row + 2 > 7: # 倒數第二row,可下一格
                moves.append((piece.row-1, piece.col))
                moves.append((piece.row-2, piece.col))
                moves.append((piece.row+1, piece.col))
            else:   # no restrict
                moves.append((piece.row+1, piece.col))
                moves.append((piece.row+2, piece.col))
                moves.append((piece.row-1, piece.col))
                moves.append((piece.row-2, piece.col))

            if piece.col -1 < 0:    # 最左, 只能往右
                moves.append((piece.row, piece.col+1))
                moves.append((piece.row, piece.col+2))
            elif piece.col -2 < 0:
                moves.append((piece.row, piece.col-1))
                moves.append((piece.row, piece.col+1))
                moves.append((piece.row, piece.col+2))
            elif piece.col + 1 > 7:
                moves.append((piece.row, piece.col-1))
                moves.append((piece.row, piece.col-2))
            elif piece.col + 2 > 7:
                moves.append((piece.row, piece.col-1))
                moves.append((piece.row, piece.col-2))
                moves.append((piece.row, piece.col+2))
            else:
                moves.append((piece.row, piece.col+1))
                moves.append((piece.row, piece.col+2))
                moves.append((piece.row, piece.col-1))
                moves.append((piece.row, piece.col-2))

        else:
            if piece.row - 1 < 0:
                moves.append((piece.row+1, piece.col))
            elif piece.row + 1 > 7:
                moves.append((piece.row-1, piece.col))
            else:
                moves.append((piece.row-1, piece.col))
                moves.append((piece.row+1, piece.col))
            
            if piece.col - 1 < 0:
                moves.append((piece.row, piece.col+1))
            elif piece.col + 1 > 7:
                moves.append((piece.row, piece.col-1))
            else:
                moves.append((piece.row, piece.col+1))
                moves.append((piece.row, piece.col-1))

        for move in moves[:]:  # 去掉隊友 標記吃
            print(move)
            if (move[0] > 8) or (move[0] < 0) or (move[1] > 8) or (move[1] < 0):
                moves.remove(move)
            if self.board[move[0]][move[1]] != 0: 
                if piece.color == self.board[move[0]][move[1]].color:
                    moves.remove(move)
                elif piece.color != self.board[move[0]][move[1]].color:
                    eat.append(move)
        return moves, eat


    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)
