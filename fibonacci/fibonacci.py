fibonacci_cache = {0: 0, 1: 1}

def fibonacci_of(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    fibonacci_cache[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)
    return fibonacci_cache[n]

print([fibonacci_of(n) for n in range(15)])