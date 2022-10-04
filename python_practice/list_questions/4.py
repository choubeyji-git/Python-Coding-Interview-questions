# Python Program to count unique values inside a list

lst = [1,'a',24,'sachin',1,'sachin',2,3]

count = 0

for i in lst:
    if lst.count(i) == 1:
        count += 1

print(count)        