'''
Solution to MPMP15: PRIME PAIRS PUZZLE
https://www.youtube.com/watch?v=AXfl_e33Gt4

Output:
    Found 140 arrangements of the numbers 1 to 9 (of 362880 total) where all adjacent pairs sum to a prime number
    eg. [1, 2, 3, 4, 7, 6, 5, 8, 9]

'''

from itertools import permutations
from math import factorial

MAX = 9
FIND_FIRST_ONLY = False

def nPr(n, r):
    return int(factorial(n)/factorial(n-r))

primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
if 2*MAX-1 > primes_list[-1]:
    raise Exception("Not enough primes!")
primes = set(primes_list)
    
def is_prime(x):
    return x in primes;

def is_prime_pairs(perm):
    for i in range(len(perm)-1):
        if not is_prime(perm[i] + perm[i+1]):
            return False
    return True


good_answers = []

for perm in permutations(range(1, MAX+1)):
    if is_prime_pairs(perm):
        good_answers.append(perm)
        if FIND_FIRST_ONLY:
            break


print("Found %s arrangements of the numbers 1 to %s (of %s total) where all adjacent pairs sum to a prime number"%(len(good_answers), MAX, nPr(9,9)))
print("eg. [%s]"%(", ".join(str(x) for x in good_answers[0])))