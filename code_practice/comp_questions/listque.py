lst1="Roses are red"
x1,x2= 2,6
print(lst1[x1:x2])

list1=[1,5,17,18,23,1,5]
list2=[]
tcount=len(list1)
for e in range(0,len(list1)):
    list2.append(list1[tcount-1-e])
print(set(list2))


a=[6,1,8,2,11,1,7,6]
#output=[1,2,6]
a.sort()
print(a)
lst=list(set(a))
print(lst)
lst1=[]
for i in range(0,3):
    lst1.append(lst[i])
print(lst1)