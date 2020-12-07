'''
Solution to MPMP10: Avoid the Square!
https://www.youtube.com/watch?v=FMQQFbZaQTk


Output:
    Out of 44170 games, 1 tied games were found, in 0 seconds
    Example (locations of player 2 counters):
    [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (1, 1), (2, 2), (3, 2), (0, 3), (4, 3), (1, 4), (3, 4)]
    done.


'''



import itertools
from math import floor
import time

STOP_AT_FIRST_RESULT = True

t0 = time.time()

width = 5
height = width
tiles = width * height

# Tuples of coordinates of all possible squares
squares = []

# Flat array of each tile, containing a tuple of its x,y coordinates
grid_points = [(i%width, int((i - (i%width)) / height)) for i in range(tiles)]

def get_tile_from_coords(grid, coord):
    needleX, needleY = coord
    for idx in range(tiles):
        ix, iy = grid[idx]
        if ix == needleX and iy == needleY:
            return idx
    return False #Square goes out of bounds

'''
Find all the possible squares on the board.
Each square is defined by four tiles: (a,b,c,d) (clockwise)
Pick two squares: 'a' and 'b'. a will always be before b. Calculate c & d.
Add the coordinate group a,b,c,d to list of squares
'''
for idxA in range(tiles):
        a = grid_points[idxA]
        for idxB in range(idxA +1, tiles):
            b = grid_points[idxB]
            diff = (b[0] - a[0]) , ( b[1] - a[1]) #distance from a to b on x & y axes
            c = (a[0] - diff[1], diff[0] + a[1])
            d = (c[0]+diff[0], c[1]+diff[1])
            idxC = get_tile_from_coords(grid_points, c)
            idxD = get_tile_from_coords(grid_points, d)
            
            if not (idxC and idxD): #square extends out of bounds
                continue
            
            squares.append(sorted([idxA,idxB,idxC,idxD]))

# squares to contains all possible squares (may be some dupes)
squares = sorted([list(x) for x in set(tuple(x) for x in squares)])
print("Found %s possible squares"%(len(squares)))

#All possible game arrangements. List of player 2 tiles.
games = itertools.combinations([x for x in range(tiles)] , int(floor(tiles/2)))

'''
    Is game a draw. ie No squares
'''
def test_game(game, squares):
    # Run through all possible squares.
    for square in squares:
        vals = [x in game for x in square] # Map of goes. Player 1: False, P2: True
        if  vals[0] == vals[1] and vals[2] == vals[3] and vals[0] == vals[2]:
            # Corners of square are all for same player.
            return False
    return True # No squares found. Hooray!

tie_games = []

i = 0
for game in games:
    i += 1
    if test_game(game, squares):
        tie_games.append(game)
        #print(game)
        if STOP_AT_FIRST_RESULT:
            break

t1 = time.time()

print("Out of %s games, %s tied games were found, in %s seconds"%(i,len(tie_games), int(t1-t0)))
print("Example (locations of player 2 counters):")
print([grid_points[x] for x in tie_games[0]])
print("done.")
