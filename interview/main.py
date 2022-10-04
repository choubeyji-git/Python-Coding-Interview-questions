# op target = 13;


# [1,3,4,5]
# [1,12] 
# [5,8]
# [3,4,6]
# [8, 4, 1]

sum_of_list = 13
lst = [ 3,1,4,12,8,5,6 ]
l = len(lst)

for i in range(l):
    for j in range(l):
        print(i+j)
        