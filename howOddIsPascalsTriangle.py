'''
Solution to MPMP16: HOW ODD IS PASCAL'S TRIANGLE?
https://www.youtube.com/watch?v=tjJ2qL9uaz4

We'll generate Pascal's Triangle but just 1's & 0's as that's enough to continue the odds && evens.
Note (a+b)%2 is equivalent to a^b.

BTW, if you consider the row as a binary number, you can get the next row like this:
    row ^= (row <<1)
Might be fun to implement in C or Go, using a uint64 for half the synetrical row.

Output:
    26.489825581395348 % of numbers are odd in the top 128 rows of Pascal's Triangle (2187 out of 8256)

'''

last_row = 128

this_row = [1]
odds = 0
evens = 0

def get_next_row(this_row):
    next_row = [1]
    for i in range(1, len(this_row)):
        next_row.append(this_row[i-1] ^ this_row[i])
    next_row.append(1)
    return next_row
        
for i in range(last_row):
    odds += this_row.count(1)
    evens += this_row.count(0)
    this_row = get_next_row(this_row)

total = odds + evens
percent = 100 * odds/total

print("%s %% of numbers are odd in the top %s rows of Pascal's Triangle (%s out of %s)"%(percent, last_row, odds, total))
