my_str = 'SSKLOPYYY'

lst = [i for i in my_str]
d = {}
for i in lst :
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1

print(d)



