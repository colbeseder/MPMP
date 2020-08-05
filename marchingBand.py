'''
Solution to MPMP12: MARCHING BAND PROBLEM
https://www.youtube.com/watch?v=2DNokQGxqjE


Output:
    Use 7560 marchers to make 64 options

    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 18, 20, 21, 24, 27, 28, 30, 35, 36, 40, 42, 45, 54, 56, 60, 63, 70, 72, 84, 90, 105, 108, 120, 126, 135, 140, 168, 180, 189, 210, 216, 252, 270, 280, 315, 360, 378, 420, 504, 540, 630, 756, 840, 945, 1080, 1260, 1512, 1890, 2520, 3780, 7560]


'''

import math

target = 64


def numberOfOptions(numOfMarchers):
    # Every option will have one side less than the root of the numOfMarchers
    # Edge case: both sides are equal to the square root
    rootOf = math.sqrt(numOfMarchers)
    options = []
    for i in range(1, math.floor(rootOf) +1):
        if numOfMarchers % i == 0:
            options.append(i)
            if i != rootOf: # check for the edge case
                options.append(int(numOfMarchers /i))
    return len(options), options

i = 1
while True:
    num, options = numberOfOptions(i)
    if  num == target:
        print ("Use %s marchers to make %s options\n"%(i, target))
        options.sort()
        print(options)
        break
    i += 1