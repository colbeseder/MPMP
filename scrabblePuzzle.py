'''

MPMP: SCRABBLE PUZZLE
https://youtu.be/JaXo_i3ktwM

Find Number of distinct 7 letter scrabble hands that score 46

Output:
    There are 138 distinct 7 letter scrabble hands that score 46 points
    eg. 'qzjxafk'

'''

# All 46 scores must include Q,Z,X,J, (36 points)
# Proof: Max possible score without one of the top 4 tiles is 45 (10,10,8,5,4,4,4)
# Number of 7 letter hands that score 46 is equal
# to number number of 3 letter hands that score 10 (46-36), excluding the big 4 tiles


from itertools import *

def sum_values(combo):
    return sum([x["value"] for x in combo])

def summary(combo):
    return ''.join([x["name"] for x in combo])

letter_pool = [{"name": "a", "value": 1}] * 9 +[{"name": "b", "value": 3}] * 2 +[{"name": "c", "value": 3}] * 2 +[{"name": "d", "value": 2}] * 4 +[{"name": "e", "value": 1}] * 12 +[{"name": "f", "value": 4}] * 2 +[{"name": "g", "value": 2}] * 3 +[{"name": "h", "value": 4}] * 2 +[{"name": "i", "value": 1}] * 9 +[{"name": "k", "value": 5}] * 1 +[{"name": "l", "value": 1}] * 4 +[{"name": "m", "value": 3}] * 2 +[{"name": "n", "value": 1}] * 6 +[{"name": "o", "value": 1}] * 8 +[{"name": "p", "value": 3}] * 2 +[{"name": "r", "value": 1}] * 6 +[{"name": "s", "value": 1}] * 4 +[{"name": "t", "value": 1}] * 6 +[{"name": "u", "value": 1}] * 4 +[{"name": "v", "value": 4}] * 2 +[{"name": "w", "value": 4}] * 2 +[{"name": "y", "value": 4}] * 2 +[{"name": "?", "value": 0}] * 2
combos = combinations(letter_pool, 3)

found = {}

result = 0
for combo in combos:
    if sum_values(combo) == 10:
        s = summary(combo)
        if s not in found: #prevent indistinct combinations (ie. different instance of same letter)
            #print("%s %s"%(s, len(found)))
            # Add combination to list
            found[summary(combo)] = 1

print("There are %s distinct 7 letter scrabble hands that score 46 points"%(len(found)))
print("eg. 'qzjx%s'"%(next(iter(found))))
