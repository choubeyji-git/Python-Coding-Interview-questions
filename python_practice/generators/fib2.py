def get_fib_2(num):
    a,b = 0,1
    count = 0

    while count < num:
        yield a
        c = a+b
        a = b
        b = c
        count += 1

fib2 = get_fib_2(10)

for i in fib2:
    print(i)
