#count no. of frequency of characters
lst = [1,'a',24,'sachin',1,'sachin',2,3]
d={}
for i in lst:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)