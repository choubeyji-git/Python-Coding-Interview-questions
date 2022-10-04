lst = [1,2,3,4,5,6]
lst2 = [89,90,91,92,93]
my_dict = {k:k*k*k for k in lst}


my_dict2 = dict(zip(lst,lst2))

print(my_dict2)