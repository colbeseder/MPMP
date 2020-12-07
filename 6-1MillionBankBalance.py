'''
MPMP6: The 1 Million Bank Balance puzzle
https://www.youtube.com/watch?v=ILrqPpLpwpE


Output:
    Max: 19 days
    (144, 154)
'''

class Fib():
    cache = [0, 1, 1]
    def get(self, n):
        while len(Fib.cache) <= n:
            Fib.cache.append(Fib.cache[-1] + Fib.cache[-2])
        return Fib.cache[n]

target = 1000000
max = 0
result = (None, None)
m = None

fib = Fib()

for days in range(15, 31):
    a = fib.get(days)
    b = fib.get(days -1)
    for x in range(1, target):
        y = (target - (a*x)) / b
        if y < 0:
            break
        if y % 1 == 0:
            max = days
            m = (x, int(y))
            result = m

print("Max: %s days"%max)
print("(%s, %s)"%(result[0], result[1]))