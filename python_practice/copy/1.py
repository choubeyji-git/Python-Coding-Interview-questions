import copy

lst = [1,2,3,[4,8],5,6]

def shallow_copy(lst):
    c_lst = copy.copy(lst)
    lst[3][0] = 8

    return c_lst,lst

def deep_copy(lst):
    c_lst = copy.deepcopy(lst)
    lst[3][0] = 8
    return c_lst,lst

print(shallow_copy(lst))
   
