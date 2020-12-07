'''
MPMP19: The 19 Challenge
https://youtu.be/tBXGIXEV7tI

Output:
    Valid values of 'n', where the sum of the first n primes, squared is a multiple of n are:
    1, 19, 37, 455, 509, 575, 20597, 202717, 202717, 1864637, 
'''
def gen_primes():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

primes = gen_primes()
print("Valid values of 'n', where the sum of the first n primes, squared is a multiple of n are:")
sum_of_squares = 0
for i, p in enumerate(primes):
    n = i+1
    sum_of_squares += (p**2)
    if sum_of_squares % n == 0:
        print(n, end=', ', flush=True)