from functools import cache
from tracemalloc import start
import time

@cache
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

start = time.time()
for n in range(1, 101):
    print(n, ";", fibonacci(n))
end = time.time()

print(end-start)