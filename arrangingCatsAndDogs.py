'''
Solution to the MPMP17: ARRANGING CATS AND DOGS PUZZLE
https://youtu.be/8gppjTZ1vCE

Output:
    For a row of 10 cages, there are 144 unique arrangements of animals without putting two cats next to each other.

'''

from itertools import permutations
from math import floor

CAGES = 10

#enum
CAT = 0
DOG = 1

def is_good_perm(perm):
    for i in range(len(perm)-1):
        if perm[i] == CAT and perm[i+1] == CAT:
            return False
    return True

def num_good_by_dogs(num_dogs):
    perms = permutations((num_dogs * [DOG]) + ((CAGES - num_dogs) * [CAT]))
    uniques = set()
    for perm in perms:
        if perm in uniques: # for speed
            continue
        if is_good_perm(perm):
            uniques.add(perm)
    return len(uniques)

def num_good_by_cages(cages):
    total = 0
    min = floor(cages/2)
    for dogs in range(min, cages+1):
        total += num_good_by_dogs(dogs)
    return total

print("For a row of %s cages, there are %s unique arrangements of animals without putting two cats next to each other."%(CAGES, num_good_by_cages(CAGES)))