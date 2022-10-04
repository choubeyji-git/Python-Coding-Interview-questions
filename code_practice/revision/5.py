def fib(n):
    a,b = 0,1
    for _ in range(n):
        yield a
        c = a + b
        a = b
        b = c
        
y = fib(10)

for i in y:
    print(i)