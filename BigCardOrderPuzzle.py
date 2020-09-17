from itertools import permutations, combinations
import pprint, sys
from TheCardOrderPuzzle import *

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