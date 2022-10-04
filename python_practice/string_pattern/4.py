def group_str(lst,x,y):
    concatenated_string = ''
    for i in lst[x:y]:
        concatenated_string += str(i)

    return concatenated_string

lst = ['k','d','a','b','g','h']

x = 1
y = 4

print(group_str(lst,x,y))