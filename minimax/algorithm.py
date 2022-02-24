from copy import deepcopy
import pygame

RED = (255, 0, 0)
WHITE = (255, 255, 255)

def minimax(position, depth, max_player, min_player, game):
    if depth == 0:  # leaf
        return position.evaluate(), position
    
    if depth % 2 == 1:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, max_player, game):
            evaluation = minimax(move, depth-1, max_player, min_player, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, min_player, game):
            evaluation = minimax(move, depth-1, max_player, min_player, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        return minEval, best_move

def simulate_move(piece, move, board, game, eat_flag):
    if piece == 0:  # need debug
        return 0
    if eat_flag:
        remove_piece = board.get_piece(move[0], move[1])
        board.remove(remove_piece)    
    board.move(piece, move[0], move[1])
    
    return board

def get_all_moves(board, color, game):
    moves = []
    for piece in board.get_all_pieces(color):
        vaild_moves, eat = board.get_vaild_move(piece)
        for move in vaild_moves:
            eat_flag = 0
            for temp_eat in eat:
                if temp_eat == move:
                    eat_flag = 1
            #draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, eat_flag)
            if new_board == 0:  # need debug
                continue
            moves.append(new_board)
    return moves

def draw_moves(game, board, piece):
    valid_moves, eat = board.get_vaild_move(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0,255,0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves)
    pygame.display.update()
    