from random import choice
import time

from visual import *

from settings import *
from utils import *


def game_over():
    print "GAME OVER: score {}".format(score)
    exit()


def play(t_stamp = [time.time(), 0]):
    """ play() is the core engine of this game
        This function changes the position
        every steps.
    """

    global piece, px, py, pc, focus, score
    global speed_rate

    # Time goes on
    t_stamp[1] = time.time()
    if t_stamp[1] - t_stamp[0] > speed_rate and not scene.pause:
    
        # Descend
        if not collide(piece, px, py + 1):
            py += 1

        elif py < 0:
            # Hit the top, Game Over
            game_over()
            return

        else:
            # Hit the bottom, place the block
            place_piece(piece, px, py, pc)

            # Check if there are lines
            clear = clear_complete_lines()
          
            if clear:
                score += len(clear)


            # Produce a new box
            piece, px, py, pc = new_block(choice(block.keys()))
            focus = new_focus(piece, pc)


        t_stamp[0] = t_stamp[1]

    # Key board Control
    if scene.kb.keys:
        key = scene.kb.getkey()
        if key == 'down':
            if not collide(piece, px, py + 1):
                py += 1
        
        elif key == 'up':
            npiece = [(j, -i+3) for (i, j) in piece]
            if not collide(npiece, px, py): piece = npiece
        
        elif key in ('left', 'right'):
            npx = px + (-1 if key in ('left') else 1)
            if not collide(piece, npx, py): px = npx
        
        elif key == 'backspace':
            scene.pause = not scene.pause

        elif key in ('[', ']'):
            speed_rate = speed_rate + (0.1 if key in '[' else -0.1)

    # Change the position
    for i in xrange(4): focus[i].pos = vector(px, py) + piece[i]


if __name__ == '__main__':
    
    # Place the first block
    piece, px, py, pc = new_block(choice(block.keys()))
    focus = new_focus(piece, pc)
    
    while 1:
        rate(50)
        play()
