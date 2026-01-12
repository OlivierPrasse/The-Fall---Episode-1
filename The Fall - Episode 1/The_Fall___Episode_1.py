import sys
import math

piece_moves = {
    0: {},  # Vide
    1: {'TOP': (0, 1), 'LEFT': (0, 1), 'RIGHT': (0, 1)},
    2: {'LEFT': (1, 0), 'RIGHT': (-1, 0)},
    3: {'TOP': (0, 1)},
    4: {'TOP': (-1, 0), 'RIGHT': (0, 1)},
    5: {'TOP': (1, 0), 'LEFT': (0, 1)},
    6: {'LEFT': (1, 0), 'RIGHT': (-1, 0)},
    7: {'TOP': (0, 1), 'RIGHT': (0, 1)},
    8: {'LEFT': (0, 1), 'RIGHT': (0, 1)},
    9: {'TOP': (0, 1), 'LEFT': (0, 1)},
    10: {'TOP': (-1, 0)},
    11: {'TOP': (1, 0)},
    12: {'RIGHT': (0, 1)},
    13: {'LEFT': (0, 1)}
}

grid = []
# w: number of columns.
# h: number of rows.
w, h = [int(i) for i in input().split()]

grid = []
for i in range(h):
    line = input()  # represents a line in the grid and contains W integers. Each integer represents one room of a given type.
    line_data = [int(x) for x in line.split()]
    grid.append(line_data)

ex = int(input())  # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).

# game loop
while True:
    inputs = input().split()
    xi = int(inputs[0])
    yi = int(inputs[1])
    pos = inputs[2]

    current_piece_type = grid[yi][xi]
    
    move = piece_moves[current_piece_type][pos]

    next_x = xi + move[0]
    next_y = yi + move[1]

    print(f"{next_x} {next_y}")
