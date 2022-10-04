#main decorator example
def sum_dec(nums):
    def sum_func(a,b):
        if (a+b)%2 ==0:
            print("even")
            return a+b
        else:
            print("odd")
            return a+b
    return sum_func   



@sum_dec
def sum_of_nums(a,b):
    return (a+b)


print(sum_of_nums(1,2))