'''
Solution to MPMP14: THE CARD ORDER PUZZLE
https://www.youtube.com/watch?v=8I1OCqX93XI

I actually originally solved this on paper.
This script is rather over-engineered for the sake of generality.

Output:
    Found 4 arrangements of 4 cards with no subsets of 3 cards in ascending or descending order.

'''

from itertools import permutations
import pprint, sys

def is_ordered_subset(sb):
    ordered_asc = True
    for i in range(1, len(sb)):
        if sb[i-1] > sb[i]:
            ordered_asc = False

    ordered_dec = True
    for i in range(1, len(sb)):
        if sb[i-1] < sb[i]:
            ordered_dec = False
    return ordered_asc or ordered_dec

def contains_ordered_subset(perm):
    for i in range(len(perm)):
        if is_ordered_subset(perm[:i] + perm[i+1:]):
            return True
    return False


top_card = 4
if len(sys.argv) >= 2:
    top_card = int(sys.argv[1])

perms = permutations(range(1, top_card+1))
perms_with_no_ordered_subsets = list(filter(lambda perm: not contains_ordered_subset(perm), perms))

print(("Found %s arrangements of %s cards with no subsets"
    + " of %s cards in ascending or descending order.")
    %(len(perms_with_no_ordered_subsets), top_card, top_card-1))

#pprint.pprint(perms_with_no_ordered_subsets)