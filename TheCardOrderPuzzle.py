'''
Solution to MPMP14: THE CARD ORDER PUZZLE
https://www.youtube.com/watch?v=8I1OCqX93XI

I actually originally solved this on paper.
This script is rather over-engineered for the sake of generality.

Output:
    Found 4 arrangements of 4 cards (out of 24) with no subsets of 3 cards in ascending or descending order.

'''

from itertools import permutations, combinations
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

def build_subset(perm, pick):
    result = []
    for i in range(len(perm)):
        if i in pick:
            result.append(perm[i])
    return result

def contains_ordered_subset(perm, subset_length):
    picks = list(combinations(range(len(perm)), subset_length))
    for pick in picks:
        sb = build_subset(perm, pick)
        if is_ordered_subset(sb):
            return True
    return False

def count_perms_with_no_ordered_subsets(top_card, subset_length, find_first=False):
    perms = permutations(range(1, top_card+1))

    count = 0
    for perm in perms:
        if not contains_ordered_subset(perm, subset_length):
            count += 1
            if find_first:
                break
    print(("Found %s arrangements of %s cards with no subsets"
        + " of %s cards in ascending or descending order.")
        %(count, top_card, subset_length))
    #pprint.pprint(perms_with_no_ordered_subsets)
    return count



if __name__ == "__main__":
    top_card = 4
    subset_length = 3
    if len(sys.argv) >= 2:
        top_card = int(sys.argv[1])
    if len(sys.argv) >= 3:
        subset_length = int(sys.argv[2])

    count_perms_with_no_ordered_subsets(top_card, subset_length, False)