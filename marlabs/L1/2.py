def fib():
    a,b = 0,1
    while True:
        yield a
        c = a + b
        a = b
        b = c


n = fib()

print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))