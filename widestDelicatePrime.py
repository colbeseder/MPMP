'''

Not strictly a MPMP. From https://youtu.be/p3Khnx0lUDE?t=1691

Calculate Digitally Delicate Primes.
If this program runs indefinitely with no output, it may have found a digitally delicate prime. Or it may be hanging.

OUTPUT:
    294001
     - with 1 extra zeros
    505447
    584141
    604171
     - with 3 extra zeros
    971767
     - with 4 extra zeros
    ...
    10564877
     - with 6 extra zeros
'''

import math
from primes import is_prime

def length_of_number(n):
    return math.ceil(math.log10(n + 1))

def is_delicate_digit(n, position):
    counted_primes = 0
    current_digit = int(((n % 10**position) / 10**(position-1)))
    with_zeroed_digit = n - (current_digit * 10**(position-1))
    for i in range(0, 10):
        if is_prime(with_zeroed_digit + (i * 10**(position-1))):
            counted_primes += 1
    return counted_primes == 1

# Returns number of digits that are delicately prime (counting from right)
# Or None if less than the number of digits in the number
def get_width(n):
    if not is_prime(n):
        return None
    width = 0
    for position in range(1, 30): #Todo: make inifinite
        if is_delicate_digit(n, position):
            width += 1
        else:
            break
    if width < length_of_number(n):
        return None
    return width

def hunt():
    widest = None
    max_width = -math.inf

    n = 2
    while True:
        width = get_width(n)
        if width is not None:
            print (n)
            if width > max_width:
                max_width = width
                widest = n
            if width > length_of_number(n):
                print(" - with %s extra zeros"%(width - length_of_number(n)))
        n +=1

if __name__=='__main__':
    hunt()