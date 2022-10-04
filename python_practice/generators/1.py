def fib(n):
    a,b = 0,1
    count = 0
    while count < n:
        yield a
        c = a + b
        a = b
        b = c
        count += 1

obj1 = fib(5)

for i in obj1:
    print(i)