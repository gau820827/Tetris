from settings import *


def new_board_lines(num):
    """ Produce new lines
    @param num: The number of new lines.

    @return: A list of zeros, which means a new line.
    """
    

    assert isinstance(num, int), num
    return [[0] * BOARD_WIDTH for j in range(num)]


# Initial Board information
board = new_board_lines(BOARD_HEIGHT)


def place_piece(piece, px, py, pc):
    """ Place the piece on the board
    @param piece   : the shape of the block
           px,py,pc: information of the block
    """
    

    for i, j in piece:
        x = px + i
        y = py + j
        if not (0 <= x < BOARD_WIDTH):
            continue
        if not (0 <= y < BOARD_HEIGHT):
            continue
        board[y][x] = pc


def clear_complete_lines():
    """ This function checks whether there are lines or not.

    @returns: A list recorded where the full lines are.
    """
    global board


    nb = []
    fn = []
    for idl, line in enumerate(board):
        if 0 in line:
            # Not full
            nb.append(line)
        else:
            fn.append(idl)

    if fn:
        # Update the board information
        board = new_board_lines(len(fn)) + nb

    # clear
    d_line = [obj for obj in scene.objects if type(obj) is box and obj.y in fn]
    for _ in xrange(10):
        rate(20)
        for obj in d_line:
            obj.opacity -= 0.1
    for obj in d_line:
        obj.visible = 0


    # decline
    for n in fn:
        for obj in (obj for obj in scene.objects if type(obj) is box and obj.y < n):
            obj.y += 1

    return fn


def collide(piece, px, py):
    """ Check if the position(px,py) collides with the board
    @param piece: the shape of the block
              px: x of the new position
              py: y of the new position
    @returns: True or False
    """
    for (i, j) in piece:
        x = px + i
        y = py + j
        if not (0 <= x < BOARD_WIDTH):
            return True
        if y >= BOARD_HEIGHT:
            return True
        if y < 0:
            continue
        if board[y][x]:
            return True
    return False