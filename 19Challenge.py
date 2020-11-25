'''
MPMP19: The 19 Challenge
https://youtu.be/tBXGIXEV7tI

Output:
    The highest 'n' (up to 33860), where the first n primes squared add to a multiple of n is 20597
'''

class sumSquareFinder():
    def getSumsOfSquares(self, primes):
        self.sum_sqrs = []
        for i, p in enumerate(primes):
            if i == 0:
                self.sum_sqrs.append(p**2)
            else:
                self.sum_sqrs.append((p**2) + self.sum_sqrs[i-1])

    def checkN(self, n):
        if self.sum_sqrs[n-1] % n == 0:
            return True
        return False
        
    def findHighest(self):
        for i in range(len(primes)-1, -1, -1):
            if self.checkN(i):
                return i
        return None

    def __init__(self, primes):
        self.getSumsOfSquares(primes)
        
        
if __name__ == "__main__":
    import json
    with open('resources/primes.json') as f:
        primes = json.load(f)["primes"]

    finder = sumSquareFinder(primes)
    highestN = finder.findHighest()
    print("The highest 'n' (up to %s), where the first n primes squared add to a multiple of n is %s"%(len(primes), highestN))
