'''
Solution to MPMP14: BIG CARD ORDER PUZZLE
https://www.youtube.com/watch?v=8I1OCqX93XI

Output:
    Found 0 arrangements of 10 cards with no subsets of 1 cards in ascending or descending order.
    Found 0 arrangements of 10 cards with no subsets of 2 cards in ascending or descending order.
    Found 0 arrangements of 10 cards with no subsets of 3 cards in ascending or descending order.
    Found 0 arrangements of 10 cards with no subsets of 4 cards in ascending or descending order.
    Found 1 arrangements of 10 cards with no subsets of 5 cards in ascending or descending order.

    All arrangements of 10 cards have an ordered 4 card subset.
    Done in 361.1527693271637 seconds

'''

from itertools import permutations, combinations
import pprint, sys, time
from TheCardOrderPuzzle import *

start_time = time.time()
top_card = 10
starting_subset_length = 1
if len(sys.argv) >= 2:
    top_card = int(sys.argv[1])
if len(sys.argv) >= 3:
    starting_subset_length = int(sys.argv[2])

for i in range(starting_subset_length, top_card+1):
    count = count_perms_with_no_ordered_subsets(top_card, i, True)
    if count != 0:
        print("\nAll arrangements of %s cards have an ordered %s card subset."%(top_card, i-1))
        break

print("Done in %s seconds"%(time.time() - start_time))
