import numpy as np
import pygame as pg
import sys

ROWS = 6
COLUMNS = 7
CONNECT = 4

##############################################################################


def instructions():
    """ 
    Displays the game instructions
    """
    print("\n There are 6 ROWS and 7 COLUMNS indexed from 0")
    print(" Choose a number from 0-6 to drop your piece into a column \n")


def set_board():
    """
    Sets the board to play.
    @returns matrix
    """
    board = np.zeros((ROWS, COLUMNS), dtype="int8")
    return board


def validate_move(col, board):
    """
    Validates the user's move
    @returns boolean
    """
    if(0 <= col <= 6):
        return board[ROWS-1, col] == 0
    else:
        instructions()
        return False


def get_next_row(col, board):
    """
    Gets the next row of the column where a piece can be put.
    @returns int
    """
    for row in range(ROWS):
        if(board[row, col] == 0):
            return row


def drop(col, row, board, piece):
    """
    Sets the place where a piece was put
    """
    board[row, col] = piece


def show_board(board):
    """
    prints the board on screen.
    """
    print(np.flip(board, axis=0))


def check_row(row, board, piece):
    """
    Checks if any user has won in a row.
    @returns boolean
    """
    win = 0
    # print("checking row")
    for c in range(COLUMNS-CONNECT+1):
        for i in range(CONNECT):
            if(board[row, c+i] == piece):
                win += 1
        if(win == CONNECT):
            return True
        win = 0
    return False


def check_col(col, board, piece):
    """
    Checks if any user has won in a column.
    @returns boolean
    """
    win = 0
    # print("checking cols")
    for r in range(ROWS-CONNECT+1):
        for i in range(CONNECT):
            if(board[r + i, col] == piece):
                win += 1
        if(win == CONNECT):
            return True
        win = 0
    return False


def check_diag(row, col, board, piece):
    """
    Checks if any user has won in any of the 2 diagonals.
    @returns boolean
    """
    d1u = 0
    d1d = 0
    d2u = 0
    d2d = 0

    r = row
    c = col
    while(r != 0 and c != 0):
        if(board[r - 1, c - 1] != piece):
            break
        else:
            d1u += 1
        r -= 1
        c -= 1

    r = row
    c = col
    while(r + 1 != ROWS and c + 1 != COLUMNS):
        if(board[r + 1, c + 1] != piece):
            break
        else:
            d1d += 1
        r += 1
        c += 1

    if(d1u + d1d == CONNECT - 1):
        return True

    r = row
    c = col
    while(r != 0 and c + 1 != COLUMNS):
        if(board[r - 1, c + 1] != piece):
            break
        else:
            d2u += 1
        r -= 1
        c += 1

    r = row
    c = col
    while(r + 1 != ROWS and c != 0):
        if(board[r + 1, c - 1] != piece):
            break
        else:
            d2d += 1
        r += 1
        c -= 1

    if(d2u + d2d == CONNECT - 1):
        return True

    return False


def win(row, col, board, piece):
    """
    Checks if any user has won.
    @returns boolean
    """

    return (check_col(col, board, piece) or
            check_diag(row, col, board, piece) or
            check_row(row, board, piece))

########################################################################


def draw_board(board):
    """
    Draws the board on the screen to play.
    """
    for r in range(ROWS):
        for c in range(COLUMNS):
            pg.draw.rect(screen, (0, 0, 200),
                         (c*SQUARE_SIZE, (r+1)*SQUARE_SIZE,
                          SQUARE_SIZE, SQUARE_SIZE))

            pg.draw.circle(screen, (0, 0, 0), (c*SQUARE_SIZE +
                           SQUARE_SIZE/2, (r+1)*SQUARE_SIZE + SQUARE_SIZE/2),
                           RADIUS)

    for r in range(ROWS):
        for c in range(COLUMNS):
            if(board[r, c] == 1):

                pg.draw.circle(screen, (255, 0, 0),
                               (c*SQUARE_SIZE + SQUARE_SIZE/2,
                               HEIGHT - (r+1)*SQUARE_SIZE + SQUARE_SIZE/2),
                               RADIUS - 1)

            elif(board[r, c] == 2):
                pg.draw.circle(screen, (0, 255, 0),
                               (c*SQUARE_SIZE + SQUARE_SIZE/2,
                               HEIGHT - (r+1)*SQUARE_SIZE + SQUARE_SIZE/2),
                               RADIUS - 1)

    pg.display.update()     # updates the display on screen

########################################################################

board = set_board()     # initialising the game
turn = 0

pg.init()
myfont = pg.font.SysFont("Times New Roman", 32)
SQUARE_SIZE = 64
WIDTH = COLUMNS * SQUARE_SIZE
HEIGHT = (ROWS+1) * SQUARE_SIZE
DIMS = (WIDTH, HEIGHT)
RADIUS = int(SQUARE_SIZE/2 - 4)

screen = pg.display.set_mode(DIMS)
draw_board(board)
pg.display.update()

print("\t CONNECT 4 \n\n")
instructions()
show_board(board)

moves = ROWS * COLUMNS

#####################################################################
########################### END OF MODULE ###########################
#####################################################################