def odd_even(num):
    def numbers(a,b):
        sum = a + b
        if sum%2 == 0:
            print('even')
        else:
            print('odd')
        num(a,b)
    return numbers

@odd_even
def two_sum(a,b):
    sum = a + b
    print(sum)

two_sum(2,2)