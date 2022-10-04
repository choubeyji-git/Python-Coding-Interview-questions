def get_fib(num):
    a ,b = 0 ,1
    count = 0
    while count < num :
        yield a
        c = a + b
        a = b
        b = c
        count += 1

fib1 = get_fib(7)

for i in fib1:
    print(i)

