from gametools import *

# Playing the game.

"""
The following code implements the UI of the game.
Using pygame library, the board is displayed and 
updated every time the user takes his/her turn.
Pygame also provides for the user interaction.
"""
while(moves > 0):

    for event in pg.event.get():
        if(event.type == pg.QUIT):
            sys.exit(0)
        elif(event.type == pg.MOUSEMOTION):
            pg.draw.rect(screen, (0, 0, 0), (0, 0, WIDTH, SQUARE_SIZE))
            posx = event.pos[0]
            if(turn == 0):
                pg.draw.circle(screen, (255, 0, 0),
                               (posx, SQUARE_SIZE//2), RADIUS - 1)
            else:
                pg.draw.circle(screen, (0, 255, 0),
                               (posx, SQUARE_SIZE//2), RADIUS - 1)
            pg.display.update()

        elif(event.type == pg.MOUSEBUTTONDOWN):

            if(turn == 0):
                col = int(event.pos[0]/SQUARE_SIZE)
                if(validate_move(col, board)):
                    row = get_next_row(col, board)
                    drop(col, row, board, 1)
                else:
                    print("\n INVALID MOVE")
            else:
                col = int(event.pos[0]/SQUARE_SIZE)
                if(validate_move(col, board)):
                    row = get_next_row(col, board)
                    drop(col, row, board, 2)
                else:
                    print("\n INVALID MOVE")
                    continue

            if(win(row, col, board, turn+1)):
                print(f"\n CONGRATULATIONS : PLAYER {turn+1} WINS !\n")
                pg.draw.rect(screen, (0, 0, 0), (0, 0, WIDTH, SQUARE_SIZE))
                label = myfont.render(
                    f"PLAYER {turn+1} WINS !", 1, (255, 0, 0) if turn == 0
                    else (0, 255, 0))
                screen.blit(label, (100, 10))
                show_board(board)
                draw_board(board)
                pg.display.update()
                pg.time.wait(3000)
                sys.exit(0)

            show_board(board)
            draw_board(board)
            pg.display.update()
            turn = (turn + 1) % 2
            moves -= 1
            if(turn == 0):
                pg.draw.circle(screen, (255, 0, 0),
                               (posx, SQUARE_SIZE//2), RADIUS - 1)
            else:
                pg.draw.circle(screen, (0, 255, 0),
                               (posx, SQUARE_SIZE//2), RADIUS - 1)
            pg.display.update()

print("\n TIE ")

sys.exit(0)

###################################################################
########################### END OF CODE ###########################
###################################################################
