import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.game import Game
from minimax.algorithm import minimax

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    
    while run:
        clock.tick(FPS)

        mykeyslist = pygame.key.get_pressed()
        if game.turn == WHITE:
            if mykeyslist[pygame.K_RIGHT]:
                opponent = 0
                if game.turn == RED:
                    opponent = WHITE
                elif game.turn == WHITE:
                    opponent = RED

                value, new_board = minimax(game.get_board(), 3, game.turn, opponent, game)
                game.ai_move(new_board)

        if mykeyslist[pygame.K_LEFT]:
            if game.turn == RED:
                game.turn = WHITE
            else:
                game.turn = RED
            print(game.turn)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
                        
        game.update()

    pygame.quit()

main()